from tkinter import *
from tkinter import ttk
from train import Train
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Attendance Management System Using Face Recognition")

        # ----------------------------- Header Image -----------------------------
        img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner.jpg")
        img = img.resize((1250, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        header_label = Label(self.root, image=self.photoimg)
        header_label.place(x=0, y=0, width=1250, height=120)

        # ----------------------------- Background Image -----------------------------
        bg1 = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1250, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1250, height=768)

        # ----------------------------- Title -----------------------------
        title_label = Label(bg_img, text="Developer", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_label.place(x=0, y=0, width=1366, height=45)

        # ----------------------------- Developer Profile -----------------------------
        dev_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\sk.jpg")
        dev_img = dev_img.resize((180, 180), Image.Resampling.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(dev_img)

        dev_btn_image = Button(bg_img, image=self.att_img1, cursor="hand2")
        dev_btn_image.place(x=550, y=180, width=180, height=200)

        dev_btn_name = Button(bg_img, text="Sujit Balu Kokate", cursor="hand2", font=("tahoma", 10, "bold"), bg="white", fg="navyblue")
        dev_btn_name.place(x=550, y=360, width=180, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
