from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImagePath:
    """
    Classe contenant les chemins vers les images utilisées dans l'application.

    Attributs :
        BACKGROUND (Path) : Chemin de l'image d'arrière-plan.
        BLUE_CAR (Path) : Chemin de l'image de la voiture bleue (batterie pleine).
        GREEN_CAR (Path) : Chemin de l'image de la voiture verte (batterie bien chargée).
        RED_CAR (Path) : Chemin de l'image de la voiture rouge (batterie faible).
        YELLOW_CAR (Path) : Chemin de l'image de la voiture jaune (batterie moyenne).
    """

    BACKGROUND: Path = Path("assets/background.png")
    BLUE_CAR: Path = Path("assets/blue_car.png")
    GREEN_CAR: Path = Path("assets/green_car.png")
    RED_CAR: Path = Path("assets/red_car.png")
    YELLOW_CAR: Path = Path("assets/yellow_car.png")
