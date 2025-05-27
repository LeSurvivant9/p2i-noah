from Window import Window
from Car import Car


class Main:
    """
    Classe principale de l'application de gestion du parking électrique.
    Gère la création de la fenêtre principale, l'initialisation des voitures et le lancement de la boucle principale.
    """

    def __init__(self) -> None:
        """
        Initialise la fenêtre principale et les voitures du parking, puis affiche les voitures.
        """
        self.window: Window = Window()
        self.initialize_cars()
        self.window.display_cars()

    def initialize_cars(self) -> None:
        """
        Crée et ajoute les voitures à la fenêtre principale avec leurs paramètres respectifs.
        """
        car_1: Car = Car(place=1, is_present=True, percentage=20, time_remaining=70)
        car_2: Car = Car(place=2, is_present=True, percentage=100, time_remaining=100)
        car_3: Car = Car(place=3, is_present=True, percentage=90, time_remaining=50)
        car_4: Car = Car(place=4, is_present=True, percentage=70, time_remaining=0)

        self.window.cars_append(car_1)
        self.window.cars_append(car_2)
        self.window.cars_append(car_3)
        self.window.cars_append(car_4)

    def run(self) -> None:
        """
        Démarre la boucle principale de l'interface graphique.
        """
        self.window.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()
