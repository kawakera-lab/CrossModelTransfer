from typing import Callable, Dict, List


# Templates for car image dataset
cars_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of a {c}.",
    lambda c: f"a photo of the {c}.",
    lambda c: f"a photo of my {c}.",
    lambda c: f"i love my {c}!",
    lambda c: f"a photo of my dirty {c}.",
    lambda c: f"a photo of my clean {c}.",
    lambda c: f"a photo of my new {c}.",
    lambda c: f"a photo of my old {c}.",
]

# Templates for CIFAR-10 dataset
cifar10_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of a {c}.",
    lambda c: f"a blurry photo of a {c}.",
    lambda c: f"a black and white photo of a {c}.",
    lambda c: f"a low contrast photo of a {c}.",
    lambda c: f"a high contrast photo of a {c}.",
    lambda c: f"a bad photo of a {c}.",
    lambda c: f"a good photo of a {c}.",
    lambda c: f"a photo of a small {c}.",
    lambda c: f"a photo of a big {c}.",
    lambda c: f"a photo of the {c}.",
    lambda c: f"a blurry photo of the {c}.",
    lambda c: f"a black and white photo of the {c}.",
    lambda c: f"a low contrast photo of the {c}.",
    lambda c: f"a high contrast photo of the {c}.",
    lambda c: f"a bad photo of the {c}.",
    lambda c: f"a good photo of the {c}.",
    lambda c: f"a photo of the small {c}.",
    lambda c: f"a photo of the big {c}.",
]

# Templates for CIFAR-100 dataset
cifar100_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of a {c}.",
    lambda c: f"a blurry photo of a {c}.",
    lambda c: f"a black and white photo of a {c}.",
    lambda c: f"a low contrast photo of a {c}.",
    lambda c: f"a high contrast photo of a {c}.",
    lambda c: f"a bad photo of a {c}.",
    lambda c: f"a good photo of a {c}.",
    lambda c: f"a photo of a small {c}.",
    lambda c: f"a photo of a big {c}.",
    lambda c: f"a photo of the {c}.",
    lambda c: f"a blurry photo of the {c}.",
    lambda c: f"a black and white photo of the {c}.",
    lambda c: f"a low contrast photo of the {c}.",
    lambda c: f"a high contrast photo of the {c}.",
    lambda c: f"a bad photo of the {c}.",
    lambda c: f"a good photo of the {c}.",
    lambda c: f"a photo of the small {c}.",
    lambda c: f"a photo of the big {c}.",
]

# Templates for Describable Textures Dataset
dtd_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of a {c} texture.",
    lambda c: f"a photo of a {c} pattern.",
    lambda c: f"a photo of a {c} thing.",
    lambda c: f"a photo of a {c} object.",
    lambda c: f"a photo of the {c} texture.",
    lambda c: f"a photo of the {c} pattern.",
    lambda c: f"a photo of the {c} thing.",
    lambda c: f"a photo of the {c} object.",
]

# Templates for EuroSAT satellite imagery dataset
eurosat_template: List[Callable[[str], str]] = [
    lambda c: f"a centered satellite photo of {c}.",
    lambda c: f"a centered satellite photo of a {c}.",
    lambda c: f"a centered satellite photo of the {c}.",
]

# Templates for Food-101 dataset
food101_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of {c}, a type of food.",
]

# Templates for German Traffic Sign Recognition Benchmark
gtsrb_template: List[Callable[[str], str]] = [
    lambda c: f"a zoomed in photo of a '{c}' traffic sign.",
    lambda c: f"a centered photo of a '{c}' traffic sign.",
    lambda c: f"a close up photo of a '{c}' traffic sign.",
]

# Templates for MNIST handwritten digits dataset
mnist_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of the number: '{c}'.",
]

