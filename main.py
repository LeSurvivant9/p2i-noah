from Window import Window
from ImagePath import ImagePath
from Car import Car


class Main:
    def __init__(self) -> None:
        self.window: Window = Window()
        self.cars: list[Car] = []
        self.initialize_cars()

        for car in self.cars:
            self.window.display_car(car)

    def initialize_cars(self) -> None:
        blue_car: Car = Car(
            image_path=ImagePath.BLUE_CAR, x=200, y=130, width=300, height=150
        )
        green_car: Car = Car(
            image_path=ImagePath.GREEN_CAR, x=200, y=460, width=300, height=150
        )
        red_car: Car = Car(
            image_path=ImagePath.RED_CAR, x=730, y=130, width=300, height=150
        )
        yellow_car: Car = Car(
            image_path=ImagePath.YELLOW_CAR, x=730, y=460, width=300, height=150
        )

        self.cars.append(red_car)
        self.cars.append(blue_car)
        self.cars.append(green_car)
        self.cars.append(yellow_car)

    def run(self) -> None:
        self.window.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()
