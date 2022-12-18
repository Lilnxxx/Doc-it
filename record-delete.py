# Deleting records with images 
import tkinter  as tk 
from tkinter import *
from turtle import width
from setuptools import sic 
from sqlalchemy import create_engine
import io
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox as msg
import mysql.connector
import os

my_w = tk.Tk() # parent window 
my_w.geometry("500x500") # size as width height
my_w.title("Dashboard")  # Adding a title

global  r

# global v
images=[] # garbage collection 


def add_file():
    # print('------------',v)
    # if v<6:
    os.system(r'python uploadimg.py')
    for row in my_w.grid_slaves():# remove widgets
        row.grid_forget()
    display2()
  
# def update_file(fyl_name):
#     # print(del_data(fyl_name))
#     if del_data(fyl_name):
#         add_file()


def down_file(data):
    

    my_conn=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
    cur=my_conn.cursor()
    cur.execute("SELECT * FROM registation order by lastname")
    my_row=cur.fetchall()

    r0=int(r)-1
    student=my_row[r0]

    print(r)

    with open(student[data]+'.jpg', 'wb') as file:
        file.write(student[data+6])

def display2():

    l2=Label(my_w, text='Name') 
    l2.grid(row=0,column=1,padx=20) 
    l3=Label(my_w, text='Preview') 
    l3.grid(row=0,column=2,padx=50) 
    l4=Button(my_w, text='Add File',bg='yellow',command=add_file) 
    l4.grid(row=0,column=4,padx=20) 
    my_conn=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
    cur=my_conn.cursor()
    # cur.execute("SELECT * from registation order by lastname")
    # my_conn.commit()

    cur.execute("SELECT * FROM registation order by lastname")
    my_row=cur.fetchall()
    i=1 # data starts from row 1 
    j=6
    global  r

    f = open("myfile.txt", "r")
    r=int(f.read())
    r0=r-1
    # print(r)
    student=my_row[r0]
    # print(student)

    if student[6]!=None:
        e0 = Label(my_w, text=student[6]) 
        e0.grid(row=1,column=1,ipadx=5,pady=25)
        del0 = Button(my_w,text='Delete',bg='yellow',command=lambda k=6:del_data(k))
        del0.grid(row=1,column=4)
        down0 = Button(my_w,text='Download',bg='yellow',command=lambda k=6:down_file(6))
        down0.grid(row=1,column=5)

        

        try:
            stream = io.BytesIO(student[12])
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            print('img 0 ')
            img=0

        if img!=0:       
            em = Label(my_w, image=img) 
            # e = Label(my_w, text='no preview') 
            em.grid(row=1, column=2)   
            images.append(img) # garbage collection 

            # print(student[12])    
        else:
            em= Label(my_w, text='no preview') 
            em.grid(row=1, column=2,ipady=7) 

        
    if student[7]!=None:
        e1 = Label(my_w, text=student[7]) 
        e1.grid(row=2,column=1,ipadx=50,pady=25)
        stream = io.BytesIO(student[13])
        del1 = Button(my_w,text='Delete',bg='yellow',command=lambda k=7:del_data(k))
        del1.grid(row=2,column=4)
        down1 = Button(my_w,text='Download',bg='yellow',command=lambda k=7:down_file(k))
        down1.grid(row=2,column=5)
        try:
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            print('img 0 ')
            img=0

        if img!=0:
            # print()
            e = Label(my_w,image=img,text='folling') 
            e.grid(row=2, column=2,ipady=0)    
            images.append(img) # garbage collection 
   
        else:
            e = Label(my_w, text='no preview') 
            e.grid(row=2, column=2,ipady=7) 



    if student[8]!=None:
        e1 = Label(my_w, text=student[8]) 
        e1.grid(row=3,column=1,ipadx=50,pady=25)
        stream = io.BytesIO(student[14])
        del2 = Button(my_w,text='Delete',bg='yellow',command=lambda k=8:del_data(k))
        del2.grid(row=3,column=4)
        down2 = Button(my_w,text='Download',bg='yellow',command=lambda k=8:down_file(k))
        down2.grid(row=3,column=5)

        try:
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            print('img 0 ')
            img=0

        if img!=0:
            # print()
            e = Label(my_w,image=img,text='folling') 
            e.grid(row=3, column=2,ipady=0)     
            images.append(img) # garbage collection 
             
        else:
            e = Label(my_w, text='no preview') 
            e.grid(row=3, column=2,ipady=7) 



    if student[9]!=None:
        e1 = Label(my_w, text=student[9]) 
        e1.grid(row=4,column=1,ipadx=50,pady=25)
        stream = io.BytesIO(student[15])
       
        del3 = Button(my_w,text='Delete',bg='yellow',command=lambda k=9:del_data(k))
        del3.grid(row=4,column=4)
        down3 = Button(my_w,text='Download',bg='yellow',command=lambda k=9:down_file(k))
        down3.grid(row=4,column=5)

        try:
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            print('img 0 ')
            img=0

        if img!=0:
            # print()
            e = Label(my_w,image=img,text='folling') 
            e.grid(row=4, column=2,ipady=0)       
            images.append(img) # garbage collection

        else:
            e = Label(my_w, text='no preview') 
            e.grid(row=4, column=2,ipady=7) 
    
    
    if student[10]!=None:
        
        print("student 10 ")
        e1 = Label(my_w, text=student[10]) 
        e1.grid(row=5,column=1,ipadx=50,pady=25)
        stream = io.BytesIO(student[16])
        
        del4 = Button(my_w,text='Delete',bg='yellow',command=lambda k=10:del_data(k))
        del4.grid(row=5,column=4)
        down4 = Button(my_w,text='Download',bg='yellow',command=lambda k=10:down_file(k))
        down4.grid(row=5,column=5)

        try:
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            print('img 0 ')
            img=0

        if img!=0:
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            e = Label(my_w,image=img,text='folling') 
            e.grid(row=5, column=2,ipady=0)     
            images.append(img) # garbage collection
    
        else:
            e = Label(my_w, text='no preview') 
            e.grid(row=5, column=2,ipady=7) 
    
    
    if student[11]!=None:
        print("student 10 ")
        e1 = Label(my_w, text=student[11]) 
        e1.grid(row=6,column=1,ipadx=50,pady=25)
        stream = io.BytesIO(student[17])

        del5 = Button(my_w,text='Delete',bg='yellow',command=lambda k=6:del_data(k))
        del5.grid(row=6,column=4)
        down5 = Button(my_w,text='Download',bg='yellow',command=lambda k=11:down_file(k))
        down5.grid(row=6,column=5)


        try:
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            print('img 0 ')
            img=0

        if img!=0:
            # print()
            e = Label(my_w,image=img,text='folling') 
            e.grid(row=6, column=2,ipady=0)     
            images.append(img) # garbage collection
    
        else:
            e = Label(my_w, text='no preview') 
            e.grid(row=6, column=2,ipady=7) 


