# from sys import path
# from tkinter import*
# from tkinter import ttk
# from PIL import Image, ImageTk
# import os
# import mysql.connector
# import cv2
# import numpy as np
# from tkinter import messagebox
# from time import strftime
# from datetime import datetime
# import time


# class Face_Recognition:

#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1250x700+0+0")
#         self.root.title("Face Recognition Based Attendance Management System")

#         # Header image setup
#         header_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner.jpg")
#         header_img = header_img.resize((1250, 120), Image.Resampling.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(header_img)

#         header_label = Label(self.root, image=self.photoimg)
#         header_label.place(x=0, y=0, width=1250, height=120)

#         # Background image
#         bg_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg3.jpg")
#         bg_img = bg_img.resize((1250, 768), Image.Resampling.LANCZOS)
#         self.photobg1 = ImageTk.PhotoImage(bg_img)

#         bg_label = Label(self.root, image=self.photobg1)
#         bg_label.place(x=0, y=130, width=1250, height=768)

#         # Title section
#         title_label = Label(bg_label, text="Welcome to the Face Recognition System", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
#         title_label.place(x=0, y=0, width=1250, height=40)

#         # Face Recognition Button with image
#         recog_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\f_det.jpg")
#         recog_img = recog_img.resize((180, 180), Image.Resampling.LANCZOS)
#         self.std_img1 = ImageTk.PhotoImage(recog_img)

#         recog_btn = Button(bg_label, command=self.face_recog, image=self.std_img1, cursor="hand2")
#         recog_btn.place(x=600, y=170, width=180, height=180)

#         recog_btn_text = Button(bg_label, command=self.face_recog, text="Face Recognition", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         recog_btn_text.place(x=600, y=350, width=180, height=45)

#     # ===================== Attendance ====================
#     def mark_attendance(self, i, r, n):
#         with open("attendance.csv", "r+", newline="\n") as f:
#             myDatalist = f.readlines()
#             name_list = []
#             for line in myDatalist:
#                 entry = line.split(",")
#                 name_list.append(entry[0])

#             if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
#                 now = datetime.now()
#                 date = now.strftime("%d/%m/%Y")
#                 time_str = now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{i}, {r}, {n}, {time_str}, {date}, Present")

#     # ================= Face Recognition ==================
#     def face_recog(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
#             coord = []

#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#                 id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#                 confidence = int((100 * (1 - predict / 300)))

#                 conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
#                 cursor = conn.cursor()

#                 cursor.execute("SELECT Name FROM student WHERE StudentID=" + str(id))
#                 n = cursor.fetchone()
#                 if n:
#                     n = "+".join(n)
#                 else:
#                     n = "Unknown"

#                 cursor.execute(
#                     "SELECT RollNumber FROM student WHERE StudentID=" + str(id)
#                 ) 
#                 r = cursor.fetchone()
#                 if r:
#                     r = "+".join(r)
#                 else:
#                     r = "Unknown"

#                 cursor.execute("SELECT StudentID FROM student WHERE StudentID=" + str(id))
#                 i = cursor.fetchone()
#                 if i:
#                     i = "+".join(i)
#                 else:
#                     i = "Unknown"

#                 if confidence > 77:
#                     cv2.putText(img, f"StudentID: {i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                     cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                     cv2.putText(img, f"RollNumber: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                     self.mark_attendance(i, r, n)
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

#                 coord = [x, y, w, h]
#                 conn.close()

#             return coord

#         def recognize(img, clf, faceCascade):
#             coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
#             return img

#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("clf.xml")

#         videoCap = cv2.VideoCapture(0)
#         start_time = time.time()
#         while True:
#             ret, img = videoCap.read()
#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("Face Recognition", img)

#             if cv2.waitKey(1) == 5:  
#                 break
#             if time.time() - start_time >= 10:  # Check if 10 seconds have passed
#                 break
        
#         videoCap.release()
#         cv2.destroyAllWindows()


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()


