from cgitb import text
from tkinter import *
from tkinter import messagebox
import os
from tkinter import filedialog
from PIL import ImageTk,Image
trace = 0 
global li
li = []

class CanvasEventsDemo: 
    # a=0
    # b=0
    def __init__(self, parent=None):
        self.a=0
        self.b=0
        global img_file_name
        global img
        global img2
        global canvas
        
        try:
            img_file_name = filedialog.askopenfilename( filetypes =[('Image Files', ' *.jpg .jpeg'),('All Files', '*.*')])
        except AttributeError:
            print("no file selected")

        img_file0= Image.open(img_file_name)  
        x= img_file0.width
        y=img_file0.height
        print('x= ',x,' y= ',y)
        canvas = Canvas(root,cursor='cross',width=x,height=y,bg='beige') 
        if img_file_name==():
            messagebox.showwarning("showwarning", "No file selected")
            # exit('no file selected')
            return False
            
        print(img_file_name,'jikik')
        img = ImageTk.PhotoImage(Image.open(img_file_name))  
        img2 = Image.open(img_file_name)
        img_file_name=os.path.basename(img_file_name)
        img_file_name=os.path.splitext(img_file_name)[0]
        canvas.create_image(0,0, anchor=NW,image=img)
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart) 
        canvas.bind('<ButtonRelease-1>',self.onrel)
        canvas.bind('<B1-Motion>',     self.onGrow)  
        # canvas.bind('<Double-1>',      self.onClear) 
        canvas.bind('<ButtonPress-3>', self.onMove)  
        # self.canvas = canvas
        self.drawn  = None
        # self.kinds = [ canvas.create_rectangle]
    def onrel(self, event):
        global li
        # print('button released')
        canvas.unbind('<ButtonPress-1>')
        # self.start=None
        li.append((self.start.x,self.start.y))
        self.start.x=li[-2][0]
        self.start.y=li[-2][-1]
        print(li[-1][0],li[-1][-1])
        # print(li)
        return

    def onStart(self, event):
        # print('in on start ')
        self.shape = canvas.create_rectangle
        # self.kinds = self.kinds[1:] + self.kinds[:1] 
        self.start = event
        print("on mouse click start --",self.start)
        self.drawn = None
    
    def onGrow(self, event):
                               
        canvas = event.widget
        if self.drawn: 
            canvas.delete(self.drawn)

            # return

        objectId = self.shape(self.start.x, self.start.y, event.x, event.y
        ,outline='light green',width='3')
        li.append((event.x,event.y))
        self.a= event.x
        self.b = event.y
        self.drawn = objectId

    def crop(self):
        global li
        print('\nevent ',li[0][0],li[0][1],' self a b ',self.a,self.b)
        
        if self.a==0: 
            messagebox.showwarning("showwarning", "Area not selected")
            return
       

        if li[0][0]>self.a and li[0][1]>self.b: #left 2
            print('2nd quad')
            jk= img2.crop((self.a,self.b,li[-1][0],li[-1][-1]))
            
        
        elif li[0][0]<self.a and li[0][1]<self.b:  #right 4  
            print('4th quad')
            jk= img2.crop((li[-1][0],li[-1][-1],self.a,self.b))
        
        elif li[0][0]<self.a and li[0][1]>self.b:
            print('1st quad ')
            jk= img2.crop((li[-1][0],self.b,self.a,li[-1][-1]))
        else:
            print('---333333333------------------- value error recorded ')
            jk= img2.crop((self.a,li[-1][-1],li[-1][0],self.b))
            
        # jk.show(title='cropped_img43')
        jk.save("Cropped_"+img_file_name+'.JPEG')
        print(li[0][0])
        li=[]
        exit()
    def onMove(self, event):
        global li
        li=[]



if __name__ == '__main__':
    root =Tk()
    # root.resizable(False,False)
    try:
        h=CanvasEventsDemo()
    except:
        exit()
    btn = Button(root,text='crop',command=h.crop)
    btn.pack()
    mainloop()


# from tkinter import *
# from PIL import ImageTk,Image

# root =Tk()
# root.resizable(False,False)


# canv = Canvas(root,cursor='cross',width=300,height=224)

# canv.pack()
# img = ImageTk.PhotoImage(Image.open("dog_ani.jpeg"))  
# canv.create_image(0,0, anchor=NW,image=img)

# mainloop()








# import PIL.Image
# # import Image
# # import ImageTk
# from PIL import ImageTk
# from tkinter import *    
# # import tkinter as tk

# class ExampleApp(Frame):
#     def __init__(self,master):
#         Frame.__init__(self,master=None)
#         self.x = self.y = 0
#         self.canvas = Canvas(self,  cursor="cross")

#         # self.sbarv=Scrollbar(self,orient=VERTICAL)
#         # self.sbarh=Scrollbar(self,orient=HORIZONTAL)
#         # self.sbarv.config(command=self.canvas.yview)
#         # self.sbarh.config(command=self.canvas.xview)

#         # self.canvas.config(yscrollcommand=self.sbarv.set)
#         # self.canvas.config(xscrollcommand=self.sbarh.set)

#         self.canvas.grid(row=0,column=0,sticky=N+S+E+W)
#         # self.sbarv.grid(row=0,column=1,stick=N+S)
#         # self.sbarh.grid(row=1,column=0,sticky=E+W)

#         self.canvas.bind("<ButtonPress-1>", self.on_button_press)
#         self.canvas.bind("<B1-Motion>", self.on_move_press)
#         self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

#         self.rect = None

#         self.start_x = None
#         self.start_y = None

#         self.im = PIL.Image.open("dog_ani.jpeg")
#         self.wazil,self.lard=self.im.size
#         # self.canvas.config(scrollregion=(0,0,self.wazil,self.lard))
#         self.tk_im = ImageTk.PhotoImage(self.im)
#         self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)   


#     def on_button_press(self, event):
#         # save mouse drag start position
#         self.start_x = self.canvas.canvasx(event.x)
#         self.start_y = self.canvas.canvasy(event.y)

#         # create rectangle if not yet exist
#         if not self.rect:
#             self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

#     def on_move_press(self, event):
#         curX = self.canvas.canvasx(event.x)
#         curY = self.canvas.canvasy(event.y)

#         w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
#         if event.x > 0.9*w:
#             self.canvas.xview_scroll(1, 'units') 
#         elif event.x < 0.1*w:
#             self.canvas.xview_scroll(-1, 'units')
#         if event.y > 0.9*h:
#             self.canvas.yview_scroll(1, 'units') 
#         elif event.y < 0.1*h:
#             self.canvas.yview_scroll(-1, 'units')

#         # expand rectangle as you drag the mouse
#         self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)    

#     def on_button_release(self, event):
#         pass    

# if __name__ == "__main__":
#     root=Tk()
#     root.geometry('300x300')
#     app = ExampleApp(root)
#     app.pack()
#     root.mainloop()
