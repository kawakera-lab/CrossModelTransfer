import copy
import inspect
import sys
from typing import Any, Dict, Optional, Tuple, Type

import torch
from torch.utils.data import Dataset, DataLoader, random_split

from .cars import Cars
from .cifar10 import CIFAR10
from .cifar100 import CIFAR100
from .dtd import DTD
from .eurosat import EuroSAT, EuroSATVal
from .gtsrb import GTSRB
from .imagenet import ImageNet
from .mnist import MNIST
from .resisc45 import RESISC45
from .stl10 import STL10
from .svhn import SVHN
from .sun397 import SUN397


# Register all classes in the module
registry: Dict[str, Type[Any]] = {
    name: obj for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass)
}


class GenericDataset:
    def __init__(self) -> None:
        self.train_dataset: Optional[Dataset] = None
        self.train_loader: Optional[DataLoader] = None
        self.test_dataset: Optional[Dataset] = None
        self.test_loader: Optional[DataLoader] = None
        self.classnames: Optional[list] = None


def split_train_into_train_val(
    dataset: GenericDataset,
    new_dataset_class_name: str,
    batch_size: int,
    num_workers: int,
    val_fraction: float,
    max_val_samples: Optional[int] = None,
    seed: int = 0
) -> GenericDataset:
    assert 0.0 < val_fraction < 1.0, "val_fraction must be between 0 and 1"

    # Calculate dataset sizes
    total_size = len(dataset.train_dataset)
    val_size = int(total_size * val_fraction)
    if max_val_samples is not None:
        val_size = min(val_size, max_val_samples)
    train_size = total_size - val_size

    assert val_size > 0 and train_size > 0, "Split results in empty dataset"

    # Split the dataset
    trainset, valset = random_split(
        dataset.train_dataset,
        [train_size, val_size],
        generator=torch.Generator().manual_seed(seed)
    )

    # Verify split for MNISTVal
    if new_dataset_class_name == "MNISTVal":
        assert trainset.indices[0] == 36044

    # Create and configure new dataset class
    new_dataset_class = type(new_dataset_class_name, (GenericDataset,), {})
    new_dataset = new_dataset_class()

    # Configure training data loader
    new_dataset.train_dataset = trainset
    new_dataset.train_loader = DataLoader(
        new_dataset.train_dataset,
        shuffle=True,
        batch_size=batch_size,
        num_workers=num_workers,
    )

    # Configure validation data loader
    new_dataset.test_dataset = valset
    new_dataset.test_loader = DataLoader(
        new_dataset.test_dataset,
        batch_size=batch_size,
        num_workers=num_workers
    )

    new_dataset.classnames = copy.copy(dataset.classnames)

    return new_dataset


def get_dataset(
    dataset_name: str,
    preprocess: Any,
    location: str,
    batch_size: int = 32,
    num_workers: int = 4,
    val_fraction: float = 0.1,
    max_val_samples: int = 5000
) -> GenericDataset:
    """Get dataset wrapper from dataset_name"""
    if dataset_name.endswith("Val"):
        # Handle validation datasets
        if dataset_name in registry:
            dataset_class = registry[dataset_name]
        else:
            # Create validation dataset from base dataset
            base_dataset_name = dataset_name.split("Val")[0]
            base_dataset = get_dataset(
                base_dataset_name,
                preprocess,
                location,
                batch_size,
                num_workers
            )
            dataset = split_train_into_train_val(
                base_dataset,
                dataset_name,
                batch_size,
                num_workers,
                val_fraction,
                max_val_samples
            )
            return dataset
    else:
        assert dataset_name in registry, (
            f"Unsupported dataset: {dataset_name}. "
            f"Available datasets: {list(registry.keys())}"
        )
        dataset_class = registry[dataset_name]

    # Create dataset instance
    dataset = dataset_class(
        preprocess,
        location=location,
        batch_size=batch_size,
        num_workers=num_workers
    )
    return dataset
