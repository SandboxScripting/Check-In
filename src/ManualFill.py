
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from sheets import *
from reader import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\manual_fill_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ManualFill(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.photoList = []
        self.entryList = []
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.pid = StringVar()
        
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

        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        
        self.photoList.append(image_image_6)
        
        image_6 = canvas.create_image(
            640.0,
            542.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        
        self.photoList.append(image_image_7)
        
        image_7 = canvas.create_image(
            640.0,
            440.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        
        self.photoList.append(image_image_8)    
        
        image_8 = canvas.create_image(
            640.0,
            339.0,
            image=image_image_8
        )  

        image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        
        self.photoList.append(image_image_9)
        
        image_9 = canvas.create_image(
            640.0,
            239.0,
            image=image_image_9
        ) 

        canvas.create_text(
            565.0,
            177.0,
            anchor="nw",
            text="First Name",
            fill="#F5F0E6",
            font=("Montserrat", 24 * -1)
        )

        canvas.create_text(
            565.0,
            278.0,
            anchor="nw",
            text="Last Name",
            fill="#F5F0E6",
            font=("Montserrat", 24 * -1)
        )

        canvas.create_text(
            595.0,
            379.0,
            anchor="nw",
            text="Email",
            fill="#F5F0E6",
            font=("Montserrat", 24 * -1)
        )

        canvas.create_text(
            605.0,
            480.0,
            anchor="nw",
            text="PID",
            fill="#F5F0E6",
            font=("Montserrat", 24 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        
        self.photoList.append(button_image_1)
        
        self.button_1 = Button(
            self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.createAccount(),
            relief="flat"
        )
        self.button_1.place(
            x=465.0,
            y=598.0,
            width=349.0,
            height=71.0
        )
        
        first_name_entry=Entry(
            self,
            textvariable=self.first_name,
            width=40,
            font=48
        )
        
        first_name_entry.place(
            x=420.0,
            y=227.0
        )   
        
        last_name_entry=Entry(
            self,
            textvariable=self.last_name,
            width=40,
            font=48
        )
        
        last_name_entry.place(
            x=420.0,
            y=327.0
        )  
        
        email_entry=Entry(
            self,
            textvariable=self.email,
            width=40,
            font=48
        )
        
        email_entry.place(
            x=420.0,
            y=428.0
        )
        
        pid_entry=Entry(
            self,
            textvariable=self.pid,
            width=40,
            font=48
        )
        
        pid_entry.place(
            x=420.0,
            y=530.0
        )
    
    def getEntries(self):
        del self.entryList[:]
        self.entryList.append(self.first_name.get())
        self.entryList.append(self.last_name.get())
        self.entryList.append(self.email.get())
        self.entryList.append(self.pid.get())
        return self.entryList
         
    def clearEntries(self):
        self.first_name.delete(0, END)
        self.last_name.delete(0, END)
        self.email.delete(0, END)
        self.pid.delete(0, END)
        
    def updateEntries(self, fn, ln, e, p):
        self.first_name.insert(0, fn)
        self.last_name.insert(0, ln)
        self.email.insert(0, e)
        self.pid.insert(0, p)
    
    def createAccount(self):
        from UserThank import UserThank
        data = self.getEntries()
        sheets.createAccount(data[0], data[1], data[2], data[3], Reader.getRFID())