from pathlib import Path
from PIL import Image, ImageTk
import utils


class Car:
    """
    Classe représentant une voiture sur le parking électrique.

    Attributs :
        _place (int) : Numéro de la place de parking.
        _is_present (bool) : Indique si la voiture est présente sur le parking.
        _percentage (int) : Pourcentage de charge de la voiture.
        _time_remaining (int) : Temps restant de charge (en secondes).
        image_path (Path) : Chemin de l'image correspondant à l'état de charge.
        image (Image.Image) : Image PIL de la voiture.
        photo_image (ImageTk.PhotoImage) : Image adaptée pour affichage Tkinter.
    """

    def __init__(
        self, place: int, is_present: bool, percentage: int, time_remaining: int
    ) -> None:
        """
        Initialise une instance de Car avec ses attributs principaux et charge l'image correspondante.

        :param place: Numéro de la place de parking.
        :param is_present: Présence de la voiture sur le parking.
        :param percentage: Pourcentage de charge de la voiture.
        :param time_remaining: Temps restant de charge (en secondes).
        """
        self._place: int = place
        self._is_present: bool = is_present
        self._percentage: int = percentage
        self._time_remaining: int = time_remaining
        self.image_path: Path = self.get_image_path()
        self.image: Image.Image = utils.open_image(self.image_path)
        self.initialize_image()
        self.photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(self.image)

    def get_image_path(self) -> Path:
        """
        Retourne le chemin de l'image à utiliser selon le pourcentage de charge.

        :return: Chemin de l'image correspondant à l'état de charge.
        """
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
        """
        Redimensionne l'image de la voiture pour l'adapter à l'affichage sur le parking.
        """
        width, height = self.image.size
        scale: float = min(300 / width, 150 / height)
        width, height = (
            int(width * scale),
            int(height * scale),
        )
        self.image = self.image.resize((width, height), Image.LANCZOS)  # type: ignore

    def get_position(self) -> tuple[int, int]:
        """
        Retourne la position (x, y) de la voiture sur le parking selon sa place.

        :return: Tuple des coordonnées (x, y) sur le canvas.
        """
        positions = {
            1: (250, 170),
            2: (870, 170),
            3: (250, 540),
            4: (870, 540),
        }
        return positions.get(self._place, (0, 0))

    @property
    def place(self) -> int:
        """
        Accesseur pour le numéro de place de la voiture.

        :return: Numéro de la place.
        """
        return self._place

    @place.setter
    def place(self, value: int) -> None:
        """
        Mutateur pour le numéro de place. Doit être un entier positif.

        :param value: Nouveau numéro de place.
        :raises ValueError: Si la valeur n'est pas positive.
        """
        if value > 0:
            self._place = value
        else:
            raise ValueError("Place must be a positive integer.")

    @property
    def is_present(self) -> bool:
        """
        Accesseur pour la présence de la voiture sur le parking.

        :return: True si la voiture est présente, False sinon.
        """
        return self._is_present

    @is_present.setter
    def is_present(self, value: bool) -> None:
        """
        Mutateur pour la présence de la voiture.

        :param value: Booléen indiquant la présence.
        """
        self._is_present = value

    @property
    def percentage(self) -> int:
        """
        Accesseur pour le pourcentage de charge de la voiture.

        :return: Pourcentage de charge.
        """
        return self._percentage

    @percentage.setter
    def percentage(self, value: int) -> None:
        """
        Mutateur pour le pourcentage de charge. Doit être entre 0 et 100.

        :param value: Nouveau pourcentage de charge.
        :raises ValueError: Si la valeur n'est pas comprise entre 0 et 100.
        """
        if 0 <= value <= 100:
            self._percentage = value
        else:
            raise ValueError("Percentage must be between 0 and 100.")

    @property
    def time_remaining(self) -> int:
        """
        Accesseur pour le temps restant de charge.

        :return: Temps restant en secondes.
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, value: int) -> None:
        """
        Mutateur pour le temps restant de charge. Doit être non négatif.

        :param value: Nouveau temps restant (en secondes).
        :raises ValueError: Si la valeur est négative.
        """
        if value >= 0:
            self._time_remaining = value
        else:
            raise ValueError("Time remaining must be non-negative.")
