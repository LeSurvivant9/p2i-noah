# -*- coding: utf-8 -*-
"""
Created on Mon May  5 08:42:25 2025

@author: INSAMC27
"""

import tkinter as tk
from tkinter import scrolledtext, simpledialog
from PIL import Image, ImageTk


class Principal(tk.Tk):
    __slots__ = ["charge_initiale", "vitesse_charge"]

    def __init__(self, parking):
        super().__init__()
        self.title("Parking électrique")
        self.resizable(height=True, width=True)
        self.parking = parking
        # Placement de la boite imaginaire en bas
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, fill="x")
        # PLacement d'une boite imaginaire à gauche
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, fill="y", expand=True)

        # Hauteur et largeur de la fenêtre graphique
        self.maximize_window()

        self.fond()
        self.creer_widget()

        self.pourcentage()
        # exemple de renvoi de données : place, présence, pourcentage, temps restant
        self.pseudo = simpledialog.askstring(
            "Connexion", prompt="Entrez votre nom et votre prénom"
        )

    def creer_widget(self):
        # Boite imaginaire

        # voiture
        self.fond

        # Champ de saisie à gauche du frame
        self.chat = tk.Entry(self.bottom_frame, bd=5, font=("Times New Roman", 14))
        self.chat.pack(side=tk.LEFT, fill="x", expand=True, pady=10, ipady=8)

        # Bouton envoyer à droite dans le frame
        self.envoyer = tk.Button(
            self.bottom_frame, text="Envoyer", font=("Times New Roman", 14), width=41
        )
        self.envoyer.pack(side=tk.RIGHT)
        # action réalisée par le bouton envoyer
        self.envoyer.bind("<Button-1>", self.recuperer_message)
        # envoi du message avec la touche entrée
        self.chat.bind("<Return>", self.recuperer_message)
        # creation de la zone de visualisation du texte
        self.text_area = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, width=50, height=38, font=("Calibri", 12)
        )
        self.text_area.pack(side=tk.RIGHT)

    def fond(self):
        # Chemin vers l'image de fond
        chemin = "assets/background.png"
        image = Image.open(chemin)

        # Adapter l'image à la taille du canvas principal
        image = image.resize(
            (1115, 730), Image.Resampling.LANCZOS
        )  # Ajuste les dimensions de l'image
        self.photo = ImageTk.PhotoImage(image)

        # Canvas principal qui contient l'image de fond ET les voitures
        self.canvas_bg = tk.Canvas(
            self.left_frame, width=1115, height=730
        )  # ajuste les dimensions du canvas
        self.canvas_bg.pack(fill="both", expand=True)

        # Affichage de l'image de fond
        self.canvas_bg.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Création d'une grille virtuelle pour positionner les voitures
        self.canvases = {}
        self.photos = {}

        for index, voiture in enumerate(self.parking):
            place, present, pourcentage, temps = voiture

            # Positions x, y pour chaque voiture
            if place == 1:
                x, y = 150, 130
            elif place == 2:
                x, y = 630, 130
            elif place == 3:
                x, y = 150, 430
            else:  # place == 4
                x, y = 630, 430

            # Créer un canvas pour chaque voiture
            canvas = tk.Canvas(self.canvas_bg, width=300, height=150)
            self.canvases[place] = canvas

            # Placer le canvas sur le canvas principal
            self.canvas_bg.create_window(x, y, window=canvas, anchor=tk.NW)

            # Si la voiture est présente, afficher son image et son label
            if present:
                self.couleur_image(place, pourcentage)

                # Ajouter le label d'information juste à côté
                label = tk.Label(
                    self.left_frame,
                    text=f"Place {place}\nPourcentage : {pourcentage}%\nTemps restant : {temps}s",
                    bg="white",
                    font=("Arial", 10),
                )
                label.place(x=x + 300, y=y + 130)  # Position à côté du canvas

    def maximize_window(self):
        """
        Fonction qui permet d'afficher la fenêtre en plein écran


        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

    def recuperer_message(self, event):
        """
        Fonction qui permet d'afficher le message que l'utilisateur a tapé
        et l'affiche dans le scrolled text


        event : clic gauche ou touche entrée.

        Returns
        -------
        None.

        """
        if self.chat.get():
            self.text_area.configure(state="normal")
            self.text_area.insert(
                tk.INSERT, self.pseudo + " : " + self.chat.get() + "\n"
            )
            self.chat.delete(0, tk.END)
            self.text_area.configure(state="disabled")

    def couleur_image(self, place, pourcentage):
        """
        Affiche l'image correspondante au pourcentage de charge pour une voiture donnée.

        Args:
            place (int): numéro de la place de parking
            pourcentage (int): pourcentage de charge de la voiture
        """
        # Déterminer le chemin de l'image selon le pourcentage
        if 0 < pourcentage <= 25:
            path = "assets/red_car.png"
        elif 26 <= pourcentage <= 50:
            path = "assets/yellow_car.png"
        elif 51 <= pourcentage <= 75:
            path = "assets/green_car.png"
        else:
            path = "assets/blue_car.png"

        # Charger et redimensionner l'image
        image = Image.open(path)
        img_width, img_height = image.size
        canvas_width, canvas_height = 300, 150  # Taille des mini-canvas dans fond()
        scale = min(canvas_width / img_width, canvas_height / img_height)
        new_size = (int(img_width * scale), int(img_height * scale))
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)

        # Convertir pour Tkinter
        photo = ImageTk.PhotoImage(resized_image)

        # Stocker la photo pour éviter que Python la détruise
        self.photos[place] = photo

        # Récupérer le canvas correspondant à la place et y afficher l'image
        canvas = self.canvases[place]
        canvas.create_image(
            canvas_width // 2, canvas_height // 2, image=photo, anchor=tk.CENTER
        )

    def pourcentage(
        self,
    ):
        pass


parking_1 = [
    [1, True, 20, 70],
    [3, True, 90, 50],
    [4, True, 70, 0],
    [2, True, 100, 100],
]


if __name__ == "__main__":
    app = Principal(parking_1)
    app.mainloop()
