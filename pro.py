# pdf to image 
# image to pdf
# pdf compress
# docx to pdf 
# docx to image

from cProfile import label
from cmath import exp
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from tkinter import font
# import ttk 
from tkinter.ttk import *
from tkinter import messagebox
from turtle import left
from PIL import Image
from pdf2image import convert_from_path
import img2pdf
import random
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet
from docx2pdf import convert
import time

# create root window
root = Tk()
root.title("Welcome to govt. form filler")
root.geometry('660x350')
root.resizable(False,False)


#------------------------Variables
Img_x=tk.StringVar()
Img_y=tk.StringVar()
Img_qual= tk.StringVar()
Img_qual_inc= tk.StringVar()
Img_ext= tk.StringVar()
global img_file
global img_file_name
global img_ext
img_file_name=0
# img7=PhotoImage(file = r"bb2.png")
#-------------------------All Functions here

def defalt():
    global img_file_name
    reset_btn.configure(style='BW2.TLabel')
    messagebox.showinfo('showinfo',"Done")
    Img_x.set('') 
    Img_y.set('')
    Img_qual.set('')
    Img_qual_inc.set('')
    img_file_name=0
    lbl_5_ae.config(state='normal')
    lbl_4_ae.config(state='normal')
    lbl_2_disc.config(text='(Not Selected)')
    reset_btn.configure(style='BW.TLabel')

def callback(input):
	
    if input.isdigit():
        
        if int(input)<=95 and int(input)>=1:
            lbl_5_ae.config(state='disabled')
            return True
        else:
            return False					
    elif input == "":
        lbl_5_ae.config(state='normal')
        return True
    else:
        return False

def callback2(input):
	
    if input.isdigit():
        
        if int(input)<=90 and int(input)>=1:
            lbl_4_ae.config(state='disabled')
            return True
        else:
            return False					
    elif input == "":
        lbl_4_ae.config(state='normal')
        return True
    else:
        return False

def callback3(input):
	
    if input.isdigit():
        
        if int(input)<=2000 and int(input)>=1:
            # lbl_4_ae.config(state='disabled')
            return True
        else:
            return False					
    elif input == "":
        # lbl_4_ae.config(state='normal')
        return True
    else:
        return False



def Img_file_open():
    global img_file
    global img_file_name
    btn_imgfileopen.configure(style='BW2.TLabel')
    img_file_name = filedialog.askopenfilename( filetypes =[('Image Files', ' *.jpg .jpeg .JPEG .PNG .WebP'),('All Files', '*.*')])

    try:
        img_file= Image.open(img_file_name)
        # img_file.show()
        img_file_name=os.path.basename(img_file_name)
        img_file_name=os.path.splitext(img_file_name)[0]
        # print(img_file_name)
        lbl_2_disc.config(text='File : '+ img_file_name)
    except:
         messagebox.showwarning("showwarning", "No File Selected ")
         img_file_name=0
    btn_imgfileopen.configure(style='BW.TLabel')

def Img_file_rescom(l,b):
    # print("--------------------Inside Resize func ----------------------- ")
    global img_file
    # cwd=os.getcwd()
    img_file=img_file.resize((int(l),int(b)))
    # img_file=iml

# def Img_file_compr(q):
#     global img_file
#     img_file.save("Compressed_"+img_file,"JPEG",optimize = False,quality = int(q))
#     # iml=
# print('--'+Img_x.get()+'--')


