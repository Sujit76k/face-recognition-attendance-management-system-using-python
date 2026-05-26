from tkinter import *
import tkinter as tk

from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Attendance Management System Using Face Recognition")

        #-----------Variables-------------------
        self.var_dep=tk.StringVar()
        self.var_course=tk.StringVar()
        self.var_year=tk.StringVar()
        self.var_semester=tk.StringVar()
        self.var_std_id=tk.StringVar()
        self.var_std_name=tk.StringVar()
        self.var_div=tk.StringVar()
        self.var_roll=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_dob=tk.StringVar()
        self.var_email=tk.StringVar()
        self.var_mob=tk.StringVar()
        self.var_address=tk.StringVar()
        self.var_teacher=tk.StringVar()
        self.var_radio1 = tk.StringVar() # Add this line

        # Image labels
        img=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner.jpg")
        img=img.resize((1250,120),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lb1 = tk.Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1250,height=120)

        bg1=Image.open(r"D:\Downloads\Attendance_Management_System_Using_Face_Recognition-main\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1250,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = tk.Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1250,height=768)

        # Title
        title_lb1 = tk.Label(bg_img,text="Student Information Management Page",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1250,height=40)

        # Main Frame
        main_frame = tk.Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=1250,height=510)

        # Left Frame
        left_frame = tk.LabelFrame(main_frame,bd=2,bg="white",relief=tk.RIDGE,text="Information",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        # Current Course Info
        current_course_frame = tk.LabelFrame(left_frame,bd=2,bg="white",relief=tk.RIDGE,text="Current Course",font=("verdana",10,"bold"),fg="navyblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

        # Department
        dep_label=tk.Label(current_course_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select","Software Engineering","Cybersecurity","Business Administration","Digital Design")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=tk.W)

        # Course
        cou_label=tk.Label(current_course_frame,text="Course",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=2,padx=5,pady=15)
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("Select","STEM","Digital Graphics","Network Programming","Linux","AI")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=tk.W)

        # Year
        year_label=tk.Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=5,sticky=tk.W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select","2020","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=tk.W)

        # Semester
        semester_label=tk.Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        semester_label.grid(row=1,column=2,padx=5,sticky=tk.W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
        semester_combo["values"]=("Select","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=15,sticky=tk.W)

        # Student Information
        class_Student_frame = tk.LabelFrame(left_frame,bd=2,bg="white",relief=tk.RIDGE,text="Overview",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=160,width=635,height=230)

        # Student ID
        studentId_label = tk.Label(class_Student_frame,text="ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)

        # Student Name
        student_name_label = tk.Label(class_Student_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=tk.W)
        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=tk.W)

        # Division
        student_div_label = tk.Label(class_Student_frame,text="Shift:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Morning","Afternoon")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

        # Roll No
        student_roll_label = tk.Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=tk.W)
        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=tk.W)

        # Gender
        student_gender_label = tk.Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=tk.W)

        # Date of Birth
        student_dob_label = tk.Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=tk.W)
        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=tk.W)

        # Email
        student_email_label = tk.Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)
        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)

        # Phone Number
        student_mob_label = tk.Label(class_Student_frame,text="Mobile No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=tk.W)
        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=tk.W)

        # Address
        student_address_label = tk.Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)
        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=tk.W)

        # Teacher Name
        student_teacher_label = tk.Label(class_Student_frame,text="Teacher:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_teacher_label.grid(row=4,column=2,padx=5,pady=5,sticky=tk.W)
        student_teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        student_teacher_entry.grid(row=4,column=3,padx=5,pady=5,sticky=tk.W)

        # Radio Buttons for Photo Sample
        self.var_radio1 = tk.StringVar()
        radionbtn1 = tk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=5, column=0)
        radionbtn2 = tk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=5, column=1)

        # Button Frame (Like your screenshot)
        button_frame = tk.Frame(left_frame, bd=2, bg="white", relief=tk.RIDGE)
        button_frame.place(x=10, y=400, width=635, height=60)

        # Buttons (Save, Edit, Delete, Reset, Capture Photo, Edit Photo)
        button_names = ["Save", "Edit", "Delete", "Reset", "Capture Photo"]
        button_commands = [self.add_data, self.update_data, self.delete_data, self.reset_data, self.generate_dataset]

        for i, name in enumerate(button_names):
            button = tk.Button(button_frame, text=name, command=button_commands[i], width=10, font=("verdana", 10, "bold"), fg="white", bg="navyblue")
            button.grid(row=0, column=i, padx=5, pady=10)

        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE, text="List", font=("verdana", 12, "bold"), fg="navyblue")
        right_frame.place(x=680, y=10, width=660, height=480)

        # Searching System in Right Label Frame 
        search_frame = tk.LabelFrame(right_frame, bd=2, bg="white", relief=tk.RIDGE, text="Search", font=("verdana", 12, "bold"), fg="navyblue")
        search_frame.place(x=10, y=5, width=635, height=80)

        # Phone Number
        search_label = tk.Label(search_frame, text="Search:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.var_searchTX = tk.StringVar()

        # Combo box 
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchTX, width=12, font=("verdana", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=15, sticky=tk.W)

        self.var_search = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=12, font=("verdana", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        search_btn = tk.Button(search_frame, command=self.search_data, text="Search", width=9, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        search_btn.grid(row=0, column=3, padx=5, pady=10, sticky=tk.W)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame 
        table_frame = tk.Frame(right_frame, bd=2, bg="white", relief=tk.RIDGE)
        table_frame.place(x=10, y=90, width=635, height=360)

        # Scroll bar 
        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)

        # Create table 
        self.student_table = ttk.Treeview(table_frame, column=("ID", "Roll-No", "Name", "Dep", "DOB", "Email", "Photo", "Course", "Year", "Sem", "Div", "Gender", "Mob-No", "Address", "Teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Roll-No", text="Roll No")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="Photo")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Div", text="Shift")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Mob-No", text="Mobile No")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table["show"] = "headings"

        # Set Width of Columns 
        self.student_table.column("ID", width=20)
        self.student_table.column("Roll-No", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Photo", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Mob-No", width=100)
        self.student_table.column("Teacher", width=100)

        self.student_table.pack(fill=tk.BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

 # ==================Function Declaration==============================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please fill all required fields!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_std_id.get(),
                    self.var_roll.get(),  # Corrected Roll Number position.
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_dob.get(), # Corrected DOB position.
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_course.get(),
                    self.var_year.get(), # Corrected Year Position.
                    self.var_semester.get(), # Corrected Semester position.
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_mob.get(),
                    self.var_teacher.get(),
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "All records have been saved!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===========================Fetch data from database to table ================================
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ================================Get cursor function=======================
    # def get_cursor(self, event=""):
    #     cursor_focus = self.student_table.focus()
    #     content = self.student_table.item(cursor_focus)
    #     data = content["values"]

    #     self.var_std_id.set(data[0])
    #     self.var_std_name.set(data[1])
    #     self.var_dep.set(data[2])
    #     self.var_course.set(data[3])
    #     self.var_year.set(data[4])
    #     self.var_semester.set(data[5])
    #     self.var_div.set(data[6])
    #     self.var_gender.set(data[7])
    #     self.var_dob.set(data[8])
    #     self.var_mob.set(data[9])
    #     self.var_address.set(data[10])
    #     self.var_roll.set(data[11])
    #     self.var_email.set(data[12])
    #     self.var_teacher.set(data[13])
    #     self.var_radio1.set(data[14])

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        data = contents["values"]

        if data:
            self.var_std_id.set(data[0])  # StudentID
            self.var_roll.set(data[1])  # RollNumber
            self.var_std_name.set(data[2])  # Name
            self.var_dep.set(data[3])  # Department
            self.var_dob.set(data[4])  # DateOfBirth
            self.var_email.set(data[5])  # Email
            self.var_address.set(data[6])  # Address
            self.var_radio1.set(data[7])  # PhotoPath (Assuming radio1 is for PhotoPath)
            self.var_course.set(data[8])  # Course
            self.var_year.set(data[9])  # Year
            self.var_semester.set(data[10])  # Semester
            self.var_div.set(data[11])  # Shift
            self.var_gender.set(data[12])  # Gender
            self.var_mob.set(data[13])  # MobileNumber
            self.var_teacher.set(data[14])  # Teacher
        else:
            # Clear fields or handle no selection
            self.var_std_id.set("")
            self.var_roll.set("")
            self.var_std_name.set("")
            self.var_dep.set("Select Department")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.var_radio1.set("")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_semester.set("Select Semester")
            self.var_div.set("")
            self.var_gender.set("")
            self.var_mob.set("")
            self.var_teacher.set("")

        # ========================================Update Function==========================
    
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_std_id.get() == ""
            or self.var_std_name.get() == ""
            or self.var_roll.get() == ""
            or self.var_dob.get() == ""
            or self.var_gender.get() == ""
            or self.var_email.get() == ""
            or self.var_mob.get() == ""
            or self.var_address.get() == ""
            or self.var_teacher.get() == ""
        ):
            messagebox.showerror("Error", "Please fill in all the required fields!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(
                        username='root',
                        password='sujit',
                        host='localhost',
                        database='face_recognition',
                        port=3306,
                    )
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "UPDATE student SET RollNumber=%s, Name=%s, Department=%s, DateOfBirth=%s, Email=%s, Address=%s, PhotoPath=%s, Course=%s, Year=%s, Semester=%s, Shift=%s, Gender=%s, MobileNumber=%s, Teacher=%s WHERE StudentID=%s",
                        (
                            self.var_roll.get(),  # RollNumber
                            self.var_std_name.get(),  # Name
                            self.var_dep.get(),  # Department
                            self.var_dob.get(),  # DateOfBirth
                            self.var_email.get(),  # Email
                            self.var_address.get(),  # Address
                            self.var_radio1.get(),  # PhotoPath
                            self.var_course.get(),  # Course
                            self.var_year.get(),  # Year
                            self.var_semester.get(),  # Semester
                            self.var_div.get(),  # Shift
                            self.var_gender.get(),  # Gender
                            self.var_mob.get(),  # MobileNumber
                            self.var_teacher.get(),  # Teacher
                            self.var_std_id.get(),  # StudentID (WHERE clause)
                        ),
                    )

                    conn.commit()
                    messagebox.showinfo("Success", "Update successful!", parent=self.root)
                    self.fetch_data()
                    conn.close()
                elif not Update:
                    return

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID is required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
                    mycursor = conn.cursor() 
                    sql = "delete from student where StudentID=%s"
                    val = (self.var_std_id.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Deleted successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_div.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT StudentID,RollNumber,Name,Department,Department,Email,Address,PhotoPath,Course,Year,Semester,Shift,Email,Gender,MobileNumber,Teacher FROM student where RollNumber='" + str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows = my_cursor.fetchall()        
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror("Error", "Data Not Found", parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)



# #=====================This part is related to Opencv Camera part=======================
# # ==================================Generate Data set take image=========================
#     def generate_dataset(self):
#         if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
#             messagebox.showerror("Error", "Please fill in all required fields!", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(username='root', password='sujit', host='localhost', database='face_recognition', port=3306)
#                 mycursor = conn.cursor()
#                 mycursor.execute("select * from student")
#                 myreslut = mycursor.fetchall()
#                 id = 0
#                 for x in myreslut:
#                     id += 1

#                 mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where StudentID=%s", (
#                     self.var_std_name.get(),
#                     self.var_dep.get(),
#                     self.var_course.get(),
#                     self.var_year.get(),
#                     self.var_semester.get(),
#                     self.var_div.get(),
#                     self.var_gender.get(),
#                     self.var_dob.get(),
#                     self.var_mob.get(),
#                     self.var_address.get(),
#                     self.var_roll.get(),
#                     self.var_email.get(),
#                     self.var_teacher.get(),
#                     self.var_radio1.get(),
#                     self.var_std_id.get() == id + 1
#                 ))
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close()

#                 # ====================part of opencv=======================

#                 face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#                 def face_croped(img):
#                     # convert to grayscale
#                     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                     faces = face_classifier.detectMultiScale(gray, 1.3, 5)
#                     # Scaling factor 1.3
#                     # Minimum neighbors 5
#                     for (x, y, w, h) in faces:
#                         face_croped = img[y:y + h, x:x + w]
#                         return face_croped

#                 cap = cv2.VideoCapture(0)
#                 img_id = 0
#                 while True:
#                     ret, my_frame = cap.read()
#                     if face_croped(my_frame) is not None:
#                         img_id += 1
#                         face = cv2.resize(face_croped(my_frame), (200, 200))
#                         face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#                         file_path = "data_img/stdudent." + str(id) + "." + str(img_id) + ".jpg"
#                         cv2.imwrite(file_path, face)
#                         cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
#                         cv2.imshow("Capture Images", face)

#                     if cv2.waitKey(1) == 13 or int(img_id) == 100:
#                         break
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result", "Dataset creation completed!", parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_std_id.get() == ""
            or self.var_std_name.get() == ""
            or self.var_div.get() == ""
            or self.var_roll.get() == ""
            or self.var_gender.get() == ""
            or self.var_dob.get() == ""
            or self.var_email.get() == ""
            or self.var_mob.get() == ""
            or self.var_address.get() == ""
            or self.var_teacher.get() == ""
        ):
            messagebox.showerror("Error", "Please fill in all required fields!", parent=self.root)
        else:
            try:
                # OpenCV Part
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_crop = img[y : y + h, x : x + w]
                        return face_crop
                    return None  # Return None if no face is detected

                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    raise Exception("Could not open camera")

                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"data_img/student.{self.var_std_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                # Database Update Part
                conn = mysql.connector.connect(
                    username="root",
                    password="sujit",
                    host="localhost",
                    database="face_recognition",
                    port=3306,
                )
                mycursor = conn.cursor()
                mycursor.execute(
                   "UPDATE student SET RollNumber=%s, Name=%s, Department=%s, DateOfBirth=%s, Email=%s, Address=%s, PhotoPath=%s, Course=%s, Year=%s, Semester=%s, Shift=%s, Gender=%s, MobileNumber=%s, Teacher=%s WHERE StudentID=%s",
                        (
                            self.var_roll.get(),  # RollNumber
                            self.var_std_name.get(),  # Name
                            self.var_dep.get(),  # Department
                            self.var_dob.get(),  # DateOfBirth
                            self.var_email.get(),  # Email
                            self.var_address.get(),  # Address
                            self.var_radio1.get(),  # PhotoPath
                            self.var_course.get(),  # Course
                            self.var_year.get(),  # Year
                            self.var_semester.get(),  # Semester
                            self.var_div.get(),  # Shift
                            self.var_gender.get(),  # Gender
                            self.var_mob.get(),  # MobileNumber
                            self.var_teacher.get(),  # Teacher
                            self.var_std_id.get(),  # StudentID (WHERE clause)
                        ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                messagebox.showinfo("Result", "Dataset creation completed!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


# main class object

if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()