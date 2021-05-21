import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("HDMS.db")

#variables
rootB=None

#----------------------TO UPDATE DISCHARGE DATE--------------------------------------------------------##
def date_up():
    global b1,b2
    b1 = P_id.get()
    b2 = dd.get()
    conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
    conn.commit()
    tkinter.messagebox.showinfo("DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
#-------------------------------------------------------------------------------------------------------##   

#---------------------TO UPDATE MEDICINE AND TREATMENT VALUES---------------------------------------------##
def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("HDMS.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
    conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
    conn.commit()
    tkinter.messagebox.showinfo("DATABASE SYSTEM", "BILLING DATA SAVED")
#---------------------------------------------------------------------------------------------------------##
    
#------------------------TO CALCULATE TOTAL AMOUNT--------------------------------------------------------##
def calci():
    global b1
    conn = sqlite3.connect("HDMS.db")
    u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
    conn.commit()
    for ii in u:
         pp=tkinter.Label(rootB,text="TOTAL AMOUNT =",fg='slateBlue4',bg="white",font='Arial 18 bold')
         pp.place(x="550", y='440')
         uu=tkinter.Label(rootB,text=ii[0],font="arial 18 bold")
         uu.place(x="980",y='440')
#---------------------------------------------------------------------------------------------------------##

L1=None
L2=None
L3=None
L4=None

def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,dd,cost,med,med_q,price,treat_1,treat_2,cost_t,j,jj,jjj,jjjj,L2,L3,L4
    rootB=tkinter.Tk()
    rootB.geometry("2000x2000")
    rootB.title("BILLING SYSTEM")
    head=tkinter.Label(rootB,text="PATIENT BILL",font="Times 40 bold italic",fg='blue4')
    head.pack()
    id = tkinter.Label(rootB, text="PATIENT ID",font="arial 15 bold")
    id.place(x=550, y=80)
    P_id = tkinter.Entry(rootB)
    P_id.place(x=700, y=80,height=25)
    dd_l = tkinter.Label(rootB, text="DATE DISCHARGED",font="arial 15 bold")
    dd_l.place(x=550, y=130)
    dd = tkinter.Entry(rootB)
    dd.place(x=800, y=130,height=25)
    ddp=tkinter.Button(rootB,text="UPDATE DISCHARGE DATE",command=date_up,bg="indian red",fg="white",font="arial 12 bold",bd=4)
    ddp.place(x=1000,y=130)
    treat = tkinter.Label(rootB, text="SELECT TREATMENT",font="arial 15 bold")
    treat.place(x=550, y=190)
    L1 = ["CONSULATION","SURGERY","LAB TEST"]
    treat_1= tkinter.Listbox(rootB, width=20, height=1, selectmode='SINGLE', exportselection=0,font="arial 11 bold")
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=800,y=190,height=25)
    treat_c = tkinter.Label(rootB, text="CODE",font="arial 15 bold")
    treat_c.place(x=1000, y=190)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB, width=8, height=1, selectmode='SINGLE', exportselection=0,font="arial 11 bold")
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.place(x=1100, y=190,height=25)
    costl= tkinter.Label(rootB, text="COST ₹",font="arial 15 bold")
    costl.place(x=1200, y=190)
    cost_t = tkinter.Entry(rootB,width=5)
    cost_t.place(x=1300, y=190,height=25)
    med1 = tkinter.Label(rootB, text="SELECT MEDICINE",font="arial 15 bold")
    med1.place(x=550, y=240)
    L3 = ["NEURAL", "FANEKPLUS", "DISPRIN","DOLO+","BANDAGE","DIGENE"]
    med = tkinter.Listbox(rootB, width=20, height=1, selectmode='SINGLE', exportselection=0,font="arial 11 bold")
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=800, y=240,height=25)
    med_ql = tkinter.Label(rootB, text="QUANTITY",font="arial 15 bold")
    med_ql.place(x=1000, y=240)
    L4 = [1,2,3,4,5,6,7,8,9,10]
    med_q = tkinter.Listbox(rootB, width=6, height=1, selectmode='SINGLE', exportselection=0,font="arial 11 bold")
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.place(x=1150, y=240,height=25)
    pricel = tkinter.Label(rootB, text="PRICE ₹",font="arial 15 bold")
    pricel.place(x=1250, y=240)
    price = tkinter.Entry(rootB, width=5)
    price.place(x=1350, y=240,height=25)
    b1=tkinter.Button(rootB,text="GENERATE BILL",command=calci,font="arial 12 bold",bg="indian red",fg="white",bd=5)
    b1.place(x="710",y="340")
    b2 = tkinter.Button(rootB, text="UPDATE DATA", command=up,font="arial 12 bold",bg="indian red",fg="white",bd=5)
    b2.place(x="550", y="340")
    ee=tkinter.Button(rootB,text="EXIT",command=exitt,font="arial 12 bold",bg="indian red",fg="white",bd=5)
    ee.place(x='930',y='340')
    nn=tkinter.Button(rootB,text="NEW",command=BILLING,font="arial 12 bold",bg="indian red",fg="white",bd=5)
    nn.place(x='1030',y='340')
    rootB.mainloop()

