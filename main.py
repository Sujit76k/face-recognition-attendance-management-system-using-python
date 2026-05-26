from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from PIL.Image import Resampling
from PIL import Image
from helpsupport import Helpsupport

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x700+0+0")
        self.root.title("Face Recognition Attendance Management System")

        # Header image
        img=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner.jpg")
        img=img.resize((1250,120),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1250,height=120)

        # Background image
        bg1=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1250,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1250,height=768)

        # Title
        title_lb1 = Label(bg_img,text="Face Recognition Attendance Management System",font=("verdana",20,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1250,height=40)

        # Student button
        std_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=220,y=100,width=180,height=180)
        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=220,y=250,width=180,height=40)

        # Detect Face button
        det_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)
        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2")
        det_b1.place(x=450,y=100,width=180,height=180)
        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detection",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=450,y=250,width=180,height=40)

        # Attendance button
        att_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)
        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2")
        att_b1.place(x=680,y=100,width=180,height=180)
        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=680,y=250,width=180,height=40)

        # Help Support button
        hlp_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)
        hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2")
        hlp_b1.place(x=910,y=100,width=180,height=180)
        hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Help Support",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=910,y=250,width=180,height=40)

        # Train Data button
        tra_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)
        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2")
        tra_b1.place(x=220,y=300,width=180,height=180)
        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=220,y=450,width=180,height=40)

        # QR Codes button
        pho_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\qr1.png")
        pho_img_btn=pho_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)
        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2")
        pho_b1.place(x=450,y=300,width=180,height=180)
        pho_b1_1 = Button(bg_img,command=self.open_img,text="QR Codes",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=450,y=450,width=180,height=40)

        # Developer button
        dev_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)
        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2")
        dev_b1.place(x=680,y=300,width=180,height=180)
        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=680,y=450,width=180,height=40)

        # Exit button
        exi_img_btn=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)
        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2")
        exi_b1.place(x=910,y=300,width=180,height=180)
        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=910,y=450,width=180,height=40)

    # Open images folder
    def open_img(self):
        os.startfile("data_img")

    # Functionality
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def Close(self):
        root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
