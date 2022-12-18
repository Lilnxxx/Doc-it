import string
import random

from bs4.element import Comment
import requests
from bs4 import BeautifulSoup
from tkinter import*
#from tkinter.ttk import*
from tkinter.font import BOLD


root = Tk()
root.geometry('775x482')
root.config(bg='#72C6E9')
#root.overrideredirect(True)
root.resizable(FALSE,FALSE)
root.title('Password Generator')

pass_len = DoubleVar()
#pass_len2 = DoubleVar()
chkbtn_sta= StringVar() 
chkbtn_sta2= StringVar() 
chkbtn_sta3= StringVar() 
chkbtn_sta4= StringVar() 
chkbtn_sta5= StringVar() 
pessw = StringVar()

chkbtn_sta.set('(Selected)')
chkbtn_sta2.set('(Selected)')
chkbtn_sta3.set('(Selected)')
chkbtn_sta4.set('(Selected)')
chkbtn_sta5.set('(Selected)')


def calculation(a,b,c,d):

    vari=int(4)
    t1.delete("1.0", "end")
    lent=pass_len.get()
    c=int(7)
    if chkbtn_sta.get()=='(Not Selected)':
        #a=0
        vari=vari-1
        c=0
        

    if chkbtn_sta4.get()=='(Not Selected)':
        #a=0
        vari=vari-1
        d=0
        

    a=int(lent/vari)

    if c==d:
        b=a
        if lent%2!=0:
            a=a+1

    elif lent%vari==0:
        b=a
        if c==0:
            d=a
        elif d==0:
            c=a
        else:
            d=c=a
    
    elif lent%vari==1:
        b=a
        if c==0:
            d=a
        elif d==0:
            c=a
        else:
            d=c=a
        a=a+1
    
    elif vari >=3 and lent%vari==2:
        if c==0:
            d=a
        elif d==0:
            c=a
        else:
            d=c=a
        b=a=a+1
    
    elif vari >= 4 and lent%vari==3:
        d=a
        b=c=a=a+1


    #print(a," ",b," ",c," ",d,' ',pass_len.get())
    s1= list(string.ascii_uppercase)
    random.shuffle(s1)
    #print(s1)
    password = ''.join(s1[0:a])

    s2 = list(string.ascii_lowercase)
    random.shuffle(s2)
    #print(s2)
    password = password+''.join(s2[0:b])

    s3 = list(string.digits)
    random.shuffle(s3)
    password = password+''.join(s3[0:d])

    s4 = list(string.punctuation)
    random.shuffle(s4)
    password = password+''.join(s4[0:c])


    password= list(password)
    random.shuffle(password)

    password=''.join(password)
    #print('\n',password)
    global pessw
    pessw = password
    t1.insert(END,password)
    Font_tuple = ("Consolas", 17, "bold")
  
    t1.configure(font = Font_tuple)
    t1.place(x=390,y=425)





def win2():
    global pass_len
    print('2nd window is active')
    root.destroy()
    cl0=0
    win2= Tk()
    win2.geometry('575x382')
    win2.config(bg='#72C6E9')
    #root.overrideredirect(True)
    #win2.resizable(FALSE,FALSE)
    win2.title('Password Generator')
    
    title = Label(win2,bg='#72C6E9',text='Note: This Generator generates passwords which are much easier\n to remember than the other one',font=('consolas',13)).place(x=0)

    l2= Label(win2,text='Choose the length of your password',font=('consolas',12,BOLD),bg='#72C6E9')
    l2.place(x=5,y=60)

    sca2 = Scale(win2,highlightbackground='#72C6E9',sliderlength=15,length=180,variable=cl0,from_=8 ,to =25,showvalue=1, orient=HORIZONTAL,bg='#72C6E9',bd=0,troughcolor='#0047b3')
    sca2.place(x=340,y=44)
    

    pass_gen_button = Button(win2,bg='RED',fg='white',text='Generate',activebackground='yellow',font=('consolas',22))
    t11= Text(win2,height=1.7,width=17)

    

    def calc2():
        b=a=c=int(0)
        lent=sca2.get()
        lent = int(lent)
        
        a=int(lent/2)
        lent=lent-a-1
        if lent%2==0:
            c=b=int(lent/2)
        else:
            c=int(lent/2)
            b=c+1
        lent=sca2.get()
        print(sca2.get(),' -- ',a,' -- ',b,' -- ',c)
        
        t11.delete("1.0", "end")
        
        url2='https://www.thefreedictionary.com/words-that-start-with-'
        x= list(string.ascii_uppercase)
        random.shuffle(x)
        x= ''.join(x[:1])
        url=url2+x

        r= requests.get(url)
        html_content = r.content

        soup = BeautifulSoup(html_content,'html.parser')
        
        all_links = set()

        anc = soup.find_all('a')
        for link in anc:#[300:400]:
            if link!='#':
                all_links.add(link.get('href'))
        
        save_tupple= set()
        
        all_links = tuple(all_links)
        for trav in all_links:
            if trav:
                if(len(trav))==a:
                    save_tupple.add(trav)
        #print(len(all_links),'\n')

        save_tupple=tuple(save_tupple)
        pass1=save_tupple[random.randint(0,len(save_tupple))]
        

        st1= list(string.ascii_uppercase)
        random.shuffle(st1)
        
        pass1= pass1.capitalize()
        pass1 = pass1+''.join(st1[0:1])
        

        st1= list(string.digits)
        random.shuffle(st1)
        pass2 = ''.join(st1[0:b])

        st1= list('!#$%&()*+/<=>?@[\]')
        random.shuffle(st1)
        pass2 = pass2+''.join(st1[0:c])
        pass2= list(pass2)
        random.shuffle(pass2)
        pass2 ="".join(pass2)
        lent=b+c

        jig = random.randint(1,lent)
        substring = pass2[0:jig]
        print(jig)
        if jig!=4:
            substring2=pass2[jig:lent]
            pass1= substring+pass1+substring2
        else:
            pass1= substring+pass1
        print(pass1)
        # print('jig 1 ',substring)
        # print('final password --> ',pass1)
        #return pass1
        t11.insert(END,pass1)
        Font_tuple = ("Consolas", 17, "bold")
    
        t11.configure(font = Font_tuple)
        t11.place(x=200,y=300)
        pass_gen_button.configure(text='Generate',state=ACTIVE)
        #
    
    
    def sync():
        pass_gen_button.configure(text='Generating',state=DISABLED)
        t11.delete("1.0", "end")
        
        win2.after(1,calc2)
        #win2.after(50,lambda :sync(count))
        

    pass_gen_button.config(command=lambda :sync())
    pass_gen_button.place(x=2,y=300)

    #
    #def ani(count):
   


