from tkinter import*
import sqlite3
from tkinter import messagebox
 
window=Tk()
window.geometry("700x500")
window.title("WELCOME")

def sign():
    window2=Toplevel(window)
    window2.geometry("700x500")
    window2.title("Sign in form")
    un=StringVar()
    cl=StringVar()
    rn=StringVar()
    fn=StringVar()
    mn=StringVar()
    e=StringVar()
    add=StringVar()
    con=StringVar()
    pa=StringVar()

    l1=Label(window2,text="Registration Form",font=('Arial',20,'bold') ).place(x=250,y=30)
    l2=Label(window2,text="Name :",font=('Arial',10,'bold')).place(x=100,y=100)
    l3=Label(window2,text="Class :",font=('Arial',10,'bold')).place(x=100,y=130)
    l4=Label(window2,text="Roll No :",font=('Arial',10,'bold')).place(x=100,y=160)
    l5=Label(window2,text="Father's Name : ",font=('Arial',10,'bold')).place(x=100,y=190)
    l6=Label(window2,text="Mother's Name : ",font=('Arial',10,'bold')).place(x=100,y=220)
    l7=Label(window2,text="E-mail : ",font=('Arial',10,'bold')).place(x=100,y=250)
    l8=Label(window2,text="Address : ",font=('Arial',10,'bold')).place(x=100,y=280)
    l9=Label(window2,text="Contact No : ",font=('Arial',10,'bold')).place(x=100,y=310)
    l10=Label(window2,text="Password",font=('Arial',10,'bold')).place(x=100,y=340)

    t1=Entry(window2,textvariable=un).place(x=280,y=100)
    t2=Entry(window2,textvariable=cl).place(x=280,y=130)
    t3=Entry(window2,textvariable=rn).place(x=280,y=160)
    t4=Entry(window2,textvariable=fn).place(x=280,y=190)
    t5=Entry(window2,textvariable=mn).place(x=280,y=220)
    t6=Entry(window2,textvariable=e).place(x=280,y=250)
    t7=Entry(window2,textvariable=add).place(x=280,y=280)
    t8=Entry(window2,textvariable=con).place(x=280,y=310)
    t9=Entry(window2,textvariable=pa).place(x=280,y=340)


    def sub():
        db=sqlite3.connect('mansi.db')
        cr=db.cursor()
        cr.execute("INSERT INTO student (name,class,rollno,father,mother,email,address,contact,password) VALUES ('"+un.get()+"','"+cl.get()+"','"+rn.get()+"','"+fn.get()+"','"+mn.get()+"','"+e.get()+"','"+add.get()+"','"+con.get()+"','"+pa.get()+"')")
        
        db.commit()
        db.close()
        messagebox.showinfo("Alert","You are successfully Registered")

         



    btn=Button(window2,text="Submit",command=sub ,bg="light blue").place(x=265,y=400,height=30,width=50)
    window2.mainloop()
    
    



def login():
    window1=Toplevel(window)
    window1.geometry("700x500")
    window1.title("Log in")
    u=StringVar()
    p=StringVar()

    l1=Label(window1,text="LOG IN",font=('Arial',20,'bold')).place(x=300,y=100)
    l2=Label(window1,text="User Name :",font=('Arial',13,'bold')).place(x=200,y=150)
    l3=Label(window1,text="Password : ",font=('Arial',13,'bold')).place(x=200,y=200)
    t1=Entry(window1,textvariable=u).place(x=330,y=150)
    t2=Entry(window1,textvariable=p).place(x=330,y=200)

    def log():
        db=sqlite3.connect('mansi.db')
        cr=db.cursor()
        r=cr.execute("SELECT *from student where name= '"+u.get()+"' AND password='"+p.get()+"'")
        for r1 in r:
            messagebox.showinfo("log in","You are successfully log in")
            break
        else:
            messagebox.showinfo("Alert","Invalid user name and password \n please enter the valid user name and password")

        db.commit()
        db.close()

    


    btn2=Button(window1,text="log in" ,command=log,bg="light blue").place(x=265,y=300,height=30,width=50)
    window1.mainloop()





l=Label(window,text="WELCOME TO MY COACHING",font=('Arial',15,'bold')).place(x=200,y=150)
b1=Button(window,text="Sign In",command=sign,bg="light blue").place(x=250,y=200,height=50,width=80)
b2=Button(window,text="login",command=login).place(x=350,y=200,height=50,width=80)
