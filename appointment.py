import tkinter
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect("HDMS.db")
rootAA=None

def set():
    global e3,e1,e2,e4,e5,e6,conn
    p1=e1.get()
    p2=e2.get()
    p3=e3.get(tkinter.ACTIVE)
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    conn = sqlite3.connect("HDMS.db")
    conn.execute("Insert into appointment values(?,?,?,?,?,?)",(p1,p2,p3,p4,p5,p6,))
    conn.commit()
    tkinter.messagebox.showinfo("DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")


def appo():
    global rootAA,L,e1,e2,e3,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("2000x2000")
    rootAA.title("APPOINTMENTS")
    H=tkinter.Label(rootAA,text="APPOINTMENTS",fg="blue4",font="Times 40 bold italic")
    H.pack()
    l1=tkinter.Label(rootAA,text="PATIENT ID",font="arial 15 bold")
    l1.place(x=800,y=100)
    e1=tkinter.Entry(rootAA)
    e1.place(x=950,y=100,height=25)
    l2 = tkinter.Label(rootAA,text="DOCTOR ID",font="arial 15 bold")
    l2.place(x=800,y=150)
    e2 = tkinter.Entry(rootAA)
    e2.place(x=950, y=150,height=25)
    l3 = tkinter.Label(rootAA,text="APPOINTMENT NO",font="arial 15 bold")
    l3.place(x=800,y=200)
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50']
    e3=tkinter.Listbox(rootAA, width=12, height=1, selectmode='SINGLE', exportselection=0,font="arial 15 bold")
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=1000,y=200)
    l4 = tkinter.Label(rootAA,text="APPOINTMENT TIME (HH:MM:SS)",font="arial 15 bold")
    l4.place(x=800,y=250)
    e4=tkinter.Entry(rootAA)
    e4.place(x=1200,y=250,height=25)
    l5 = tkinter.Label(rootAA,text="APPOINTMENT DATE (YYYY-MM-DD)",font="arial 15 bold")
    l5.place(x=800,y=300)
    e5=tkinter.Entry(rootAA)
    e5.place(x=1200,y=300,height=25)
    l6=tkinter.Label(rootAA,text="DESCRIPTION",font="arial 15 bold")
    l6.place(x=800,y=350)
    e6=tkinter.Text(rootAA,width=80,height=3,font="arial 12 bold")
    e6.place(x=950,y=350)
    scrollbar = tkinter.Scrollbar(rootAA,orient=tkinter.VERTICAL)
    scrollbar.place(x=1160, y=200)
    e3.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=e3.yview)
    b1=tkinter.Button(rootAA,text="SET APPOINTMENT",command=set,font="arial 12 bold",bd=5,bg="indian red")
    b1.place(x=650,y=470)
    b2=tkinter.Button(rootAA,text="DELETE APPOINTMENT",command=dela,font="arial 12 bold",bd=5,bg="indian red")
    b2.place(x=850,y=470)
    b4=tkinter.Button(rootAA,text="TODAYS APPOINTMENTS",command=va,font="arial 12 bold",bd=5,bg="indian red")
    b4.place(x=1080,y=470)
    b4=tkinter.Button(rootAA,text="EXIT",command=exitmain,font="arial 12 bold",bd=5,bg="indian red")
    b4.place(x=1330,y=470)
    rootAA.mainloop()

def exitmain():
    rootAA.destroy()

def remove():
    global e7,edd
    edd=str(e7.get())
    v=list(conn.execute("select * from appointment where AP_NO=?", (edd,)))
    if (len(v)==0):
        tkinter.messagebox.showinfo("ERROR","PATIENT APPOINTMENT NOT FIXED")
    else:
        conn.execute('DELETE FROM appointment where AP_NO=?',(edd,))
        tkinter.messagebox.showinfo("","PATIENT APPOINTMENT DELETED")
        conn.commit()

rootDAP=None
def exitdel():
       rootDAP.destroy()

