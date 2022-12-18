from tkinter import *
import tkinter
import os
from tkinter import filedialog
from tkinter import messagebox
# import required module
from cryptography.fernet import Fernet


root = Tk()
root.geometry('450x300')
root.resizable(False,False)



encr_file = tkinter.StringVar()
decr_file = tkinter.StringVar()
key_file = tkinter.StringVar()


def encrt1():

    # file_name = filedialog.askopenfilename( filetypes =[('All Files', '*.*')])
    file_name= encr_file.get()
    encr_file.set('')
    # file_ext=os.path.basename(file_name)
    # key generation
    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    try:
        with open(file_name, 'rb') as file:
            original = file.read()
    except:
        messagebox.showwarning("showwarning", "No File Selected ")
        return    
    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt1():

    # key_file_name = filedialog.askopenfilename( filetypes =[('Key Files', ' *.key'),('All Files', '*.*')])
    key_file_name= key_file.get()
    file_name= decr_file.get()
    decr_file.set('')
    key_file.set('')
    # opening the key
    try:
        with open(key_file_name, 'rb') as filekey:
            key = filekey.read()
    except:
            messagebox.showwarning("showwarning", "No File Selected ")
            return

    fernet = Fernet(key)

    # file_name = filedialog.askopenfilename( filetypes =[('All Files', '*.*')])
    file_ext=os.path.basename(file_name)
    # print(file_ext)
    # file_ext=os.path.splitext(file_ext)[0]
    # opening the original file to encrypt
    try:
        with open(file_name, 'rb') as file:
            original = file.read()
    except:
        messagebox.showwarning("showwarning", "No File Selected ")
        return    
    # encrypting the file
    # print(file_ext)

    decrypted = fernet.decrypt(original)
    # opening the file in write mode and
    # writing the encrypted data
    with open(file_ext, 'wb') as encrypted_file:
        encrypted_file.write(decrypted)

def select_fyl():
    file_name = filedialog.askopenfilename( filetypes =[('All Files', '*.*')])
    encr_file.set(file_name)

def select_fyl2():
    file_name = filedialog.askopenfilename( filetypes =[('All Files', '*.*')])
    decr_file.set(file_name)

def select_key():
    file_name = filedialog.askopenfilename( filetypes =[('All Files', '*.*')])
    key_file.set(file_name)


lbl_1=Label(root,text='Image/File Encryption',font = ('calibre',13,'bold'))
lbl_1.place(x=160,y=0)

lbl_2=Label(root,text='Select file : ')
entry_2=Entry(root,textvariable=encr_file,width=50) 
btn2= Button(root,text='..',command=select_fyl)
lbl_2.place(x=10,y=55)
entry_2.place(x=80,y=55)
btn2.place(x=388,y=51)

lbl_3=Label(root,text='Select Key : ')
lbl_3a=Label(root,text='Select File : ')
entry_3=Entry(root,textvariable=key_file,width=50) 
btn3= Button(root,text='..',command=select_key)
entry_3a=Entry(root,textvariable=decr_file,width=50) 
btn3a= Button(root,text='..',command=select_fyl2)

lbl_3.place(x=10,y=150)
lbl_3a.place(x=10,y=190)
entry_3.place(x=80,y=150)
entry_3a.place(x=80,y=190)
btn3.place(x=388,y=150)
btn3a.place(x=388,y=190)



btn = Button(root,text='Encrypt',command=encrt1)
btn.place(x=220,y=90)

btn = Button(root,text='Decrypt',command=decrypt1)
btn.place(x=220,y=250)


mainloop()