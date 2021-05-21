import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("HDMS.db")

P_id=None
rootR=None

##-----------------------------------------------------------TO INSERT ROOM VALUES----------------------------------------##
def room_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    conn = sqlite3.connect("HDMS.db")
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    conn.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(r1,r3, r2, r4, r5, r6,))
    tkinter.messagebox.showinfo("DATABSE SYSTEM", "ROOM ALLOCATED")
    conn.commit()
    conn.close()
#--------------------------------------------------------------------------------------------------------------------------##    

#-----------------------------------------------------------TO UPDATE ROOM VALUES------------------------------------------##
def update_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    p = list(conn.execute("Select * from ROOM where PATIENT_ID=?", (r1,)))
    if len(p) != 0:
        conn.execute('UPDATE ROOM SET ROOM_NO=?,ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r3, r2, r4, r5, r6,r1,))
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "ROOM DETAILS UPDATED")
        conn.commit()
    else:
        tkinter.messagebox.showinfo("DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")
##--------------------------------------------------------------------------------------------------------------------------##   

##ROOT FOR DISPLAY ROOM INFO
rootRD=None

##EXIT FOR ROOM_PAGE
def EXITT():
    global rootR
    rootR.destroy()

##--------------------------------------------------------------FUNCTION FOR ROOM DISPLAY BUTTON----------------------------##
def ROOMD_button():
    global r1,c1,lr1,dis1,lr2,dis2,ii,conn,c1,P_iid
    conn = sqlite3.connect("HDMS.db")
    c1=conn.cursor()
    r1=P_iid.get()
    p=list(c1.execute('select * from  ROOM  where PATIENT_ID=?',(r1,)))
    if (len(p)==0):
        tkinter.messagebox.showinfo("DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
    else:
        t=c1.execute('SELECT NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(r1,));
        for ii in t:
            lr0=tkinter.Label(rootRD,text="PATIENT NAME :",fg='Dodgerblue4',font="arial 12 bold")
            dis0=tkinter.Label(rootRD,text=ii[0],font="arial 12 bold")
            lr0.place(x=800,y=300)
            dis0.place(x=800,y=350)
            lr1=tkinter.Label(rootRD,text="ROOM NO :",fg='Dodgerblue4',font="arial 12 bold")
            dis1=tkinter.Label(rootRD,text=ii[1],font="arial 12 bold")
            lr1.place(x=800,y=400)
            dis1.place(x=800,y=450)
            lr2=tkinter.Label(rootRD,text="ROOM TYPE :",fg='Dodgerblue4',font="arial 12 bold")
            dis2=tkinter.Label(rootRD,text=ii[2],font="arial 12 bold")
            lr2.place(x=800,y=500)
            dis2.place(x=800,y=550)
#----------------------------------------------------------------------------------------------------------------------------##  

def exittt():
    rootRD.destroy()

def roomDD():
    global rootRD,ra1,ss,P_iid
    rootRD=tkinter.Tk()
    rootRD.geometry("2000x2000")
    rootRD.title("ROOM INFO")
    headd=tkinter.Label(rootRD,text="SEARCH ROOM DETAILS",fg="blue4",font='Times 35 bold italic')
    ra1=tkinter.Label(rootRD,text="ENTER PATIENT ID",font="arial 15 bold")
    ra1.place(x=800,y=100)
    P_iid=tkinter.Entry(rootRD)
    ss=tkinter.Button(rootRD,text="SEARCH",command=ROOMD_button,font='arial 12 bold',bg="indian red",fg="white",bd=5)
    P_iid.place(x=810, y=150)
    ss.place(x=800,y=200)
    e=tkinter.Button(rootRD,text="EXIT",command=exittt,font='arial 12 bold',bg="indian red",fg="white",bd=5)
    e.place(x=910,y=200)
    headd.pack()
    rootRD.mainloop()
    

def exitt():
    rootR.destroy()

L=None
L1=None
def Room_all():
    global rootR,r_head,P_id,id,room_tl,L,i,room_t,room_nol,room_no,L1,j,ratel,rate,da_l,da ,dd_l,dd,Submit,Update,cr
    rootR=tkinter.Tk()
    rootR.title("ROOM ALLOCATION")
    rootR.geometry("2000x2000")
    r_head=tkinter.Label(rootR,text="ROOM ALLOCATION",font='Times 40 bold italic',fg="blue4")
    r_head.pack()
    id=tkinter.Label(rootR,text="PATIENT ID",font="arial 15 bold")
    id.place(x=600,y=80)
    P_id=tkinter.Entry(rootR)
    P_id.place(x=750,y=80,height=25)
    room_tl=tkinter.Label(rootR,text="ROOM TYPE",font="arial 15 bold")
    room_tl.place(x=600, y=130)
    L=['SINGLE ROOM: Rs 4500','TWIN SHARING : Rs2500','TRIPLE SHARING: Rs2000']
    room_t= tkinter.Listbox(rootR, width=25, height=3, selectmode='SINGLE', exportselection=0,font="arial 12 bold")
    for i in L:
        room_t.insert(tkinter.END,i)
    room_t.place(x=750,y=130)
    room_nol=tkinter.Label(rootR,text="ROOM NUMBER",font="arial 15 bold")
    room_nol.place(x=600,y=230)
    L1=['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']
    room_no = tkinter.Listbox(rootR, width=8, height=1, selectmode='SINGLE', exportselection=0,font="arial 12 bold")
    for j in L1:
        room_no.insert(tkinter.END,j)
    room_no.place(x=780,y=230,height=25)
    ratel=tkinter.Label(rootR, text="ROOM CHARGES",font="arial 15 bold")
    ratel.place(x=600, y=280)
    rate=tkinter.Entry(rootR)
    rate.place(x=850, y=280,height=25)
    da_l = tkinter.Label(rootR, text="DATE ADMITTED",font="arial 15 bold")
    da_l.place(x=600,y=320)
    da=tkinter.Entry(rootR)
    da.place(x=850,y=320,height=25)
    dd_l = tkinter.Label(rootR, text="DATE DISCHARGED",font="arial 15 bold")
    dd_l.place(x=600, y=370)
    dd =tkinter.Entry(rootR)
    dd.place(x=850, y=370,height=25)
    Submit=tkinter.Button(rootR,text="SUBMIT",font="arial 12 bold",command=room_button,bg="indian red",fg="white",bd=5)
    Submit.place(x=650,y=450)
    Update=tkinter.Button(rootR,text="UPDATE",font="arial 12 bold",command=update_button,bg="indian red",fg="white",bd=5)
    Update.place(x=750,y=450)
    cr=tkinter.Button(rootR,text='ROOM DETAILS',font="arial 12 bold",command=roomDD,bg="indian red",fg="white",bd=5)
    cr.place(x=850,y=450)
    ee=tkinter.Button(rootR,text="EXIT",font="arial 12 bold",command=exitt,bg="indian red",fg="white",bd=5)
    ee.place(x=1010,y=450)
    rootR.mainloop()

