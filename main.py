from Window import Window


class Main:
    def __init__(self) -> None:
        self.window: Window = Window()
        self.window.set_background(self.background_image.image)

    def run(self) -> None:
        self.window.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()
