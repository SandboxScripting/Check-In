# Part of this file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import *
from MainPage import *
from AccNoWaiver import *
from AccNoWaiverSwipe import *
import time
import global_


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/user_thank_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class UserThank(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.photoList = []
        self.loadWidgets(controller)

    def loadWidgets(self, controller):
        self.canvas = Canvas(
            self,
            bg="#153244",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))

        self.photoList.append(image_image_1)

        image_1 = self.canvas.create_image(640.0, 360.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))

        self.photoList.append(image_image_2)

        image_2 = self.canvas.create_image(
            639.33203125, 359.333984375, image=image_image_2
        )

        self.canvas.create_text(
            99.33203125,
            259.33203125,
            anchor="nw",
            text="Thank you for registering",
            fill="#F5F0E6",
            font=("Montserrat", 45 * -1),
        )

        self.canvas.create_text(
            429.0,
            550.0,
            anchor="nw",
            text="UCSD Makerspace",
            fill="#F5F0E6",
            font=("Montserrat", 45 * -1),
        )

    def displayName(self, name, nextPage):
        u_name = self.canvas.create_text(
            99.0,
            323.0,
            anchor="nw",
            text=name,
            fill="#F5F0E6",
            font=("Montserrat", 73 * -1),
            tag="thank",
        )

        time.sleep(0.500)

        global_.app.show_frame(UserThank)

        self.canvas.after(5000, lambda: self.canvas.delete("thank"))
        global_.app.after(4000, lambda: global_.app.show_frame(nextPage))
