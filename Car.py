from pathlib import Path
from PIL import Image, ImageTk
import utils


class Car:
    def __init__(
        self, image_path: Path, x: int, y: int, width: int, height: int
    ) -> None:
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.image_path: Path = image_path
        self.image: Image.Image = utils.open_image(self.image_path)
        self.image = self.image.resize((self.width, self.height), Image.LANCZOS)
        self.photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(self.image)

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height