a=b=c=d=int(1)

img = PhotoImage(file=r"Increased_lk.png")
l0 =Label(root,image=img,bg='#72C6E9').place(x=200,y=50)

l1 = Label(root,text="Welcome to Pass Generator",font=('consolas',20,BOLD),bg='#72C6E9',fg='black')
l1.place(x=200,y=0)

l2= Label(root,text='Choose the length of your password',font=('consolas',12,BOLD),bg='#72C6E9')
l2.place(x=5,y=70)

sca1 = Scale(root,highlightbackground='#72C6E9',sliderlength=15,length=280,variable=pass_len,from_=5 ,to =25,showvalue=1, orient=HORIZONTAL,bg='#72C6E9',bd=0,troughcolor='#0047b3')
sca1.place(x=350,y=55)
sca1.set(8)

l3=Label(root,bg='#72C6E9',text='Include symbols(For eg:<,?,@ etc)',font=('consolas',12,BOLD))
l3.place(x=5,y=120)
chkbtn = Checkbutton(root,textvariable = chkbtn_sta, variable = chkbtn_sta,
                          offvalue='(Not Selected)',onvalue='(Selected)',activebackground='#72C6E9',bg='#72C6E9').place(x=350,y=120)



l4=Label(root,bg='#72C6E9',text='Include Uppercase ',font=('consolas',12,BOLD))
l4.place(x=5,y=270)
chkbtn2 = Checkbutton(root,bg='#26B999',activebackground='#26B999', textvariable = chkbtn_sta2, variable = chkbtn_sta2,
                          offvalue='(Not Selected)',onvalue='(Selected)').place(x=350,y=273)



l5=Label(root,bg='#72C6E9',text='Include Lowercase',font=('consolas',12,BOLD))
l5.place(x=5,y=220)
chkbtn3 = Checkbutton(root,bg='#EFEFEF',activebackground='#EFEFEF',state=ACTIVE, textvariable = chkbtn_sta3, variable = chkbtn_sta3,
                          offvalue='(Not Selected)',onvalue='(Selected)').place(x=350,y=223)



l6=Label(root,bg='#72C6E9',text='Include Digits    ',font=('consolas',12,BOLD))
l6.place(x=5,y=170)
chkbtn4 = Checkbutton(root,bg='#26B999',activebackground='#26B999',textvariable = chkbtn_sta4, variable = chkbtn_sta4,
                          offvalue='(Not Selected)',onvalue='(Selected)',state=ACTIVE).place(x=350,y=173)



btn1=Button(root,bg='RED',fg='white',text='Generate Password',command=lambda :calculation(a,b,c,d),font=('consolas',20))
btn1.place(x=100,y=425)
t1= Text(root,height=2,width=25)

l8=Label(root,bg='#72C6E9',text='Note: This password generator offers you strong password for all social  sites\n You can simply press generate pass or tweak some settings',font=('consolas',12))
l8.place(x=5,y=370)

new_label = Label(root,cursor='hand2',bg='#72C6E9',text="Want passwords which are easy to remember!? ",font=('underline',10,BOLD,UNDERLINE))
new_label.place(x=5,y=320)
new_label.bind("<Button-1>", lambda e:win2())


mainloop()