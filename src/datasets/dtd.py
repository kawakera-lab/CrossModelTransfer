import os

import torch
import torchvision
import torchvision.datasets as datasets


class DTD:
    def __init__(
        self,
        preprocess: torchvision.transforms.Compose,
        location: str | os.PathLike = os.path.expanduser("dataset"),
        batch_size: int = 32,
        num_workers: int = 4
    ) -> None:
        # Setup dataset paths
        traindir = os.path.join(location, "dtd", "train")
        valdir = os.path.join(location, "dtd", "val")

        # Setup training data
        self.train_dataset = datasets.ImageFolder(
            traindir,
            transform=preprocess
        )
        self.train_loader = torch.utils.data.DataLoader(
            self.train_dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=num_workers
        )

        # Setup test data
        self.test_dataset = datasets.ImageFolder(
            valdir,
            transform=preprocess
        )
        self.test_loader = torch.utils.data.DataLoader(
            self.test_dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers
        )

        # Setup class names
        idx_to_class = {
            v: k for k, v in self.train_dataset.class_to_idx.items()
        }
        self.classnames = [
            idx_to_class[i].replace("_", " ")
            for i in range(len(idx_to_class))
        ]
