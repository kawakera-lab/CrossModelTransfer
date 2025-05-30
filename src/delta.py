import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class LoRALayer(nn.Module):
    """LoRA or Linear layer with additional weight"""
    def __init__(
        self,
        in_features: int,
        out_features: int,
        r: int = 0,
        alpha: int = 0,
        bias: bool = True,
    ):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.r = r
        self.alpha = alpha
        self.bias = bias

        if r > 0:
            self.A = nn.Parameter(torch.empty(r, in_features))
            self.B = nn.Parameter(torch.empty(out_features, r))
            self.reset_parameters()
        else:
            self.D = nn.Parameter(torch.zeros(in_features, out_features))
            nn.init.zeros_(self.D)

            if bias:
                self.b = nn.Parameter(torch.zeros(out_features))
                nn.init.zeros_(self.b)

        self.U = nn.Parameter(torch.eye(in_features))

    def reset_parameters(self):
        if self.r > 0:
            nn.init.kaiming_uniform_(self.A, a=math.sqrt(5))
            nn.init.zeros_(self.B)
        else:
            nn.init.zeros_(self.D)
            if self.bias:
                nn.init.zeros_(self.b)

    def zero_parameters(self):
        if self.r > 0:
            nn.init.zeros_(self.A)
            nn.init.zeros_(self.B)
        else:
            nn.init.zeros_(self.D)
            if self.bias:
                nn.init.zeros_(self.b)

    def randomize(self):
        nn.init.kaiming_uniform_(self.U, a=math.sqrt(5))
        self.qr()

    @torch.no_grad()
    def qr(self):
        Q, R = torch.linalg.qr(self.U)
        self.U.copy_(Q)

    def forward(self, inputs: torch.Tensor):
        if self.r > 0:
            xU = F.linear(inputs, self.U)
            xUW = F.linear(xU, self.B @ self.A)
            xUWUh = F.linear(xUW, self.U.T)
            return xUWUh * self.alpha / self.r
            # return F.linear(inputs, self.U.T @ self.B @ self.A @ self.U) * self.alpha / self.r
            # return F.linear(inputs, self.B @ self.A) * self.alpha / self.r
        else:
            if self.bias:
                xU = F.linear(inputs, self.U)
                xUW = F.linear(xU, self.D)
                xUWUh = F.linear(xUW, self.U.T)
                return xUWUh + self.b
                # return F.linear(inputs, self.U.T @ self.D @ self.U, self.b)
                # return F.linear(inputs, self.D, self.b)
            else:
                xU = F.linear(inputs, self.U)
                xUW = F.linear(xU, self.D)
                xUWUh = F.linear(xUW, self.U.T)
                return xUWUh
                # return F.linear(inputs, self.U.T @ self.D @ self.U)
                # return F.linear(inputs, self.D)

    def __repr__(self):
        return f'LoRALayer(in_features={self.in_features}, out_features={self.out_features}, r={self.r}, alpha={self.alpha})'


class Linear(nn.Module):
    """A wrapper class that implements either a LoRA or standard Linear layer, primarily designed for use in MultiheadAttention"""
    def __init__(
        self,
        in_features: int,
        out_features: int,
        r: int = 0,
        alpha: int = 0,
        weight: torch.Tensor = None,
        bias: torch.Tensor = None,
    ):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.r = r
        self.alpha = alpha

        self.Pre = nn.Linear(in_features, out_features, bias=True if bias is not None else False)
        with torch.no_grad():
            self.Pre.weight.copy_(weight)
            self.Pre.bias.copy_(bias)

        self.Delta = LoRALayer(in_features, out_features, r, alpha)
        self.Delta.reset_parameters()

    def forward(self, inputs: torch.Tensor):
        return self.Pre(inputs) + self.Delta(inputs)