def save_file(q,q1):

    save_btn.configure(style='BW2.TLabel')
    if q1!='':q1= int(q1)+100
    if q!='':q= 91-int(q)
    # files = [('Image Files', '*.jpg .JPEG')]
    # file = asksaveasfile(filetypes = files, defaultextension = files)

    if img_file_name==0:
        # print(" no image file selected ")
        messagebox.showwarning("showwarning", "No Image Selected")
        save_btn.configure(style='BW.TLabel')
        return
    
    if Img_x.get()=='' and Img_qual.get()==''and Img_qual_inc.get()=='':
        messagebox.showwarning("showwarning", "No Values Entered")
        save_btn.configure(style='BW.TLabel')
        return
    
    elif Img_x.get()!='' and Img_qual.get()==''and Img_qual_inc.get()=='':
        Img_file_rescom(Img_x.get(),Img_y.get())
        img_file.save("Resized_"+img_file_name+'.'+Img_ext.get(),Img_ext.get())

    elif Img_x.get()!='' and Img_qual.get()==''and Img_qual_inc.get()!='':
        Img_file_rescom(Img_x.get(),Img_y.get())
        img_file.save("Resized_Increased_"+img_file_name+'.'+Img_ext.get(),Img_ext.get(),optimize = True,quality = int(q1))

    elif Img_x.get()=='' and Img_qual.get()!='':
        img_file.save("Compressed_"+img_file_name+'.'+Img_ext.get(),Img_ext.get(),optimize = True,quality = int(q))

    elif Img_x.get()=='' and Img_qual_inc.get()!='':
        img_file.save("Increased_"+img_file_name+'.'+Img_ext.get(),Img_ext.get(),optimize = True,quality = int(q1))

    else:
        Img_file_rescom(Img_x.get(),Img_y.get())
        img_file.save("Resized_Compressed_"+img_file_name+'.'+Img_ext.get(),Img_ext.get(),optimize = True,quality = int(q))
        # print("last else "+Img_x.get()+Img_qual.get())
        defalt()
        save_btn.configure(style='BW.TLabel')
        return
    save_btn.configure(style='BW.TLabel')
    defalt()
    




##---------------------------------Second window---------------------

def pdf2img():
    lbl_8b.configure(style='BW2.TLabel')
    li=[i for i in range(1,100)]
    img_file_name = filedialog.askopenfilename( filetypes =[('Document Files', ' *.pdf'),('All Files', '*.*')])
    try:
        images = convert_from_path(img_file_name)   #str(e1.get())
        for img in images:
            print('ko')
            img.save('output'+str(li.pop(0))+'.jpg', 'JPEG')
        lbl_8b.configure(style='BW.TLabel')
    except:
            messagebox.showerror('Result','no file selected')
            lbl_8b.configure(style='BW.TLabel')



def image2pdf():

    lbl_8c.configure(style='BW2.TLabel')
    try:
        img_file_name = filedialog.askopenfilenames( filetypes =[('Image Files', ' *.jpg .jpeg .JPEG .PNG .WebP'),('All Files', '*.*')])
        if(img_file_name==''):
            lbl_8c.configure(style='BW.TLabel')
            return
        print(type(img_file_name))
        with open(f"imgtopdf_file.pdf","wb") as f:
            f.write(img2pdf.convert(img_file_name))
        lbl_8c.configure(style='BW.TLabel')
        messagebox.showinfo("Result", 'img to pdf file created')
    except:
            messagebox.showinfo("Result", 'no image selected')
            lbl_8c.configure(style='BW.TLabel')
    