from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import time


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Face Recognition Based Attendance Management System")

        # Header image setup
        header_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner.jpg")
        header_img = header_img.resize((1250, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(header_img)

        header_label = Label(self.root, image=self.photoimg)
        header_label.place(x=0, y=0, width=1250, height=120)

        # Background image
        bg_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg3.jpg")
        bg_img = bg_img.resize((1250, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.photobg1)
        bg_label.place(x=0, y=130, width=1250, height=768)

        # Title section
        title_label = Label(bg_label, text="Welcome to the Face Recognition System", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_label.place(x=0, y=0, width=1250, height=40)

        # Face Recognition Button with image
        recog_img = Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\f_det.jpg")
        recog_img = recog_img.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(recog_img)

        recog_btn = Button(bg_label, command=self.face_recog, image=self.std_img1, cursor="hand2")
        recog_btn.place(x=600, y=170, width=180, height=180)

        recog_btn_text = Button(bg_label, command=self.face_recog, text="Face Recognition", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        recog_btn_text.place(x=600, y=350, width=180, height=45)

    # ===================== Attendance ====================
    # def mark_attendance(self, i, r, n):
    #     with open("attendance.csv", "r+", newline="\n") as f:
    #         myDatalist = f.readlines()
    #         name_list = []
    #         for line in myDatalist:
    #             entry = line.split(",")
    #             name_list.append(entry[0])

    #         if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
    #             now = datetime.now()
    #             date = now.strftime("%d/%m/%Y")
    #             time_str = now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i}, {r}, {n}, {time_str}, {date}, Present")
    #             print(f"Attendance recorded to CSV: StudentID={i}, RollNumber={r}, Name={n}, Time={time_str}, Date={date}") #optional print.

    # ================= Face Recognition ==================
    # def face_recog(self):
    #     def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    #         coord = []

    #         for (x, y, w, h) in features:
    #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
    #             confidence = int((100 * (1 - predict / 300)))

    #             conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
    #             cursor = conn.cursor()

    #             cursor.execute("SELECT Name FROM student WHERE StudentID=" + str(id))
    #             n = cursor.fetchone()
    #             if n:
    #                 n = "+".join(n)
    #             else:
    #                 n = "Unknown"

    #             cursor.execute(
    #                 "SELECT RollNumber FROM student WHERE StudentID=" + str(id)
    #             )
    #             r = cursor.fetchone()
    #             if r:
    #                 r = "+".join(r)
    #             else:
    #                 r = "Unknown"

    #             cursor.execute("SELECT StudentID FROM student WHERE StudentID=" + str(id))
    #             i = cursor.fetchone()
    #             if i:
    #                 i = "+".join(i)
    #             else:
    #                 i = "Unknown"

    #             if confidence > 77:
    #                 cv2.putText(img, f"StudentID: {i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
    #                 cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
    #                 cv2.putText(img, f"RollNumber: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
    #                 self.mark_attendance(i, r, n)
    #             else:
    #                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    #                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

    #             coord = [x, y, w, h]
    #             conn.close()

    #         return coord

    def mark_attendance(self, i, r, n):
        try:
            with open("attendance.csv", "r+", newline="\n") as f:
                myDatalist = f.readlines()
                name_list = []
                for line in myDatalist:
                    entry = line.split(",")
                    name_list.append(entry[0])

                if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                    now = datetime.now()
                    date = now.strftime("%d/%m/%Y")
                    time_str = now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i}, {r}, {n}, {time_str}, {date}, Present")
                    print(f"Attendance recorded to CSV: StudentID={i}, RollNumber={r}, Name={n}, Time={time_str}, Date={date}")  # Optional print.
        except Exception as e:
            print(f"Error writing to attendance.csv: {e}")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
                cursor = conn.cursor()

                cursor.execute("SELECT Name FROM student WHERE StudentID=" + str(id))
                n_result = cursor.fetchone()
                n = n_result[0] if n_result else "Unknown"

                cursor.execute("SELECT RollNumber FROM student WHERE StudentID=" + str(id))
                r_result = cursor.fetchone()
                r = r_result[0] if r_result else "Unknown"

                cursor.execute("SELECT StudentID FROM student WHERE StudentID=" + str(id))
                i_result = cursor.fetchone()
                i = str(i_result[0]) if i_result else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"StudentID: {i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"RollNumber: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]
                conn.close()

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)
        start_time = time.time()
        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
            

        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()