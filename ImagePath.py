from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImagePath:
    BACKGROUND: Path = Path("assets/background.png")
    BLUE_CAR: Path = Path("assets/blue_car.png")
    GREEN_CAR: Path = Path("assets/green_car.png")
    RED_CAR: Path = Path("assets/red_car.png")
    YELLOW_CAR: Path = Path("assets/yellow_car.png")
