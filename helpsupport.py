from tkinter import *
from PIL import Image, ImageTk
import webbrowser


class Helpsupport:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Attendance Management System Using Face Recognition")

        # ------------------ Header image setup ------------------
        img = Image.open(
            r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner.jpg")
        img = img.resize((1250, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1250, height=120)

        # ------------------ Background image setup ------------------
        bg1 = Image.open(
            r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg4.png")
        bg1 = bg1.resize((1250, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set background as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1250, height=768)

        # ------------------ Title Section ------------------
        title_lb1 = Label(bg_img, text="Help & Support", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # ------------------ Buttons Section ------------------
        # Button 1: Website
        std_img_btn = Image.open(
            r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\web.png")
        std_img_btn = std_img_btn.resize((180, 180),Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.website, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=200, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.website, text="Website", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=250, y=380, width=180, height=45)

        # Button 2: Facebook
        det_img_btn = Image.open(
            r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\fb.png")
        det_img_btn = det_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.facebook, image=self.det_img1, cursor="hand2", )
        det_b1.place(x=480, y=200, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.facebook, text="Facebook", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=480, y=380, width=180, height=45)

        # Button 3: YouTube
        att_img_btn = Image.open(
            r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\yt.png")
        att_img_btn = att_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.youtube, image=self.att_img1, cursor="hand2", )
        att_b1.place(x=710, y=200, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.youtube, text="Youtube", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=710, y=380, width=180, height=45)

        # Button 4: Gmail
        hlp_img_btn = Image.open(
            r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\gmail.png")
        hlp_img_btn = hlp_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, command=self.gmail, image=self.hlp_img1, cursor="hand2", )
        hlp_b1.place(x=940, y=200, width=180, height=180)

        hlp_b1_1 = Button(bg_img, command=self.gmail, text="Gmail", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_1.place(x=940, y=380, width=180, height=45)

    # ------------------ Link Functions ------------------
    def website(self):
        self.new = 1
        self.url = "http://www.google.com"
        webbrowser.open(self.url, new=self.new)

    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com"
        webbrowser.open(self.url, new=self.new)

    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com"
        webbrowser.open(self.url, new=self.new)

    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url, new=self.new)


if __name__ == "__main__":
    root = Tk()
    obj = Helpsupport(root)
    root.mainloop()
Image.Resampling.LANCZOS