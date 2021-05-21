import tkinter
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect("HDMS.db")
c=conn.cursor()
rootE=None
var=None

#----------------------------------------------------------------------------------------------------------------------------------##
def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=lb.get(tkinter.ACTIVE)
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    conn = sqlite3.connect("HDMS.db")
    c=conn.cursor()
    c.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
    c.execute("SELECT COUNT(*) FROM EMPLOYEE")
    conn.commit()
    print(c.fetchone())
    tkinter.messagebox.showinfo("DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
    
##----------------------------------------------------------------------------------------------------------------------------------##

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    rootE=tkinter.Tk()
    rootE.title("Employee registration")
    rootE.geometry('2000x2000')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="EMPLOYEE REGISTRATION",fg='blue4',font="Times 40 bold italic")
    H.place(x=600,y=40)
    l1=tkinter.Label(rootE,text="EMPLOYEE ID",font='arial 15 bold')
    l1.place(x="600",y="140")
    t1=tkinter.Entry(rootE)
    t1.place(x='750',y='140')
    l2 = tkinter.Label(rootE, text="EMPLOYEE NAME",font='arial 15 bold')
    l2.place(x=600,y=190)
    t2 = tkinter.Entry(rootE)
    t2.place(x='780', y='190')
    l3 = tkinter.Label(rootE, text="SEX",font='arial 15 bold')
    l3.place(x=600,y=240)
    r1 = tkinter.Radiobutton(rootE, text="MALE", variable=var, value="Male",font='arial 15 bold',fg='steelblue4')
    r1.place(x=650, y=240)
    r2 = tkinter.Radiobutton(rootE, text="FEMALE", variable=var, value="Female",font='arial 15 bold',fg='steelblue4')
    r2.place(x=750,y=240)
    l4 = tkinter.Label(rootE, text="AGE",font='arial 15 bold')
    l4.place(x=600,y=290)
    t3=tkinter.Entry(rootE)
    t3.place(x=650,y=290)
    l5 = tkinter.Label(rootE, text="EMPLOYEE TYPE",font='arial 15 bold')
    l5.place(x=600,y=340)
    scrollbar = tkinter.Scrollbar(rootE, width=12)
    scrollbar.place(x=940, y=340)
    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1, width=15,yscrollcommand = scrollbar.set,font='arial 12 bold')
    lb.insert(tkinter.END, "DOCTOR")
    lb.insert(tkinter.END, "NURSE")
    lb.insert(tkinter.END, "RECEPTIONIST")
    lb.place(x=780, y=340)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)
    l6=tkinter.Label(rootE,text="SALARY",font='arial 15 bold')
    l6.place(x=600,y=390)
    t4=tkinter.Entry(rootE)
    t4.place(x=690,y=390)
    l7 = tkinter.Label(rootE, text="EXPERIENCE",font='arial 15 bold')
    l7.place(x=600,y=440)
    t5 = tkinter.Entry(rootE)
    t5.place(x=750,y=440)
    l8 = tkinter.Label(rootE, text="MOBILE NO",font='arial 15 bold')
    l8.place(x=600,y=490)
    t6 = tkinter.Entry(rootE)
    t6.place(x=720,y=490)
    l9 = tkinter.Label(rootE, text="EMAIL",font='arial 15 bold')
    l9.place(x=600,y=540)
    t7=tkinter.Entry(rootE)
    t7.place(x=680,y=540)
    b1=tkinter.Button(rootE,text="SAVE",command=inp,bg='indian red',fg='white',font='arial 12 bold',bd=5)
    b1.place(x=600,y=650)
    b2=tkinter.Button(rootE,text="DELETE EMPLOYEE",command=delo,fg='white',bg='indian red',font='arial 12 bold',bd=5)
    b2.place(x=680,y=650)
    b3=tkinter.Button(rootE,text="EXIT",command=ex,bg='indian red',fg='white',font='arial 12 bold',bd=5)
    b3.place(x=875,y=650)
    rootE.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------##
def delling():
    global d1,de
    de=str(d1.get())
    conn = sqlite3.connect("HDMS.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?",(de,))
        tkinter.messagebox.showinfo("DATABASE SYSTEM","EMPLOYEE RECORD DELETED SUCCESFULLY")
        conn.commit()
    else:
        tkinter.messagebox.showinfo("ERROR MESSAGE","EMPLOYEE RECORD NOT FOUND")
    
##-------------------------------------------------------------------------------------------------------------------------------------------------------##    


def dexo():
    rootDE.destroy()

rootDE=None
def delo():
    global rootDE,d1
    rootDE=tkinter.Tk()
    rootDE.geometry("2000x2000")
    rootDE.title("EMPLOYEE DELETION")
    h1=tkinter.Label(rootDE,text="DELETE EMPLOYEE",font="Times 35 bold italic",fg='blue4')
    h1.place(x=680,y=40)
    l10=tkinter.Label(rootDE,text="ENTER EMPLOYEE ID TO DELETE",font="arial 15 bold")
    l10.place(x=750,y=200)
    d1=tkinter.Entry(rootDE,width=30)
    d1.place(x=800,y=250)
    B1=tkinter.Button(rootDE,text="DELETE",command=delling,font="arial 12 bold",bg="indian red",fg="white",bd=5)
    B1.place(x=830,y=320)
    B2=tkinter.Button(rootDE,text="EXIT",command=dexo,font="arial 12 bold",bg="indian red",fg="white",bd=5)
    B2.place(x=950,y=320)
    rootDE.mainloop()
def trig():
    c.execute("DROP TRIGGER IF EXISTS count_employee")
    c.execute("CREATE TRIGGER count_employee AFTER INSERT ON EMPLOYEE BEGIN SELECT COUNT(*) FROM EMPLOYEE; END;")
    conn.commit()
    print(c.fetchall())

