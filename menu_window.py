import tkinter
from tkinter import*
import sqlite3
import tkinter.messagebox
from patient_registration import P_display
from patient_registration import D_display
from patient_registration import P_UPDATE
from room import Room_all
from billing import BILLING
from employee_registration import emp_screen
from appointment import appo

conn=sqlite3.connect("HDMS.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("2000x2000")
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="MENU",font='Times 40 bold italic',fg='blue4')
    button1=tkinter.Button(root1,text="PATIENT REGISTRATION",command=PAT,bg='light blue',fg='black',font='arial 12 bold',bd=5)
    button2 = tkinter.Button(root1, text="ROOM ALLOCATION",command=Room_all,bg='light green',fg='black',font='arial 12 bold',bd=5)
    button3 = tkinter.Button(root1, text="EMPLOYEE REGISTRATION",command=emp_screen,bg='light blue',fg='black',font='arial 12 bold',bd=5)
    button4 = tkinter.Button(root1, text="BOOK APPOINTMENT",command=appo,bg='light green',fg='black',font='arial 12 bold',bd=5)
    button5 = tkinter.Button(root1, text="PATIENT BILL",command=BILLING,bg='light blue',fg='black',font='arial 12 bold',bd=5)
    button6 = tkinter.Button(root1, text="EXIT",command=ex,bg='light green',fg='black',font='arial 12 bold',bd=5)
    m.place(x=850,y=80)
   
    button1.place(relx=0.350,rely=0.2,relwidth=0.30,relheight=0.05)

    button2.place(relx=0.350,rely=0.3,relwidth=0.30,relheight=0.05)

    button3.place(relx=0.350,rely=0.4,relwidth=0.30,relheight=0.05)

    button4.place(relx=0.350,rely=0.5,relwidth=0.30,relheight=0.05)

    button5.place(relx=0.350,rely=0.6,relwidth=0.30,relheight=0.05)

    button6.place(relx=0.350,rely=0.7,relwidth=0.30,relheight=0.05)
    root1.mainloop()

p=None
def IN_PAT():
     global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
     conn=sqlite3.connect("HDMS.db")
     conn.cursor()
     pp1=pat_ID.get()
     pp2=pat_name.get()
     pp3=pat_sex.get()
     pp4=pat_BG.get()
     pp5=pat_dob.get()
     pp6=pat_contact.get()
     pp7=pat_contactalt.get()
     pp8=pat_address.get()
     pp9=pat_CT.get()
     pp10=pat_email.get()
     conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,))
     conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(pp1,pp6,pp7,))
     tkinter.messagebox.showinfo("", "SUBMITTED SUCCESSFULY")
     conn.commit()


#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    tkinter.messagebox.showinfo("HELP","CONTACT DATABASE HEAD")

def nothing1():
    tkinter.messagebox.showinfo("ABOUT","DESIGNED BY KARTIK")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.geometry("2000x2000")
    rootp.title("PATIENT FORM")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXO)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=nothing)
    helpmenu.add_command(label="ABOUT",command=nothing1)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="REGISTRATION FORM",font="Times 40 bold italic",fg='blue4')

    id=tkinter.Label(rootp,text="PATIENT ID",font='arial 12 bold')
    pat_ID=tkinter.Entry(rootp,width=25)
   
    name=tkinter.Label(rootp,text="PATIENT NAME",font='arial 12 bold') 
    pat_name = tkinter.Entry(rootp,width=25) 
       
    sex=tkinter.Label(rootp,text="SEX",font='arial 12 bold')
    pat_sex=tkinter.Entry(rootp,width=25)

    dob=tkinter.Label(rootp, text="DOB (YYYY-MM-DD)",font='arial 12 bold')
    pat_dob=tkinter.Entry(rootp,width=25)
  
    bg=tkinter.Label(rootp, text="BLOOD GROUP",font='arial 12 bold') 
    pat_BG=tkinter.Entry(rootp,width=25)

    c1=tkinter.Label(rootp, text="CONTACT NUMBER",font='arial 12 bold') 
    pat_contact=tkinter.Entry(rootp,width=25)
 

    c2=tkinter.Label(rootp, text="ALTERNATE CONTACT",font='arial 12 bold')
    pat_contactalt=tkinter.Entry(rootp,width=25) 

    email=tkinter.Label(rootp, text="EMAIL",font='arial 12 bold') 
    pat_email = tkinter.Entry(rootp,width=25) 

    ct=tkinter.Label(rootp,text="CONSULTING TEAM / DOCTOR",font='arial 12 bold')
    pat_CT=tkinter.Entry(rootp,width=25)

    addr=tkinter.Label(rootp, text="ADDRESS",font='arial 14 bold')
    pat_address=tkinter.Entry(rootp,width=25)
 
    back=tkinter.Button(rootp,text="<< BACK",command=menu,font='arial 10 bold',bg="indian red",fg="white",bd=5)
    SEARCH=tkinter.Button(rootp,text="  SEARCH >>  ",command=P_display,font='arial 10 bold',bg="indian red",fg="white",bd=5)
    DELETE=tkinter.Button(rootp,text="  DELETE  ",command=D_display,font='arial 10 bold',bg="indian red",fg="white",bd=5)
    UPDATE=tkinter.Button(rootp,text="  UPDATE  ",command=P_UPDATE,font='arial 10 bold',bg="indian red",fg="white",bd=5)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,font='arial 12 bold',bg="indian red",fg="white",bd=5)
    SUBMIT.place(x=880,y=650)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    c2.pack()
    pat_contactalt.pack()
    email.pack()
    pat_email.pack()
    ct.pack()
    pat_CT.pack()
    addr.pack()
    pat_address.pack()

    back.pack(side=tkinter.LEFT)
    UPDATE.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    SEARCH.pack(side=tkinter.LEFT)
    rootp.mainloop()

