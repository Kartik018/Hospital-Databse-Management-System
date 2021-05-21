import tkinter
import tkinter.messagebox
import sqlite3
conn=sqlite3.connect("HDMS.db")

#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None

#display/search button----
def Search_button():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    c1=conn.cursor()
    inp_s=entry.get()
    p=list(c1.execute('select * from PATIENT where PATIENT_ID=?',(inp_s,)))
    if (len(p)==0):
        tkinter.messagebox.showinfo("ERROR MESSAGE","PATIENT RECORD NOT FOUND..!!")
    else:
        t=c1.execute('SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=?',(inp_s,));
        for i in t:
            l1=tkinter.Label(rootS,text="PATIENT ID :",fg='Dodgerblue4',font="arial 12 bold")
            l1.place(x=800,y=270)
            dis1=tkinter.Label(rootS,text=i[0],font="arial 12 bold")
            dis1.place(x=1080,y=270)
            l2=tkinter.Label(rootS,text="PATIENT NAME :",fg='Dodgerblue4',font="arial 12 bold")
            l2.place(x=800,y=320)
            dis2=tkinter.Label(rootS,text=i[1],font="arial 12 bold")
            dis2.place(x=1080,y=320)
            l3=tkinter.Label(rootS,text="PATIENT SEX :",fg='Dodgerblue4',font="arial 12 bold")
            l3.place(x=800,y=370)
            dis3=tkinter.Label(rootS,text=i[2],font="arial 12 bold")
            dis3.place(x=1080,y=370)
            l4=tkinter.Label(rootS,text="PATIENT BLOOD GROUP :",fg='Dodgerblue4',font="arial 12 bold")
            l4.place(x=800,y=420)
            dis4=tkinter.Label(rootS,text=i[3],font="arial 12 bold")
            dis4.place(x=1080,y=420)
            l5=tkinter.Label(rootS,text="PATIENT DATE OF BIRTH :",fg='Dodgerblue4',font="arial 12 bold")
            l5.place(x=800,y=470)
            dis5=tkinter.Label(rootS,text=i[4],font="arial 12 bold")
            dis5.place(x=1080,y=470)
            l6=tkinter.Label(rootS,text="PATIENT ADDRESS :",fg='Dodgerblue4',font="arial 12 bold")
            l6.place(x=800,y=520)
            dis6=tkinter.Label(rootS,text=i[5],font="arial 12 bold")
            dis6.place(x=1080,y=520)
            l7=tkinter.Label(rootS,text="PATIENT DOCTOR/TEAM :",fg='Dodgerblue4',font="arial 12 bold")
            l7.place(x=800,y=570)
            dis7=tkinter.Label(rootS,text=i[6],font="arial 12 bold")
            dis7.place(x=1080,y=570)
            l8=tkinter.Label(rootS,text="PATIENT EMAIL :",fg='Dodgerblue4',font="arial 12 bold")
            l8.place(x=800,y=620)
            dis8=tkinter.Label(rootS,text=i[7],font="arial 12 bold")
            dis8.place(x=1080,y=620)
            l9=tkinter.Label(rootS,text="PATEINT CONTACT NO :",fg='Dodgerblue4',font="arial 12 bold")
            l9.place(x=800,y=670)
            dis9=tkinter.Label(rootS,text=i[8],font="arial 12 bold")
            dis9.place(x=1080,y=670)
            l10=tkinter.Label(rootS,text="PATIENT ALTERNATE CONTACT :",fg='Dodgerblue4',font="arial 12 bold")
            l10.place(x=800,y=720)
            dis10=tkinter.Label(rootS,text=i[9],font="arial 12 bold")
            dis10.place(x=1080,y=720)    

    


def eXO():
    rootS.destroy()

##search window
def P_display():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.geometry("2000x2000")
    rootS.title("SEARCH WINDOW")
    head=tkinter.Label(rootS,text="SEARCH PATIENT",fg="blue4",font='Times 35 bold italic')
    ls=tkinter.Label(rootS,text="ENTER PATIENT ID TO SEARCH",font="arial 15 bold")
    ls.place(x=770,y=100)
    entry=tkinter.Entry(rootS,width=30)
    entry.place(x=800,y=150,height=40)
    searchB=tkinter.Button(rootS,text='SEARCH',font='arial 10 bold',command=Search_button,bg="indian red",fg="white",bd=5)
    searchB.place(x=880,y=220)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    rootS.mainloop()

inp_d=None
entry1=None
errorD=None
disd1=None

