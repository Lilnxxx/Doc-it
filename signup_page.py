# from email.mime import image
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from joblib import PrintTime
import mysql.connector
# import mysqlx
import os
# import credentials as cr
global id_entered
id_entered=0
class SignUp:
    def __init__(self, root):
        # self.new_changed_pass()
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("900x620+0+0")
        self.bg_color="#Ff004a"            #Ff0076"  ,3b 3a                     #0085a2'

        self.window.config(bg = self.bg_color)
        self.logn_id=0
        # self.bg_color= '#00a6ca'

        self.bg_img = ImageTk.PhotoImage(file="Images/pic4.jpg")
        self.fram1_img = ImageTk.PhotoImage(file="Images/photo10.jpg")

        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.window, bg=self.bg_color)
        frame.place(x=430,y=40,width=450,height=550)

        # labl_frm = Label(frame,image=self.bg_img)
        # labl_frm.place(x=0,y=0)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25),bg=self.bg_color,fg='white').place(x=20, y=10)
        # title2 = Label(frame, text="Join with us", font=("times new roman",13),bg=self.bg_color, fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="Name", font=("helvetica",15),bg=self.bg_color).place(x=20, y=100)
        l_name = Label(frame, text="Login Id", font=("helvetica",15),bg=self.bg_color).place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica",15),bg=self.bg_color).place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("helvetica",15),bg=self.bg_color).place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("helvetica",15),bg=self.bg_color).place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="Password", font=("helvetica",15),bg=self.bg_color).place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        re_password =  Label(frame, text="Re-enter Password", font=("helvetica",15),bg=self.bg_color).place(x=20, y=410)

        self.re_password_txt = Entry(frame,font=("arial"))
        self.re_password_txt.place(x=20, y=440, width=420)

        self.terms = IntVar()
        # terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg=self.bg_color,font=("times new roman",12)).place(x=20,y=420)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg='white').place(x=92,y=495,width=250)



        # -------------------------------- Sign in ---------------------------
        # -------------------------------- Sign in ---------------------------



        frame2 = Frame(self.window, bg=self.bg_color)
        frame2.place(x=20,y=160,width=370,height=320)

        title_2 = Label(frame2, text="Log In", font=("times new roman",25),bg=self.bg_color,fg='white')
        title_2.place(x=20, y=10)

        lgid = Label(frame2, text="ID", font=("helvetica",15),bg=self.bg_color)
        lgid.place(x=20, y=100)
        
        self.id_entry = Entry(frame2,font=("arial"))
        self.id_entry.place(x=20, y=130, width=250)
    
        lgpass = Label(frame2, text="Password", font=("helvetica",15),bg=self.bg_color)
        lgpass.place(x=20, y=180)
        
        self.pass_entry = Entry(frame2,font=("arial"))
        self.pass_entry.place(x=20, y=210, width=250)

        self.log_in = Button(frame2,text="Log In",command=self.login_f,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg='white')
        self.log_in.place(x=15,y=270,width=140)

        self.log_in = Button(frame2,text="Forgot Password",command=self.reset_pass,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg='white')
        self.log_in.place(x=170,y=270,width=190)

#----------------------------------Forgot Password window----------------------------------
    def reset_pass(self):   
        # print('reset password win activated')
        # root.withdraw()
        self.top = Toplevel()
        self.top.geometry("400x330")
        self.top.title("toplevel")
        self.top.grab_set()
        self.top.resizable(False,False)
        # self.top.protocol('WM_DELETE_WINDOW',(root.deiconify,self.top.destroy))

        self.l1 = Label(self.top,text='Enter your login id ', font=("helvetica",15))
        self.l1.place(x=5,y=5)

        self.e1 = Entry(self.top)
        self.e1.place(x=5, y=45, width=100)

        re_sec_question = Label(self.top, text="Security questions", font=("helvetica",15))
        re_sec_question.place(x=5, y=90)
        re_answer = Label(self.top, text="Answer", font=("helvetica",15))
        re_answer.place(x=240, y=90)

        self.e2 = Entry(self.top)
        self.e2.place(x=240, y=130, width=100)
        
        self.questions2 = ttk.Combobox(self.top,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions2['values'] = ("What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions2.place(x=0,y=130,width=200)
        self.questions2.current(0)

        l3 = Label(self.top,text='Enter your email id ', font=("helvetica",15))
        l3.place(x=5,y=180)
        self.e3 = Entry(self.top)
        self.e3.place(x=5, y=225, width=150)

        self.log_in = Button(self.top,text="Confirm",command=self.reset_pass_button,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg='white')
        self.log_in.place(x=125,y=270,width=140)

#----------------------------------Sign up  window----------------------------------
    def signup_func(self):
     
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        # elif self.terms.get() == 0:
        #     messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
                cur=mysqldb.cursor()                
                # cur = connection.cursor()
                # e_mail=list(self.email_txt.get())
                cur.execute("SELECT * FROM registation WHERE email=%s",(self.email_txt.get(),))
                row=cur.fetchall()
                cur.execute("SELECT * FROM registation WHERE lastname=%s",(self.lname_txt.get(),))
                row1=cur.fetchall()
                print(row,type(row))
                # Check if th entered email id is already exists or not.
                if row!=[]:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                elif row1!=[]:
                    messagebox.showerror("Error!","The login id is taken, Try again with another login id",parent=self.window)
                elif self.password_txt.get() != self.re_password_txt.get():
                     messagebox.showerror("Error!","Passwords Do not match ",parent=self.window)
                     return

                else:
                    cur.execute("insert into registation (firstname,lastname,email,sec_ques,answer,pass) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.questions.get(),
                                        self.answer_txt.get(),
                                        self.password_txt.get()
                                    ))
                    # mysqldb.commit()
                    # cur.execute("select * from registation order by lastname ASC")
                    mysqldb.commit()
                    mysqldb.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
            except Exception as e:
                # print(type(self.email_txt.get()),type(e_mail))
                # print('last error',self.email_txt.get())
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

#----------------------------------Reset all fields ----------------------------------
    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)
        self.re_password_txt.delete(0, END)
        self.id_entry.delete(0,END)
        self.pass_entry.delete(0,END)
        # self.e1.delete(0, END)
        # self.e2.delete(0, END)
        # self.e3.delete(0, END)
        # self.questions2.delete(0, END)