# Templates for ImageNet dataset
imagenet_template: List[Callable[[str], str]] = [
    lambda c: f"a bad photo of a {c}.",
    lambda c: f"a photo of many {c}.",
    lambda c: f"a sculpture of a {c}.",
    lambda c: f"a photo of the hard to see {c}.",
    lambda c: f"a low resolution photo of the {c}.",
    lambda c: f"a rendering of a {c}.",
    lambda c: f"graffiti of a {c}.",
    lambda c: f"a bad photo of the {c}.",
    lambda c: f"a cropped photo of the {c}.",
    lambda c: f"a tattoo of a {c}.",
    lambda c: f"the embroidered {c}.",
    lambda c: f"a photo of a hard to see {c}.",
    lambda c: f"a bright photo of a {c}.",
    lambda c: f"a photo of a clean {c}.",
    lambda c: f"a photo of a dirty {c}.",
    lambda c: f"a dark photo of the {c}.",
    lambda c: f"a drawing of a {c}.",
    lambda c: f"a photo of my {c}.",
    lambda c: f"the plastic {c}.",
    lambda c: f"a photo of the cool {c}.",
    lambda c: f"a close-up photo of a {c}.",
    lambda c: f"a black and white photo of the {c}.",
    lambda c: f"a painting of the {c}.",
    lambda c: f"a painting of a {c}.",
    lambda c: f"a pixelated photo of the {c}.",
    lambda c: f"a sculpture of the {c}.",
    lambda c: f"a bright photo of the {c}.",
    lambda c: f"a cropped photo of a {c}.",
    lambda c: f"a plastic {c}.",
    lambda c: f"a photo of the dirty {c}.",
    lambda c: f"a jpeg corrupted photo of a {c}.",
    lambda c: f"a blurry photo of the {c}.",
    lambda c: f"a photo of the {c}.",
    lambda c: f"a good photo of the {c}.",
    lambda c: f"a rendering of the {c}.",
    lambda c: f"a {c} in a video game.",
    lambda c: f"a photo of one {c}.",
    lambda c: f"a doodle of a {c}.",
    lambda c: f"a close-up photo of the {c}.",
    lambda c: f"a photo of a {c}.",
    lambda c: f"the origami {c}.",
    lambda c: f"the {c} in a video game.",
    lambda c: f"a sketch of a {c}.",
    lambda c: f"a doodle of the {c}.",
    lambda c: f"a origami {c}.",
    lambda c: f"a low resolution photo of a {c}.",
    lambda c: f"the toy {c}.",
    lambda c: f"a rendition of the {c}.",
    lambda c: f"a photo of the clean {c}.",
    lambda c: f"a photo of a large {c}.",
    lambda c: f"a rendition of a {c}.",
    lambda c: f"a photo of a nice {c}.",
    lambda c: f"a photo of a weird {c}.",
    lambda c: f"a blurry photo of a {c}.",
    lambda c: f"a cartoon {c}.",
    lambda c: f"art of a {c}.",
    lambda c: f"a sketch of the {c}.",
    lambda c: f"a embroidered {c}.",
    lambda c: f"a pixelated photo of a {c}.",
    lambda c: f"itap of the {c}.",
    lambda c: f"a jpeg corrupted photo of the {c}.",
    lambda c: f"a good photo of a {c}.",
    lambda c: f"a plushie {c}.",
    lambda c: f"a photo of the nice {c}.",
    lambda c: f"a photo of the small {c}.",
    lambda c: f"a photo of the weird {c}.",
    lambda c: f"the cartoon {c}.",
    lambda c: f"art of the {c}.",
    lambda c: f"a drawing of the {c}.",
    lambda c: f"a photo of the large {c}.",
    lambda c: f"a black and white photo of a {c}.",
    lambda c: f"the plushie {c}.",
    lambda c: f"a dark photo of a {c}.",
    lambda c: f"itap of a {c}.",
    lambda c: f"graffiti of the {c}.",
    lambda c: f"a toy {c}.",
    lambda c: f"itap of my {c}.",
    lambda c: f"a photo of a cool {c}.",
    lambda c: f"a photo of a small {c}.",
    lambda c: f"a tattoo of the {c}.",
]

# Templates for RESISC45 remote sensing dataset
resisc45_template: List[Callable[[str], str]] = [
    lambda c: f"satellite imagery of {c}.",
    lambda c: f"aerial imagery of {c}.",
    lambda c: f"satellite photo of {c}.",
    lambda c: f"aerial photo of {c}.",
    lambda c: f"satellite view of {c}.",
    lambda c: f"aerial view of {c}.",
    lambda c: f"satellite imagery of a {c}.",
    lambda c: f"aerial imagery of a {c}.",
    lambda c: f"satellite photo of a {c}.",
    lambda c: f"aerial photo of a {c}.",
    lambda c: f"satellite view of a {c}.",
    lambda c: f"aerial view of a {c}.",
    lambda c: f"satellite imagery of the {c}.",
    lambda c: f"aerial imagery of the {c}.",
    lambda c: f"satellite photo of the {c}.",
    lambda c: f"aerial photo of the {c}.",
    lambda c: f"satellite view of the {c}.",
    lambda c: f"aerial view of the {c}.",
]

# Templates for STL-10 dataset
stl10_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of a {c}.",
    lambda c: f"a photo of the {c}.",
]

# Templates for SUN397 scene dataset
sun397_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of a {c}.",
    lambda c: f"a photo of the {c}.",
]

# Templates for Street View House Numbers dataset
svhn_template: List[Callable[[str], str]] = [
    lambda c: f"a photo of the number: '{c}'.",
]

# Mapping from dataset names to their templates
dataset_to_template: Dict[str, List[Callable[[str], str]]] = {
    "Cars": cars_template,
    "CIFAR10": cifar10_template,
    "CIFAR100": cifar100_template,
    "DTD": dtd_template,
    "EuroSAT": eurosat_template,
    "Food101": food101_template,
    "GTSRB": gtsrb_template,
    "MNIST": mnist_template,
    "ImageNet": imagenet_template,
    "RESISC45": resisc45_template,
    "STL10": stl10_template,
    "SUN397": sun397_template,
    "SVHN": svhn_template,
}


def get_templates(dataset_name: str) -> List[Callable[[str], str]]:
    if dataset_name.endswith("Val"):
        return get_templates(dataset_name.replace("Val", ""))
    assert dataset_name in dataset_to_template, f"Unsupported dataset: {dataset_name}"
    return dataset_to_template[dataset_name]