#DELTE BUTTON-------
def Delete_button():
    global inp_d,entry1,errorD,disd1
    c1= conn.cursor()
    inp_d = entry1.get()
    p=list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
    pp=list(conn.execute("select * from CONTACT_NO where PATIENT_ID=?",(inp_d)))
    if (len(p) & len(pp) ==0):
        tkinter.messagebox.showinfo("ERROR MESSAGE","PATIENT RECORD NOT FOUND")
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(inp_d,))
        conn.execute('DELETE FROM CONTACT_NO where PATIENT_ID=?',(inp_d))
        tkinter.messagebox.showinfo("","PATIENT RECORD DELETED SUCCESSFULY")
        conn.commit()
   


#EXIT FROM DELETE SCREEN
def exit():
    rootD.destroy()

## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.geometry("2000x2000")
    rootD.title("DELETE WINDOW")
    headD=tkinter.Label(rootD,text="DELETE PATIENT",fg="blue4",font='Times 35 bold italic')
    ld=tkinter.Label(rootD,text="ENTER PATIENT ID TO DELETE",font="arial 15 bold")
    ld.place(x=770,y=200)
    entry1=tkinter.Entry(rootD,width=30)
    entry1.place(x=800,y=250,height=40)
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button,font='arial 10 bold',bg="indian red",fg="white",bd=5)
    DeleteB1=tkinter.Button(rootD,text="EXIT",command=exit,font='arial 10 bold',bg="indian red",fg="white",bd=5)
    DeleteB.place(x=880,y=320)
    DeleteB1.place(x=880,y=370)
    headD.pack()
    rootD.mainloop()

##variables for update

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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------##
def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
    conn.cursor()
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()
    u4 = pat_dob.get()
    u5 = pat_BG.get()
    u6 = pat_contact.get()
    u7 = pat_contactalt.get()
    u8 = pat_email.get()
    u9 = pat_CT.get()
    u10 = pat_address.get()
    conn = sqlite3.connect("HDMS.db")
    p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
    if len(p) != 0:
        conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?', ( u2, u3, u4, u5, u10, u9, u8,u1,))
        conn.execute('UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', ( u6, u7,u1,))
        tkinter.messagebox.showinfo("DATABSE SYSTEM", "DETAILS UPDATED SUCCESSFULLY")
        conn.commit()

    else:
        tkinter.messagebox.showinfo("DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------##   

labelu=None
bu1=None

def EXITT():
    rootU.destroy()

##-----PATIENT UPDATE SCREEN -----##
def P_UPDATE():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootU, regform, id, name, dob, sex, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
    rootU = tkinter.Tk()
    rootU.geometry("2000x2000")
    rootU.title("UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_UPDATE)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    HEAD=tkinter.Label(rootU,text="ENTER NEW DETAILS TO UPDATE",fg='blue4',font='Times 35 bold italic')
    id = tkinter.Label(rootU, text="PATIENT ID",font='arial 11 bold')
    pat_ID = tkinter.Entry(rootU,width=25)
    name = tkinter.Label(rootU, text="PATIENT NAME",font='arial 11 bold')
    pat_name = tkinter.Entry(rootU,width=25)
    sex = tkinter.Label(rootU, text="SEX",font='arial 11 bold')
    pat_sex = tkinter.Entry(rootU,width=25)
    dob = tkinter.Label(rootU, text="DOB (YYYY-MM-DD)",font='arial 11 bold')
    pat_dob = tkinter.Entry(rootU,width=25)
    bg = tkinter.Label(rootU, text="BLOOD GROUP",font='arial 11 bold')
    pat_BG = tkinter.Entry(rootU,width=25)
    c1 = tkinter.Label(rootU, text="CONTACT NUMBER",font='arial 11 bold')
    pat_contact = tkinter.Entry(rootU,width=25)
    c2 = tkinter.Label(rootU, text="ALTERNATE CONTACT",font='arial 11 bold')
    pat_contactalt = tkinter.Entry(rootU,width=25)
    email = tkinter.Label(rootU, text="EMAIL",font='arial 11 bold')
    pat_email = tkinter.Entry(rootU,width=25)
    ct = tkinter.Label(rootU, text="CONSULTING TEAM / DOCTOR",font='arial 11 bold')
    pat_CT = tkinter.Entry(rootU,width=25)
    addr = tkinter.Label(rootU, text="ADDRESS",font='arial 11 bold')
    pat_address = tkinter.Entry(rootU,width=25)
    SUBMIT=tkinter.Button(rootU,text="SUBMIT",command=up1,font='arial 12 bold',bg="indian red",fg="white",bd=5)
    SUBMIT.place(x=880,y=650)
    HEAD.pack()
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
    #SUBMIT.pack()
    rootU.mainloop()