def dela():
    global rootDAP,e1,e7
    rootDAP=tkinter.Tk()
    rootDAP.geometry("2000x2000")
    rootDAP.title("DELETE APPOINTMENTS")
    headd=tkinter.Label(rootDAP,text="DELETE APPOINTMENT DETAILS",fg="blue4",font='Times 35 bold italic')
    headd.pack()
    l3 = tkinter.Label(rootDAP, text="ENTER APPOINTMENT NUMBER TO DELETE",font="arial 15 bold")
    l3.place(x=750, y=100)
    e7=tkinter.Entry(rootDAP)
    e7.place(x=850,y=150,height=25)
    b3=tkinter.Button(rootDAP,text="DELETE",command=remove,font="arial 12 bold",bg="indian red",bd=5)
    b12=tkinter.Button(rootDAP,text="EXIT",command=exitdel,font="arial 12 bold",bg="indian red",bd=5)
    b13=tkinter.Button(rootDAP,text="NEW",command=dela,font="arial 12 bold",bg="indian red",bd=5)
    b13.place(x=1050,y=220)
    b3.place(x=850,y=220)
    b12.place(x=960,y=220)
    rootDAP.mainloop()

rootAP=None

def viewappointment():
    global e8,ap,s1,s2,s3,s4,s5,s6
    ap=str(e8.get())
    vv = list(conn.execute("select * from appointment where AP_DATE=?", (ap,)))
    if (len(vv) == 0):
        tkinter.messagebox.showinfo("DATABSE SYSTEM","NO APPOINTMENT TODAY")
    else:
        s=conn.execute("Select * from appointment where AP_DATE=?",(ap,))
        for i in s:
            s11=tkinter.Label(rootAP,text="PATIENT ID:",fg='green',font="arial 13 bold")
            s11.place(x=820,y=300)
            s1=tkinter.Label(rootAP,text=i[0],font="arial 12 bold")
            s1.place(x=950,y=300)

            s22=tkinter.Label(rootAP,text="EMPLOYEE ID:",fg='green',font="arial 13 bold")
            s22.place(x=820,y=350)
            s2=tkinter.Label(rootAP,text=i[1],font="arial 12 bold")
            s2.place(x=980,y=350)

            s33=tkinter.Label(rootAP,text="APPLICATION NUMBER:",fg='green',font="arial 13 bold")
            s33.place(x=820,y=400)
            s3=tkinter.Label(rootAP,text=i[2],font="arial 12 bold")
            s3.place(x=1050,y=400)

            s44=tkinter.Label(rootAP,text="APPLICATION TIME:",fg='green',font="arial 13 bold")
            s44.place(x=820,y=450)
            s4=tkinter.Label(rootAP,text=i[3],font="arial 12 bold")
            s4.place(x=1050,y=450)

            s55=tkinter.Label(rootAP,text="APPLICATION DATE:",fg='green',font="arial 13 bold")
            s55.place(x=820,y=500)
            s5=tkinter.Label(rootAP,text=i[4],font="arial 12 bold")
            s5.place(x=1050,y=500)
           
            s66=tkinter.Label(rootAP,text="DESCRIPTION:",fg='green',font="arial 13 bold")
            s66.place(x=820,y=550)
            s6=tkinter.Label(rootAP,text=i[5],font="arial 12 bold")
            s6.place(x=980,y=550)
def exitva():
    rootAP.destroy()

def va():
    global rootAP,e8
    global s1,s2,s3,s4,s5,s6
    rootAP=tkinter.Tk()
    rootAP.geometry("2000x2000")
    rootAP.title("TODAYS APPOINTMENTS")
    h0=tkinter.Label(rootAP,text="TODAYS APPOINTMENT",fg="blue4",font="Times 35 bold italic")
    h0.pack()
    h1=tkinter.Label(rootAP,text="ENTER DATE TO VIEW APPOINTMENTS",font="arial 15 bold")
    h1.place(x=750,y=100)
    e8=tkinter.Entry(rootAP,font="arial 15 bold")
    e8.place(x=850,y=150,height=25)
    b5=tkinter.Button(rootAP,text="SEARCH",command=viewappointment,font="arial 12 bold",bg="indian red",bd=5)
    bb5=tkinter.Button(rootAP,text="EXIT",command=exitva,font="arial 12 bold",bg="indian red",bd=5)
    bb5.place(x=960,y=220)
    b5.place(x=850,y=220)
    rootAP.mainloop()

