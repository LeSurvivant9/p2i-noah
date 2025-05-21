import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

from ImagePath import ImagePath


class Window(tk.Tk):
    def __init__(self, title="Parking électrique", zoomed=True) -> None:
        super().__init__()
        self.title(title)
        self.resizable(height=True, width=True)
        if zoomed:
            self.state("zoomed")

        self.background_image: ImageTk.PhotoImage = self.load_image(
            ImagePath.BACKGROUND
        )
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Lier la touche Escape à la fermeture
        self.bind("<Escape>", lambda e: self.destroy())
        # Bind the resize event to the on_resize method
        self.bind("<Configure>", self.on_resize)

    def load_image(self, image_path: Path) -> ImageTk.PhotoImage:
        """
        Load an image from the specified path.
        :return: Image object or None if the image cannot be loaded.
        """
        width, height = self.get_window_size()
        if width < 1 or height < 1:
            width, height = 100, 100
        black_screen: Image.Image = Image.new("RGB", (width, height), "black")
        image: Image.Image | None = None
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Image not found at {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
        image = (
            image.resize((width, height), Image.Resampling.LANCZOS)
            if image
            else black_screen
        )
        return ImageTk.PhotoImage(image)

    def get_window_size(self) -> tuple[int, int]:
        """
        Get the current size of the window.
        :return: A tuple containing the width and height of the window.
        """
        return max(self.winfo_width(), 1), max(self.winfo_height(), 1)

    def on_resize(self, event):
        # Only update if size actually changed
        if event.width > 1 and event.height > 1:
            self.background_image = self.load_image(ImagePath.BACKGROUND)
            self.background_label.config(image=self.background_image)
            self.background_label.image = self.background_image  # Prevent GC


if __name__ == "__main__":
    window = Window()
    window.mainloop()