def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_pdf():#input_file: str, output_file: str):
    lbl_8d.configure(style='BW2.TLabel')
    PDFNet.Initialize("demo:1649858903893:7bd5aaea0300000000d59d055f87f723ea0078ee528a2030cf813a8475")
    """Compress PDF file"""
    # try:
    input_file = filedialog.askopenfilename( filetypes =[('Document Files', ' *.pdf'),('All Files', '*.*')])
    if(input_file==''):
        lbl_8d.configure(style='BW.TLabel')          
        return False
    progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
    progress.pack(padx=40,pady = 120)
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
  
    # except AttributeError:
    #     print("no file selected") 

    # input_file = r'big1.pdf'
    output_file = 'compressed'+str(random.randint(0,9999))+'.pdf'
    if not output_file:
        output_file = input_file
        print("----------------------out = in")
    
    try:
        initial_size = os.path.getsize(input_file)
        # Initialize the library
        PDFNet.Initialize()
        doc = PDFDoc(input_file)
        # Optimize PDF with the default settings
        doc.InitSecurityHandler()
        progress['value'] = 40
        root.update_idletasks()
        time.sleep(1)
        # Reduce PDF size by removing redundant information and compressing data streams
        Optimizer.Optimize(doc)
        progress['value'] = 60
        root.update_idletasks()
        time.sleep(1)
        doc.Save(output_file, SDFDoc.e_linearized)
        doc.Close()
        progress['value'] = 80
        root.update_idletasks()
        time.sleep(1)
    except Exception as e:
        lbl_8d.configure(style='BW.TLabel')
        print("Error compress_file=", e)
        # doc.Close()
        return False
        
    compressed_size = os.path.getsize(output_file)
    ratio = 1 - (compressed_size / initial_size)
    summary = {
         "Initial Size": get_size_format(initial_size),
        "Output File": output_file, f"Compressed Size": get_size_format(compressed_size),
        "Compression Ratio": "{0:.3%}.".format(ratio)
    }
    progress['value'] = 100
    progress.destroy()
    lbl_8d.configure(style='BW.TLabel')
    messagebox.showinfo("Result","\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    # Printing Summary
    # print("## Summary ########################################################")
    # print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    # print("###################################################################")
    # root.deiconify()
    return True

def doc_topdf():
    try:
        docfile_name = filedialog.askopenfilename( filetypes =[('Document Files', ' *.docx .doc'),('All Files', '*.*')])
        convert(docfile_name)
    except:
            messagebox.showinfo('showinfo',"Error occured")




def part2():
    root.withdraw()
    os.system(r'python pass_gen.py')
    root.deiconify()

    
#--------------------------icon / img filees
img0=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Increased_imz2a.png')
img1=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_pdf.png')
img2=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_crop-tool.png')
img3=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_iz3.png')
img4=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_iz42.png')
img5=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_res.png')
img6=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_save.png')
img7=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_reset.png')
img8=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_folder.png')
img9=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_pass_icon.png')
img10=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_imz89.png')
img11=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_encry.png')
img12=PhotoImage(file =r'C:\Users\D\Documents\code\python\project_1\icons\Resized_cloud-database.png')



#--------------------------styles/ 
bg_1='#7ed2dc'
# bg_2='#39c0ca'
bg_2='#28a2b7'
style = ttk.Style()
style2 = ttk.Style()
style2.configure("BW2.TLabel", background=bg_2)
style.configure("BW.TLabel", background=bg_1,foreground='black')
font1=('calibre',11,'normal')


# -----------------------all widgets will be here 
lbl_1b=Label(root,image=img0)
lbl_1=Label(root,text='Image Resize/Compress',background=bg_1,font = ('calibre',13,'bold'))
lbl_head2=Label(root,text='Other Features',background=bg_1,font = ('calibre',13,'bold'))

lbl_2=Label(root,text='Select Image',background=bg_1,font =font1)

btn_imgfileopen= Button(root,text='Open file',image=img8,style='BW.TLabel',command=Img_file_open)
# lbl_2_img=Label(root,image=img8,style='BW.TLabel')
lbl_2_disc = Label(root,text='(Not Selected)',background=bg_1,font =font1)

lbl_3=Label(root,text='Resize Image',background=bg_1,font =font1)
lbl_3_x=Label(root,text='X',background=bg_1,font =font1)
lbl_3_y=Label(root,text='Y',background=bg_1,font =font1)
lbl_3_xe=Entry(root,textvariable=Img_x,width=4,font = ('calibre',10,'normal'))
lbl_3_ye=Entry(root,textvariable=Img_y,width=4 ,font = ('calibre',10,'normal'))
lbl_3_img=Label(root,image=img5,style='BW.TLabel')

lbl_4=Label(root,text='Compress Image',style='BW.TLabel',font =font1)
lbl_4_a=Label(root,text='Percent(1 to 90)',style='BW.TLabel',font =font1)
lbl_4_ae=Entry(root,textvariable=Img_qual,width=3)

lbl_5=Label(root,text="Increse Image Size",style='BW.TLabel',font =font1)
lbl_5_a=Label(root,text='Percent(1 to 90)',style='BW.TLabel',font =font1)
lbl_5_ae=Entry(root,textvariable=Img_qual_inc,width=3)

lbl_7=Label(root,text='Select Extension',style='BW.TLabel',font =font1)
lbl_7_ex=ttk.Combobox(root,width=12,textvariable=Img_ext)
lbl_7_ex['values'] = ['JPEG','jpg','PNG','WebP']
lbl_7_ex['state'] = 'readonly'
lbl_7_ex.current(0)

save_btn=Button(root,text='save',image=img6,style='BW.TLabel',command=lambda:save_file(Img_qual.get(),Img_qual_inc.get()))
reset_btn=Button(root,text='reset',image=img7,style='BW.TLabel',command=defalt)

lbl_8= Button(root,text="Crop Image",style='BW.TLabel',image=img2,compound= TOP,command= lambda:os.system(r'python crop.py'))
lbl_8b=Button(root,text='Pdf2img',style='BW.TLabel',image=img3,compound=TOP,command=pdf2img)
lbl_8c=Button(root,image=img1,text='img2pdf',style='BW.TLabel',compound=TOP,command=image2pdf)
lbl_8d=Button(root,text='Compress pdf',style='BW.TLabel',image=img4,compound=TOP,command=compress_pdf)
lbl_8e=Button(root,text='Pass Gen',style='BW.TLabel',image=img9,compound=TOP,command=part2) #lambda:os.system(r'python crop.py')
lbl_8f=Button(root,text='Docx2pdf',style='BW.TLabel',image=img10,compound=TOP,command=doc_topdf)
lbl_8g=Button(root,text='Encryption',style='BW.TLabel',image=img11,compound=TOP,
            command=lambda:os.system(r'python encryptin.py'))
lbl_8h=Button(root,text='Database',style='BW.TLabel',image=img12,compound=TOP,
            command=lambda:os.system(r'python signup_page.py'))


#---------------------------------widgets placement
lbl_1.place(x=120,y=3)
lbl_head2.place(x=450,y=3)
lbl_1b.place(x=0,y=0)

lbl_2.place(x=3,y=40)
btn_imgfileopen.place(x=212,y=35)
# lbl_2_img.place(x=280,y=35)
lbl_2_disc.place(x=250,y=35)

lbl_3.place(x=3,y=85) 
lbl_3_x.place(x=210,y=80)
lbl_3_y.place(x=276,y=80) 
lbl_3_xe.place(x=223,y=80)
lbl_3_ye.place(x=288,y=80)
lbl_3_img.place(x=330,y=70)

lbl_4.place(x=3,y=130)
lbl_4_a.place(x=210,y=130) 
lbl_4_ae.place(x=325,y=128) 

lbl_5.place(x=3,y=180)
lbl_5_a.place(x=210,y=180) 
lbl_5_ae.place(x=325,y=180)

lbl_7.place(x=3,y=230)
lbl_7_ex.place(x=215,y=230)

save_btn.place(x=220,y=265)
reset_btn.place(x=120,y=280)

lbl_8.place(x=444,y=59) 
lbl_8b.place(x=450,y=130)
lbl_8c.place(x=450,y=200) 
lbl_8d.place(x=440,y=290) 
lbl_8e.place(x=540,y=59)
lbl_8f.place(x=540,y=120)
lbl_8g.place(x=540,y=220)
lbl_8h.place(x=540,y=300)

# e = Entry(root)
# e.place(x = 50, y = 50)
reg = root.register(callback)
reg2 = root.register(callback2)
reg3 = root.register(callback3)
lbl_4_ae.config(validate ="key",validatecommand =(reg,'%P'))
lbl_5_ae.config(validate ="key",validatecommand =(reg2,'%P'))
lbl_3_xe.config(validate ="key",validatecommand =(reg3,'%P'))
lbl_3_ye.config(validate ="key",validatecommand =(reg3,'%P'))


root.mainloop()