def display(): # show all records 
    # print('hi display')
    l2=Label(my_w, text='Name') 
    l2.grid(row=0,column=1) 
    l3=Label(my_w, text='Photo') 
    l3.grid(row=0,column=2) 
    l4=Button(my_w, text='Add File',bg='yellow',command=add_file) 
    l4.grid(row=0,column=4) 
    my_conn=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
    cur=my_conn.cursor()
    cur.execute("SELECT * FROM registation ")
    my_row=cur.fetchall()
    i=1 # data starts from row 1 
    j=6
    global  r

     
    f = open("myfile.txt", "r")
    id=f.read()
    r=int(id)-1
    student=my_row[r]

    e = Label(my_w, text=student[j]) 
    e.grid(row=i,column=1,ipadx=50,sticky='w')

    while  j<12: 
        stream = io.BytesIO(student[j+6])
        try:
            img=Image.open(stream)
            img=img.resize((50,50))  
            img = ImageTk.PhotoImage(img)  
        except:
            img=0
        # img =Image.open(img)
        # l= img.width
        # b=img.height
        # img=img.resize((20,20),Image.ANTIALIAS)  
        # e = Label(my_w, text=student[0]) 
        # e.grid(row=i,column=1,ipadx=20) 
        if student[j]==None:
            pass
            # e = Label(my_w, text='NULL') 
            # e.grid(row=i,column=1,ipadx=50,sticky='w') 
        else:
            e = Label(my_w, text=student[j]) 
            e.grid(row=i,column=1,ipadx=50,sticky='w') 
        if img!=0:
            e = Label(my_w, image=img) 
            e.grid(row=i, column=2,ipady=7) 
        elif student[j]==None:
            pass        
        else:
            e = Label(my_w, text='no preview') 
            e.grid(row=i, column=2,ipady=7) 

        if student[j]!=None:
            # e = Button(my_w,bg='Yellow',
            #     text='Update',command=lambda k=student[0]:update_file(k)) 
            # e.grid(row=i, column=3,ipady=3,ipadx=5,padx=20,pady=20,sticky='e') 

            e = Button(my_w,bg='Yellow',
                text='Delete',command=lambda:del_data(j)) 
            e.grid(row=i, column=4,ipady=3,ipadx=5,sticky='w') 
            
            e = Button(my_w,bg='Yellow',
                text='Download',command=lambda k=student[1]:down_file(k)) 
            e.grid(row=i, column=5,ipady=3,ipadx=5,padx=20) 
        else:
            pass    
        images.append(img) # garbage collection 
        i=i+1
        v=i 
        j=j+1
        

