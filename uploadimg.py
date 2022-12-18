import tkinter as tk
from tkinter import Label, filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from sqlalchemy import create_engine
from tkinter import messagebox as msg
import mysql.connector
# from signup_page import *

my_w = tk.Tk()
my_w.geometry("400x200")  # Size of the window 
my_w.title('Upload fyl')
my_font1=('times', 18, 'bold')

l1 = tk.Label(my_w,text='Add Student Data with Photo',font=my_font1)  
# l1.grid(row=1,column=1,columnspan=5)

l2 = tk.Label(my_w,  text='File name', width=10 )  # added one Label 
l2.grid(row=2,column=1)

e1 = tk.Entry(my_w,width=10,bg='yellow') # added one Entry box
e1.grid(row=2,column=2)

b1 = tk.Button(my_w, text='Upload File', 
   command = lambda:upload_file())
b1.grid(row=2,column=4) 

my_font=('times', 12, 'bold')
b2 = tk.Button(my_w, text='Add data', font=my_font,command = lambda:add_data())
b2.grid(row=2,column=5,padx=20) 

global filename # Access this from both functions
filename=''



##### function to upload_file() ###
def upload_file(): # Image upload and display
    global filename,img, img_icon
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg'),('All Files',"*")]
    try:
        filename = filedialog.askopenfilename(filetypes=f_types)

        # img = ImageTk.PhotoImage(file=filename)
        img_icon=Image.open(filename)
        img_icon=img_icon.resize((90,90))  
        img_icon = ImageTk.PhotoImage(img_icon)
        b2 =tk.Button(my_w,image=img_icon) # using Button 
        b2.grid(row=4,column=1,columnspan=2)#display uploaded photo
    except :
        b2= Label(my_w,text=filename)
        b2.grid(row=4,column=1,columnspan=2)#display uploaded photo
        
    # except:
    #     messagebox.showwarning("showwarning", "No File Selected")
        
##### function to add_data() ####
def add_data(): # Add data to MySQL table 
    global img , filename 
    if filename!='' and e1.get()!='':    
        fob=open(filename,'rb') # filename from upload_file()
        fob=fob.read()
        
        f = open("myfile.txt", "r")
        id=f.read()
        r=int(id)-1
        
        # data=(e1.get(),fob) # tuple with data 
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
        cur=mysqldb.cursor()
        cur.execute('select * from registation order by lastname')
        data0 = cur.fetchall()

        print(r,type(r))
        # print(data0)
        # print(data0[0][6])
    
        if data0[r][6] is None:
            print('1st null',data0[0][6])
            cur.execute("UPDATE registation SET photo_name = %s ,profile_photo=%s WHERE lastname =%s"
            ,(e1.get(),fob,id))
            
        elif data0[r][7] is None:
            cur.execute("UPDATE registation SET photo_name2 = %s ,profile_photo2=%s WHERE lastname =%s"
            ,(e1.get(),fob,id))
            
        elif data0[r][8] is None:
            cur.execute("UPDATE registation SET photo_name3 = %s ,profile_photo3=%s WHERE lastname =%s"
            ,(e1.get(),fob,id))
            
        elif data0[r][9] is None:
            cur.execute("UPDATE registation SET photo_name4 = %s ,profile_photo4=%s WHERE lastname =%s"
            ,(e1.get(),fob,id))
            
        elif data0[r][10] is None:
            cur.execute("UPDATE registation SET photo_name5 = %s ,profile_photo5=%s WHERE lastname =%s"
            ,(e1.get(),fob,id))
            
        elif data0[r][11] is None:
            cur.execute("UPDATE registation SET photo_name6 = %s ,profile_photo6=%s WHERE lastname =%s"
            ,(e1.get(),fob,id))
            
        else:
            msg.showerror("error",'Limit Files Reached')
                   
        
        # cur.execute("UPDATE registation SET photo_name = %s ,profile_photo=%s WHERE lastname =%s",(e1.get(),fob,id))

        # id=cur.execute("INSERT INTO  student_profile(student,profile_photo) VALUES (%s,%s)",data)
        # (self.new_pass_entry.get(),self.e1.get(),))

        mysqldb.commit()
        # print("Row Added  = ",id.rowcount) # displayed in console 
        my_w.destroy() # close window after adding data
    else:
        msg.showerror("error",'please upload file and enter name')

my_w.mainloop()  # Keep the