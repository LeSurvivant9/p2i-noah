import tkinter as tk
from tkinter import scrolledtext

from PIL import Image, ImageTk
import utils
from Car import Car

from ImagePath import ImagePath
import sys


class Window(tk.Tk):
    def __init__(self, title="Parking électrique", zoomed=True) -> None:
        super().__init__()
        self.title(title)
        # self.resizable(height=True, width=True)
        if zoomed:
            self.state("zoomed")
        self.input_height: int = self.get_window_size()[1] // 5  # 20% of the window height

        # Store references to images to prevent garbage collection
        self._images: list[ImageTk.PhotoImage] = []
        self.cars: list[Car] = []

        # Output area (right, 20% width)
        self.output = scrolledtext.ScrolledText(self, font=("Calibri", 12))
        self.output.place(relx=0.8, rely=0, relwidth=0.8, relheight=0.2)
        self.output.config(state="disabled")

        # Input area (bottom left, 80% width)
        self.input = tk.Entry(self, font=("Times New Roman", 14))
        self.input.place(relx=0, rely=1.0, anchor='sw', relwidth=0.2, relheight=1.0)

        # Parking area (top left, 80% width, height minus input)
        self.parking_canvas = tk.Canvas(self, bg="gray")
        self.parking_canvas.place(relx=0, rely=0, relwidth=0.8, height=self.winfo_height()-self.input_height)

        self.background_image: Image.Image = utils.open_image(ImagePath.BACKGROUND)
        self.set_background()

        # Lier la touche Escape à la fermeture
        self.bind("<Escape>", lambda e: self.destroy())
        # Bind the resize event to the on_resize method
        self.bind("<Configure>", self.on_resize)

    def set_background(self) -> None:
        width, height = self.parking_canvas.winfo_width(), self.parking_canvas.winfo_height()
        bg_img = self.background_image.resize((width, height), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_img)
        self.parking_canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
        self._images.append(bg_photo)

    def get_window_size(self) -> tuple[int, int]:
        """
        Get the current size of the window.
        :return: A tuple containing the width and height of the window.
        """
        return max(self.winfo_width(), 1), max(self.winfo_height(), 1)

    def on_resize(self, event: tk.Event) -> None:
        h = self.get_window_size()[1]
        self.output.place(relx=0.8, rely=0, relwidth=0.2, relheight=1.0)
        self.input.place(relx=0, rely=1.0, anchor='sw', relwidth=0.8, relheight=0.2)
        self.parking_canvas.place(relx=0, rely=0, relwidth=0.8, height=h-self.input_height)
        self.set_background()
        for car in self.cars:
            self.parking_canvas.create_image(car.x, car.y, image=car.photo_image, anchor=tk.NW)

    def display_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            print(
                "Erreur : l'objet passé n'est pas une instance de Car.", file=sys.stderr
            )
            return
        self.cars.append(car)
        self.parking_canvas.create_image(car.x, car.y, image=car.photo_image, anchor=tk.NW)
        self._images.append(car.photo_image)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