#----------------------------------Login  window----------------------------------
    def login_f(self):
        
        if self.id_entry.get()=="" or self.pass_entry.get()=="" :
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

                # elif self.terms.get() == 0:
                #     messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
                cur=mysqldb.cursor()                
                # cur = connection.cursor()
                # e_mail=list(self.email_txt.get())
                cur.execute("SELECT * FROM registation WHERE lastname=%s",(self.id_entry.get(),))
                row=cur.fetchall()
                # cur.execute("SELECT * FROM registation WHERE pass=%s",(self.password_txt.get(),))
                # row1=cur.fetchall()
                # print(row,type(row))
                # Check if th entered email id is already exists or not.
                if row==None:
                    print('1st')
                    messagebox.showerror("Error!","Id/Password is Incorrect",parent=self.window)
                    return
                else:
                    for i in row:
                        print(i[5])
                        if i[5]==self.pass_entry.get():
                            messagebox.showinfo("Login Successfull ! "," logged in",parent=self.window)
                            mysqldb.close()
                            f = open("myfile.txt", "w")
                            f.write(self.id_entry.get())
                            f.close()
                            # messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                            # self.reset_fields()
                            root.destroy()
                            os.system(r'python record-delete.py')
                            # root.destroy()
                            return
                    messagebox.showerror("Error!","Id/Password is Incorrect",parent=self.window)
                    return
                # else:
                #     messagebox.showinfo("Login Successfull ! "," logged in",parent=self.window)
                #     mysqldb.close()
                #     # messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                #     self.reset_fields()
            except Exception as e:
                # print(type(self.email_txt.get()),type(e_mail))
                # print('last error',self.email_txt.get())
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

#----------------------------------Forgot Pass Reset Password check button----------------------------------
    def reset_pass_button(self):
        # self.new_changed_pass()
        if self.e1.get()=="" or self.e2.get()=="" or self.e3.get()==""  or self.questions2.get()==""  :
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)


        else:
            try:
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
                cur=mysqldb.cursor()                
           
                cur.execute("SELECT * FROM registation WHERE lastname=%s",(self.e1.get(),))
                row=cur.fetchall()
                if row==None:
                    print('1st')
                    messagebox.showerror("Error!","Id is Incorrect",parent=self.window)

                    return
                else:
                    for i in row:
                        # print(i[5])
                        if i[2]==self.e3.get() and i[3]==self.questions2.get() and i[4]==self.e2.get():                            
                            # messagebox.showinfo("Reset Successfull ! "," reset ",parent=self.window)
                            mysqldb.close()
                            self.logn_id=self.e1.get()
                            # self.reset_fields()
                            self.new_changed_pass()     
                            # self.top.destroy()
                            return
                    messagebox.showerror("Error!","Id/Password is Incorrect",parent=self.window)
                    self.reset_fields()
                    return
              
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
                

#----------------------------------Reset Password/ change passsword Window----------------------------------
    def new_changed_pass(self):
        self.top2 = Toplevel()
        self.top2.geometry("400x130")
        self.top2.title("toplevel")
        self.top2.grab_set()
        self.top2.resizable(False,False)

        self.new_pass=Label(self.top2,text='New Password')
        self.new_pass.place(x=5,y=5)

        self.new_pass_entry=Entry(self.top2)
        self.new_pass_entry.place(x=180,y=5,width=160)

        self.re_new_pass=Label(self.top2,text=' Re-enter New Password')
        self.re_new_pass.place(x=5,y=30)

        self.re_new_pass_entry=Entry(self.top2)
        self.re_new_pass_entry.place(x=180,y=30,width=160)

        self.change_pass = Button(self.top2,text="Reset",command=self.ncp_button,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg='white')
        self.change_pass.place(x=130,y=65,width=140)

    def ncp_button(self):
        print(self.e1.get())
        print(self.new_pass_entry.get())

        if self.new_pass_entry.get()=="" or self.re_new_pass_entry.get()==""  :
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        elif self.new_pass_entry.get() != self.re_new_pass_entry.get():
            messagebox.showerror("Error!","Passwords must be same",parent=self.window)
        else:
            try:
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysql828",database="payroll")
                cur=mysqldb.cursor()                
           
                cur.execute("UPDATE registation SET pass = %s WHERE lastname =%s",(self.new_pass_entry.get(),self.e1.get(),))
                
                row=cur.fetchall()
                print(row)
                mysqldb.commit()

                mysqldb.close()
                messagebox.showinfo("Reset Successfull ! "," Password has been changed ",parent=self.window)
                self.top.destroy()
                self.top2.destroy()
                # if row==None:
                #     print('1st')
                #     messagebox.showerror("Error!","Id is Incorrect",parent=self.window)

                #     return
                # else:
                #    pass
              
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
             

# def id_get():
#     global id_entered
#     return id_entered

if __name__ == "__main__":
    root = Tk()
    # root.geometry('300x200')
    root.resizable(False,False)
    obj = SignUp(root)
    root.mainloop()
