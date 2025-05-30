import random

from PIL import ImageFilter, ImageOps, Image
import torchvision.transforms as transforms


class GrayScale:
    def __init__(self, p: float = 0.2) -> None:
        self.p = p
        self.transf = transforms.Grayscale(3)

    def __call__(self, img: Image) -> Image:
        if random.random() < self.p:
            return self.transf(img)
        return img


class HorizontalFlip:
    def __init__(self, p: float = 0.2, activate_pred: bool = False) -> None:
        self.p = p
        self.transf = transforms.RandomHorizontalFlip(p=1.0)

    def __call__(self, img: Image) -> Image:
        if random.random() < self.p:
            return self.transf(img)
        return img


class Solarization:
    def __init__(self, p: float = 0.2) -> None:
        self.p = p

    def __call__(self, img: Image) -> Image:
        if random.random() < self.p:
            return ImageOps.solarize(img)
        return img


class GaussianBlur:
    def __init__(
            self,
            p: float = 0.1,
            radius_min: float = 0.1,
            radius_max: float = 2.
    ) -> None:
        self.prob = p
        self.radius_min = radius_min
        self.radius_max = radius_max

    def __call__(self, img: Image) -> Image:
        do_it = random.random() <= self.prob
        if not do_it:
            return img

        img = img.filter(
            ImageFilter.GaussianBlur(
                radius=random.uniform(self.radius_min, self.radius_max)
            )
        )
        return img


def get_augmented_preprocess_fn(
        preprocess: transforms,
        p: float = 1.0
) -> transforms:
    """Create a preprocessing function with data augmentation using the given preprocess function."""
    return transforms.Compose([
        preprocess.transforms[0],
        preprocess.transforms[1],
        transforms.RandomHorizontalFlip(),
        transforms.RandomChoice([
            GrayScale(p=p),
            Solarization(p=p),
            GaussianBlur(p=p)
        ]),
        preprocess.transforms[2],
        preprocess.transforms[3]
    ])
