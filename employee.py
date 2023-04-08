from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")

        #variables"dep","name","id","post","gender","dob","phone","address","photo"

        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_id = StringVar()
        self.var_mail = StringVar()
        self.var_post = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_photo = StringVar()        
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()
        
        # first image

        img1 = Image.open(r"images\logo3.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS) #converts high level image to low level image
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

        img3 = Image.open(r"images\logo3.png")
        img3 = img3.resize((500,130),Image.Resampling.LANCZOS)     
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130) 

        # bg image

        img4 = Image.open(r"images\bgimg1.png")
        img4 = img4.resize((1530,790),Image.Resampling.LANCZOS)    
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=790) 

        title_lbl = Label(bg_img,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #main frame

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame

        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"),bg="lavender")
        left_frame.place(x=10,y=20,width=730,height=560)

        # #image

        # img_left = Image.open(r"C:\Users\karan\Pictures\final_project\employee.jpg")
        # img_left = img_left.resize((720,130),Image.Resampling.LANCZOS)     
        # self.photoimg_left = ImageTk.PhotoImage(img_left)

        # f_lbl = Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=720,height=130)

        #frame inside left frame

        # left_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        # left_frame.place(x=5,y=140,width=715,height=410)


        #department

        dep_label = Label(left_frame,text="Department:",font=("times new roman",12,"bold"))
        # dep_label.place(x=10,y=10)
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        dep_combo = ttk.Combobox(left_frame,textvariable=self.var_dep,state="read only",font=("times new roman",12,"bold"),width=35)
        dep_combo["values"] = ("Select Department","Chemical")
        dep_combo.current(0)
        # dep_combo.place(x=150,y=10)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #name
        
        name_label = Label(left_frame,text="Employee Name:",font=("times new roman",12,"bold"))
        # name_label.place(x=10,y=50)
        name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
      
        name_entry = ttk.Entry(left_frame,textvariable=self.var_name,state="read only",font=("times new roman",12,"bold"),width=35)
        # name_entry.place(x=150,y=50)
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #id

        id_label = Label(left_frame,text="Employee ID:",font=("times new roman",12,"bold"))
        # id_label.place(x=10,y=90)
        id_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
      
        id_entry = ttk.Entry(left_frame,textvariable=self.var_id,state="read only",font=("times new roman",12,"bold"),width=35)
        # id_entry.place(x=150,y=90)
        id_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #mail

        mail_label = Label(left_frame,text="Email:",font=("times new roman",12,"bold"))
        # mail_label.place(x=10,y=130)
        mail_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
      
        mail_entry = ttk.Entry(left_frame,textvariable=self.var_mail,state="read only",font=("times new roman",12,"bold"),width=35)
        # mail_entry.place(x=150,y=130)
        mail_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #Post

        post_label = Label(left_frame,text="Post:",font=("times new roman",12,"bold"))
        # post_label.place(x=10,y=170)
        post_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)
      
        post_combo = ttk.Combobox(left_frame,textvariable=self.var_post,state="read only",font=("times new roman",12,"bold"),width=35)
        post_combo["values"] = ("Select Post","Manager","Employee")
        post_combo.current(0)
        # post_combo.place(x=150,y=170)
        post_combo.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #DOB

        dob_label = Label(left_frame,text="DOB:",font=("times new roman",12,"bold"))
        # dob_label.place(x=10,y=210)
        dob_label.grid(row=5,column=0,padx=10,pady=10,sticky=W)
      
        dob_entry = ttk.Entry(left_frame,textvariable=self.var_dob,state="read only",font=("times new roman",12,"bold"),width=35)
        # dob_entry.place(x=150,y=210)
        dob_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        #Gender

        gender_label = Label(left_frame,text="Gender:",font=("times new roman",12,"bold"))
        # gender_label.place(x=10,y=250)
        gender_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        gender_combo = ttk.Combobox(left_frame,textvariable=self.var_gender,state="read only",font=("times new roman",12,"bold"),width=35)
        gender_combo["values"] = ("Select gender","Male","Female","Other")
        gender_combo.current(0)
        # gender_combo.place(x=150,y=250)
        gender_combo.grid(row=6,column=1,padx=10,pady=10,sticky=W)
      
        # gender_entry = ttk.Entry(left_frame,textvariable=self.var_gender,state="read only",font=("times new roman",12,"bold"),width=35)
        # gender_entry.place(x=150,y=250)

        #phone no

        phone_label = Label(left_frame,text="Phone No:",font=("times new roman",12,"bold"))
        # phone_label.place(x=10,y=290)
        phone_label.grid(row=7,column=0,padx=10,pady=10,sticky=W)

        phone_entry = ttk.Entry(left_frame,textvariable=self.var_phone,state="read only",font=("times new roman",12,"bold"),width=35)
        # phone_entry.place(x=150,y=290)
        phone_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        #address

        address_label = Label(left_frame,text="Address:",font=("times new roman",12,"bold"))
        # address_label.place(x=10,y=330)
        address_label.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        address_entry = ttk.Entry(left_frame,textvariable=self.var_address,state="read only",font=("times new roman",12,"bold"),width=35)
        # address_entry.place(x=150,y=330)
        address_entry.grid(row=8,column=1,padx=10,pady=10,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(left_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        # radiobtn1.place(x=10,y=380)
        radiobtn1.grid(row=9,column=0,padx=10,pady=10,sticky=W)

        
        radiobtn2 = ttk.Radiobutton(left_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        # radiobtn2.place(x=150,y=380)
        radiobtn2.grid(row=9,column=1,padx=10,pady=10,sticky=W)

        #button frame

        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=450,width=704,height=120)

        #save

        save_btn = Button(btn_frame,command=self.add_data,text="Save",font=("times new roman",12,"bold"),bg="green",fg="white")
        save_btn.place(x=0,y=0,width=175,height=35)

        #update

        update_btn = Button(btn_frame,command=self.update_data,text="Update",font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.place(x=175,y=0,width=175,height=35)

        #delete

        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="white")
        delete_btn.place(x=350,y=0,width=175,height=35)
        
        #reset

        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",font=("times new roman",12,"bold"),bg="green",fg="white")
        reset_btn.place(x=525,y=0,width=175,height=35)

        #take photo

        takephoto_btn = Button(btn_frame,command=self.generate_dataset,text="Take Photo",font=("times new roman",12,"bold"),bg="green",fg="white")
        takephoto_btn.place(x=0,y=40,width=350,height=35)

        #update photo

        update_btn = Button(btn_frame,text="Update Photo",font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.place(x=350,y=40,width=350,height=35)




        #right label frame

        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"),bg="lavender")
        right_frame.place(x=750,y=20,width=715,height=560)

        #search system

        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=20,width=700,height=80)



        search_label = Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        self.search_combo = ttk.Combobox(search_frame,state="readonly",font=("times new roman",12,"bold"),width=29)
        self.search_combo["values"] = ("Select","ID","Phone_No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.search_entry = ttk.Entry(search_frame,font=("times new roman",12,"bold"))
        self.search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        search_btn = Button(search_frame,command=self.search_entries,text="Search",font=("times new roman",12,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn = Button(search_frame,text="Show All",command=self.showall,font=("times new roman",12,"bold"),bg="green",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        #table frame

        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=120,width=700,height=380)

        #scroll bar

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)

        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame,column=("dep","name","id","email","post","gender","dob","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("id",text="ID")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("post",text="Post")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("photo",text="PhotoSample")

        self.employee_table["show"] = "headings"

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("id",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("post",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("photo",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    
    
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_post.get()=="Select Post":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_mail.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get()
                
                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added successfully",parent=self.root)                
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_name.set(data[1]),
        self.var_id.set(data[2]),
        self.var_mail.set(data[3]),
        self.var_post.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_phone.set(data[7]),
        self.var_address.set(data[8]),
        self.var_radio1.set(data[9])

#update data

    def update_data(self):
            if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_post.get()=="Select Post":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    update=messagebox.askyesno("Update","Do you want to update this employee details",parent=self.root)
                    if update>0:
                        conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("Update employee set Department=%s,Name=%s,Email=%s,Post=%s,Gender=%s, Dob=%s,Phone=%s,Address=%s,PhotoSample=%s where id=%s", (

                                                                                                    self.var_dep.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_mail.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get(),
                                                                                                    self.var_id.get()



                                                                                                    ))


                    else:
                        if not update:
                            return 
                    messagebox.showinfo("Success","Employee details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  

    #delete data

    def delete_data(self):
            if self.var_id.get()=="": 
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                try:
                    delete=messagebox.askyesno("Delete","Do you want to delete this employee",parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
                        my_cursor=conn.cursor()
                        sql="delete from employee where id=%s"
                        val=(self.var_id.get(),)
                        my_cursor.execute(sql,val)
                        
                    else:
                        if not delete:
                            return

                    messagebox.showinfo("Delete","Successfully deleted emmployee details",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  


    def reset_data(self):
        self.var_dep.set("select department"),
        self.var_name.set(""),
        self.var_id.set(""),
        self.var_mail.set(""),
        self.var_post.set("select post"),
        self.var_gender.set("select gender"),
        self.var_dob.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")



# Generate data set or take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_post.get()=="Select Post":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update employee set Department=%s,Name=%s,Email=%s,Post=%s,Gender=%s, Dob=%s,Phone=%s,Address=%s,PhotoSample=%s where id=%s",(

                                                                                    self.var_dep.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_mail.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_radio1.get(),
                                                                                    self.var_id.get()==id+1

                                                                           ))


                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
    

                #=============Load predifiend data on face frontals from opencv=========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!!!")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                


    def search_entries(self):
        conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
        my_cursor=conn.cursor()


    
        search_type = self.search_combo.get()
        search_value = self.search_entry.get()
    
        self.employee_table.delete(*self.employee_table.get_children())

        if search_type == "ID":
            query = "SELECT * FROM employee WHERE id = %s"
        elif search_type == "Phone_No":
            query = "SELECT * FROM employee WHERE phone = %s"
        else:
            messagebox.showerror("Error", "Please select a valid search type.")
            return
    
    # Execute the query with the search value as a parameter
        my_cursor.execute(query, (search_value,))
        rows = my_cursor.fetchall()
    
    # Display the results in the table
        for row in rows:
            self.employee_table.insert("", "end", values=row)
        conn.close()
    

    def showall(self):
        conn=mysql.connector.connect(host="127.0.0.1",user="sanket",password="Sanket@123",database="face_recognizer")
        my_cursor=conn.cursor()
        for record in self.employee_table.get_children():
            self.employee_table.delete(record)
        
    # Fetch all data from the database
        my_cursor.execute("SELECT * FROM employee")
        rows = my_cursor.fetchall()
        
    # Insert data into the table
        for row in rows:
            self.employee_table.insert("", END, values=row)


    




if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()