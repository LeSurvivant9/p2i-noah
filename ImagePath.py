from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImagePath:
    """
    A class to represent an image path.

    Attributes:
        path (Path): The path to the image file.
    """

    BACKGROUND: Path = Path("assets/place de parking 3 bataille.png")
    BLUE_CAR: Path = Path("assets/dessin de voiture bleu du dessus horizontale.png")
    YELLOW_CAR: Path = Path(
        "assets/dessin de voiture bleu du dessus jaune copie bien rognée bien soignée.png"
    )
    RED_CAR: Path = Path(
        "assets/dessin de voiture bleu du dessus rouge horizontale.png"
    )
    GREEN_CAR: Path = Path(
        "assets/dessin de voiture bleu du dessus vert horizontale.png"
    )
