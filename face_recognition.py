from tkinter import*
# from tkinter import ttk
# from tkinter import messagebox
from PIL import Image,ImageTk
import cv2
# import numpy as np
# import os
import mysql.connector
from time import strftime
from datetime import datetime



class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")

        bg_image = Image.open(r"images\bg14.jpg")
        bg_image = bg_image.resize((1530,790),Image.Resampling.LANCZOS)     #converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(bg_image)

        bg_image = Label(self.root,image=self.photoimg)
        bg_image.place(x=0,y=0,width=1530,height=790)

        f_label = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        f_label.place(x=0,y=0,width=1530,height=50)

        bg1_image = Image.open(r"images\face3.jpg")
        bg1_image = bg1_image.resize((400,400),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(bg1_image)

        bg1_image = Label(self.root,image=self.photoimg1)
        bg1_image.place(x=580,y=150,width=400,height=400)

        b1= Button(self.root,text="Face Recognition",cursor="hand2",font=("times new roman",25,"bold"),bg="darkblue",fg="white",command=self.face_recognizer)
        b1.place(x=580,y=550,width=400,height=50)
    
    # Attendance

    def mark_attendance(self,i,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist = f.readlines()
            name_list=[]
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},present")

            







    # Face recognition
    def face_recognizer(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select ID from employee where ID="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)


                my_cursor.execute("select Name from employee where ID="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Department from employee where ID="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

               
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()