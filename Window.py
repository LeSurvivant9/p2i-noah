import tkinter as tk
from tkinter import scrolledtext, simpledialog

from PIL import Image, ImageTk
import utils
from Car import Car

from ImagePath import ImagePath


class Window(tk.Tk):
    """
    Classe principale de la fenêtre de l'application de gestion de parking électrique.
    Hérite de `tk.Tk` et gère l'interface graphique, l'affichage des voitures, la gestion des messages
    et la configuration de la fenêtre.
    """

    def __init__(self, title="Parking électrique", zoomed=True) -> None:
        """
        Initialise la fenêtre principale, configure les widgets et l'arrière-plan.

        :param title: Titre de la fenêtre.
        :param zoomed: Si True, la fenêtre démarre en mode agrandi.
        """
        self.pseudo: str = (
            simpledialog.askstring(
                "Connexion", prompt="Entrez votre nom et votre prénom"
            )
            or "Anonyme"
        )
        super().__init__()
        self.title(title)
        self.resizable(width=False, height=False)
        if zoomed:
            self.state("zoomed")
        self.input_height: int = self.get_window_size()[1] // 5

        self.background_image: Image.Image = utils.open_image(ImagePath.BACKGROUND)
        self._images: list[ImageTk.PhotoImage] = []
        self._cars: list[Car] = []

        self.output_frame: tk.Frame = tk.Frame(self)
        self.output: scrolledtext.ScrolledText = scrolledtext.ScrolledText(
            self.output_frame, font=("Calibri", 12)
        )
        self.input_frame: tk.Frame = tk.Frame(self)
        self.input: tk.Entry = tk.Entry(
            self.input_frame, font=("Times New Roman", 14), bd=10
        )
        self.send_button: tk.Button = tk.Button(
            self.input_frame,
            text="Envoyer",
            font=("Times New Roman", 14),
            width=15,
            height=2,
        )
        self.initialize_widgets()
        self.bind_keys()

        self.parking_canvas = tk.Canvas(self)
        self.parking_canvas.pack(fill="both", expand=True)

        self.set_background()

    def initialize_widgets(self) -> None:
        """
        Initialise et place les widgets de l'interface graphique (cadres, zones de texte, boutons).
        """
        self.output_frame.pack(side="right", fill="y")
        self.output_frame.pack_propagate(False)
        self.output.pack(fill="both", expand=True, padx=5, pady=5)

        self.input_frame.pack(side="bottom", fill="x")
        self.input_frame.pack_propagate(False)
        self.input.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.send_button.pack(side="right", padx=10, pady=10)

    def display_cars(self) -> None:
        """
        Affiche les voitures présentes sur le parking dans le canvas,
        ainsi que leurs informations (place, pourcentage, temps restant).
        """
        self.parking_canvas.delete("car")
        self.parking_canvas.delete("car_label")
        for car in self._cars:
            x, y = car.get_position()
            if car.is_present:
                self.parking_canvas.create_image(
                    x, y, image=car.photo_image, anchor=tk.NW, tags="car"
                )

                label_text = f"Place {car.place}\nPourcentage : {car.percentage}%\nTemps restant : {car.time_remaining}s"

                label_x = x + 310
                label_y = y + 140

                rect_width = 130
                rect_height = 55

                self.parking_canvas.create_rectangle(
                    label_x - rect_width // 2,
                    label_y - rect_height // 2,
                    label_x + rect_width // 2,
                    label_y + rect_height // 2,
                    fill="white",
                    outline="black",
                    width=1,
                    tags="car_label",
                )

                self.parking_canvas.create_text(
                    label_x,
                    label_y,
                    text=label_text,
                    fill="black",
                    font=("Arial", 10),
                    anchor="center",
                    tags="car_label",
                )

    def bind_keys(self) -> None:
        """
        Lie les événements clavier et souris aux actions correspondantes :
        - Escape pour fermer la fenêtre
        - Redimensionnement pour ajuster l'affichage
        - Entrée ou clic sur le bouton pour envoyer un message
        """
        self.bind("<Escape>", lambda e: self.destroy())
        self.bind("<Configure>", self.on_resize)
        self.input.bind("<Return>", self.get_message)
        self.send_button.bind("<Button-1>", self.get_message)

    def set_background(self) -> None:
        """
        Redimensionne et affiche l'image de fond sur le canvas principal.
        """
        width, height = (
            self.parking_canvas.winfo_width(),
            self.parking_canvas.winfo_height(),
        )
        self._images.clear()
        bg_img = self.background_image.resize((width, height), Image.LANCZOS)  # type: ignore
        bg_photo = ImageTk.PhotoImage(bg_img)
        self.parking_canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
        self._images.append(bg_photo)

    def get_window_size(self) -> tuple[int, int]:
        """
        Retourne la taille actuelle de la fenêtre.

        :return: Un tuple contenant la largeur et la hauteur de la fenêtre.
        """
        return max(self.winfo_width(), 1), max(self.winfo_height(), 1)

    def on_resize(self, event: tk.Event) -> None:
        """
        Gère le redimensionnement de la fenêtre :
        ajuste la taille des cadres et réaffiche l'arrière-plan et les voitures.

        :param event: Événement de redimensionnement.
        """
        w, h = self.get_window_size()
        self.input_frame.config(height=h // 5)
        self.output_frame.config(width=w // 4)
        self.parking_canvas.delete("all")
        self.set_background()
        self.display_cars()

    def get_message(self, event: tk.Event) -> None:
        """
        Récupère le message saisi, l'affiche dans la zone de texte de sortie,
        puis efface le champ de saisie.

        :param event: Événement clavier ou souris déclenchant l'envoi.
        """
        if message := self.input.get().strip():
            self.output.configure(state="normal")
            self.output.tag_configure("pseudo", foreground="blue")
            self.output.insert(tk.END, f"{self.pseudo}", "pseudo")
            self.output.insert(tk.END, f" : {message}\n")
            self.input.delete(0, tk.END)
            self.output.see(tk.END)
            self.output.configure(state="disabled")

    def cars_append(self, car: Car) -> None:
        """
        Ajoute une voiture à la liste et met à jour l'affichage.

        :param car: Instance de la classe Car à ajouter.
        """
        self._cars.append(car)
        self.display_cars()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
