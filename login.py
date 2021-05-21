import tkinter
from tkinter import*
from tkinter import messagebox
from menu_window import menu

#root=login page
#root1=menu
#rootp=patient form

#variable
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='kartik' and S2=='12345'):
       menu()
    elif(S1=='dbmslab' and S2=='18csl58'):
         menu()
    else:
         tkinter.messagebox.showinfo("Error message", "Wrong Id or Password")
        


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("1500x1500")
    topframe =Frame(root,bg="dark green",bd=5)
    topframe.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    heading =Label(topframe, text="WELCOME TO HOSPITAL MANAGEMENT SYSTEM",bg='white',fg='blue4',font=('Times 20 bold italic',30))
    heading.place(relx=0,rely=0, relwidth=1, relheight=1)

   
    username=tkinter.Label(root,text="USERNAME",fg='black',font='Times 16 bold italic')
    username.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    userbox = tkinter.Entry(root,font="arial 15 bold")
    userbox.place(relx=0.435,rely=0.5, relwidth=0.15,relheight=0.05)
    password=tkinter.Label(root,text="PASSWORD",fg='black',font='Times 16 bold italic')
    password.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
    passbox = tkinter.Entry(root,show="*",font="arial 15 bold")
    passbox.place(relx=0.435,rely=0.7,relwidth=0.15,relheight=0.05)
    login = tkinter.Button(root, text="LOGIN", command=GET,font="arial 12 bold",fg='white',bg='indian red',bd=5)
    login.place(relx=0.46,rely=0.8, relwidth=0.1,relheight=0.05)
    

    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()
