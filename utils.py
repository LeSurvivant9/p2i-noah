import sys

from pathlib import Path
from PIL import Image, UnidentifiedImageError


def open_image(image_path: Path) -> Image.Image:
    """
    Charge une image depuis un chemin pathlib et retourne une ImageTk.PhotoImage.
    Arrête le programme si le fichier est introuvable ou corrompu.

    :param image_path: Chemin vers l'image (format Pathlib.Path)
    :return: ImageTk.PhotoImage
    """
    if not image_path.exists():
        print(f"Erreur : le fichier '{image_path}' n'existe pas.", file=sys.stderr)
        sys.exit(1)

    try:
        return Image.open(image_path)
    except UnidentifiedImageError:
        print(
            f"Erreur : le fichier '{image_path}' n'est pas une image valide ou est corrompu.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(
            f"Erreur inattendue lors du chargement de l'image : {e}",
            file=sys.stderr,
        )
        sys.exit(1)