def del_data(s_id):
    my_conn=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
    cur=my_conn.cursor()
    try:
        my_var=msg.askyesnocancel("Delete Record",
           "This file will be deleted ? ",icon='warning')
        print(my_var,'---',s_id)
        if my_var:
        
            if s_id==6:
                query=("UPDATE registation SET photo_name = %s ,profile_photo=%s WHERE lastname =%s")
                my_data=[None,None,r]
                cur.execute(query,my_data)
                print('-------------------------------------------------',r)
            elif s_id==7:
                query=("UPDATE registation SET photo_name2 = %s ,profile_photo2=%s WHERE lastname =%s")
                my_data=[None,None,r]
                cur.execute(query,my_data)
            elif s_id==8:
                query=("UPDATE registation SET photo_name3 = %s ,profile_photo3=%s WHERE lastname =%s")
                my_data=[None,None,r]
                cur.execute(query,my_data)
            elif s_id==9:
                query=("UPDATE registation SET photo_name4 = %s ,profile_photo4=%s WHERE lastname =%s")
                my_data=[None,None,r]
                cur.execute(query,my_data)
            elif s_id==10:
                query=("UPDATE registation SET photo_name5= %s ,profile_photo5=%s WHERE lastname =%s")
                my_data=[None,None,r]
                cur.execute(query,my_data)
            elif s_id==11:
                query=("UPDATE registation SET photo_name6 = %s ,profile_photo6=%s WHERE lastname =%s")
                my_data=[None,None,r]
                cur.execute(query,my_data)
            else:
                print('big error')
            
            my_conn.commit()
            print("Row Deleted  ")
            # print(my_w.grid_slaves())
            for row in my_w.grid_slaves():# remove widgets
                row.grid_forget()
            display2() 
            # return my_var
            # refresh the list 
            # os.system(r'python uploadimg.py')
    except mysql as e:
        error = str(e.__dict__['orig'])
        print(error)
        return my_var




def dwn():
    my_conn=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
    cur=my_conn.cursor()
    # my_conn.free_results()
    cur.execute("SELECT * from registation order by lastname")
    print(cur.fetchall())
    my_conn.commit()
    my_conn.close()


display2()  # call to display all records 


my_w.mainloop()