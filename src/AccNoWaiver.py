# Part of this file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/acc_no_waiver_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AccNoWaiver(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.photoList = []
        self.loadWidgets(controller)

    def loadWidgets(self, controller):
        canvas = Canvas(
            self,
            bg="#153244",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))

        self.photoList.append(image_image_1)

        image_1 = canvas.create_image(640.0, 360.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))

        self.photoList.append(image_image_2)

        image_2 = canvas.create_image(639.333984375, 359.333984375, image=image_image_2)

        canvas.create_text(
            169.0,
            258.0,
            anchor="nw",
            text="Looks like you haven’t signed\n  the waiver, let’s solve that",
            fill="#F5F0E6",
            font=("Montserrat", 64 * -1),
        )
