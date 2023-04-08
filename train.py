from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import cv2
import numpy as np
import os



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")

        bg_image = Image.open(r"images\bg14.jpg")
        bg_image = bg_image.resize((1530,790),Image.Resampling.LANCZOS)     #converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(bg_image)

        bg_image = Label(self.root,image=self.photoimg)
        bg_image.place(x=0,y=0,width=1530,height=790)

        f_label = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        f_label.place(x=0,y=0,width=1530,height=50)

        bg1_image = Image.open(r"images\face2.jpg")
        bg1_image = bg1_image.resize((400,400),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(bg1_image)

        bg1_image = Label(self.root,image=self.photoimg1)
        bg1_image.place(x=580,y=150,width=400,height=400)

        b1= Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="darkblue",fg="white")
        b1.place(x=580,y=550,width=400,height=50)

        


    def train_classifier(self):
            data_dir = ("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L')  #gray scale image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Dataset Completed")










if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()