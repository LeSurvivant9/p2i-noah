from pathlib import Path
from PIL import Image, ImageTk
import utils


class Car:
    def __init__(
        self, place: int, is_present: bool, percentage: int, time_remaining: int
    ) -> None:
        self._place: int = place
        self._is_present: bool = is_present
        self._percentage: int = percentage
        self._time_remaining: int = time_remaining
        self.image_path: Path = self.get_image_path()
        self.image: Image.Image = utils.open_image(self.image_path)
        self.initialize_image()
        self.photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(self.image)

    def get_image_path(self) -> Path:
        p = self._percentage
        if 0 < p <= 25:
            return Path("assets/red_car.png")
        elif 26 <= p <= 50:
            return Path("assets/yellow_car.png")
        elif 51 <= p <= 75:
            return Path("assets/green_car.png")
        else:
            return Path("assets/blue_car.png")

    def initialize_image(self) -> None:
        width, height = self.image.size
        scale: float = min(300 / width, 150 / height)
        width, height = (
            int(width * scale),
            int(height * scale),
        )
        self.image = self.image.resize((width, height), Image.LANCZOS)  # type: ignore

    def get_position(self) -> tuple[int, int]:
        positions = {
            1: (250, 170),
            2: (870, 170),
            3: (250, 540),
            4: (870, 540),
        }
        return positions.get(self._place, (0, 0))

    @property
    def place(self) -> int:
        return self._place

    @place.setter
    def place(self, value: int) -> None:
        if value > 0:
            self._place = value
        else:
            raise ValueError("Place must be a positive integer.")

    @property
    def is_present(self) -> bool:
        return self._is_present

    @is_present.setter
    def is_present(self, value: bool) -> None:
        self._is_present = value

    @property
    def percentage(self) -> int:
        return self._percentage

    @percentage.setter
    def percentage(self, value: int) -> None:
        if 0 <= value <= 100:
            self._percentage = value
        else:
            raise ValueError("Percentage must be between 0 and 100.")

    @property
    def time_remaining(self) -> int:
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, value: int) -> None:
        if value >= 0:
            self._time_remaining = value
        else:
            raise ValueError("Time remaining must be non-negative.")
