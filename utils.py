import sys

from pathlib import Path
from PIL import Image, UnidentifiedImageError


def open_image(image_path: Path) -> Image.Image:
    """
    Ouvre une image à partir du chemin spécifié et la retourne sous forme d'objet PIL Image.

    :param path: Chemin du fichier image à ouvrir.
    :return: Image ouverte sous forme d'objet PIL Image.
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
