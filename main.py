from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from employee import Employee
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance


class Face_Recognition_Attendence_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")

        # first image

        img1 = Image.open(r"images\company3.jpg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)     #converts high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130) 

        #second image

        img2 = Image.open(r"images\logo1.png") 
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)     
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130) 
        
         # third image

        img3 = Image.open(r"images\company3.jpg")
        img3 = img3.resize((500,130),Image.Resampling.LANCZOS)     #converts high level image to low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130) 

        # bg image

        img4 = Image.open(r"images\bg14.jpg")
        img4 = img4.resize((1530,790),Image.Resampling.LANCZOS)     #converts high level image to low level image
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=790) 

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #employee button

        img5 = Image.open(r"images\icon1.png")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,command=self.employee_details,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,command=self.employee_details,text="Employee Details",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=300,width=220,height=40)

        #face detect button

        img6 = Image.open(r"images\icon2.png")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_detector)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1 = Button(bg_img,text="Face Detector",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2",command=self.face_detector)
        b2_1.place(x=500,y=300,width=220,height=40)

        #attendance button

        img7 = Image.open(r"images\icon3.png")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_1 = Button(bg_img,text="Attendance",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b3_1.place(x=800,y=300,width=220,height=40)

        # help button

        img8 = Image.open(r"images\icon4.png")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1 = Button(bg_img,text="Help",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=1100,y=300,width=220,height=40)

        #Train data button

        img9 = Image.open(r"images\icon5.png")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=400,width=220,height=220)

        b5_1 = Button(bg_img,text="Train Data",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2",command=self.train_data)
        b5_1.place(x=200,y=600,width=220,height=40)

        #Photos button

        img10 = Image.open(r"images\icon6.png")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img,command=self.open_img,image=self.photoimg10,cursor="hand2")
        b6.place(x=500,y=400,width=220,height=220)

        b6_1 = Button(bg_img,text="Photos",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b6_1.place(x=500,y=600,width=220,height=40)

        #developer button

        img11 = Image.open(r"images\icon7.png")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)     
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=800,y=400,width=220,height=220)

        b7_1 = Button(bg_img,text="Developer",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b7_1.place(x=800,y=600,width=220,height=40)

        #exit button

        img12 = Image.open(r"images\icon8.png")
        img12 = img12.resize((230,220),Image.Resampling.LANCZOS)     
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b8_1 = Button(bg_img,image=self.photoimg12,cursor="hand2")
        b8_1.place(x=1100,y=400,width=220,height=220)

        b8_1_1 = Button(bg_img,text="Exit",font=("times new roman",15,"bold"),bg="darkBlue",fg="white",cursor="hand2")
        b8_1_1.place(x=1100,y=600,width=220,height=40)

    # function to open images in data folder
    def open_img(self):
        os.startfile("data")

    
    #function to show employee details

    def employee_details(self):
            self.new_window = Toplevel(self.root) 
            self.app = Employee(self.new_window)
    

    def train_data(self):
         self.new_window = Toplevel(self.root)   
         self.app = Train(self.new_window)
    
    def face_detector(self):
         self.new_window = Toplevel(self.root)   
         self.app = Face_recognition(self.new_window)

    def attendance(self):
         self.new_window = Toplevel(self.root)
         self.app = Attendance(self.new_window)

         
    









if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Attendence_System(root)
    root.mainloop()