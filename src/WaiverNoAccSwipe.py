
# Part of this file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\logan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\build\assets\frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class WaiverNoAccSwipe(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.photoList = []
        self.loadWidgets()
        
    def loadWidgets(self):  
        canvas = Canvas(
            self,
            bg = "#153246",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        
        self.photoList.append(image_image_1)

        image_1 = canvas.create_image(
            640.0,
            360.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        
        self.photoList.append(image_image_2)
        
        image_2 = canvas.create_image(
            640.0,
            76.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        
        self.photoList.append(image_image_3)
        
        image_3 = canvas.create_image(
            640.0,
            430.0,
            image=image_image_3
        )

        canvas.create_text(
            236.0,
            207.0,
            anchor="nw",
            text="Please swipe your ID where the\nswipe sign is located or fill your\ninformation manually by tapping\nthe screen",
            fill="#F5F0E6",
            font=("Montserrat", 48 * -1)
        )

        canvas.create_text(
            371.0,
            45.0,
            anchor="nw",
            text="Account",
            fill="#F5F0E6",
            font=("Montserrat", 40 * -1)
        )

        canvas.create_text(
            701.0,
            45.0,
            anchor="nw",
            text="Waiver",
            fill="#F5F0E6",
            font=("Montserrat", 40 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        
        self.photoList.append(image_image_4)
        
        image_4 = canvas.create_image(
            585.0,
            77.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        
        self.photoList.append(image_image_5)
        
        image_5 = canvas.create_image(
            884.0,
            77.0,
            image=image_image_5
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        
        self.photoList.append(button_image_1)
        
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=465.0,
            y=554.0,
            width=349.0,
            height=71.0
        )