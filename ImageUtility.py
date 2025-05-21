from PIL import Image
from pathlib import Path


class ImageUtility:
    def __init__(self, image_path: Path) -> None:
        self.image_path: Path = image_path
        self.image: Image.Image | None = self.load_image()
