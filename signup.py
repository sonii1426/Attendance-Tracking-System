#importing#
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#Logic & Functions 

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')

    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Condition')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Admin123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query='create database admindata' #create database
            mycursor.execute(query)
            query='use admindata' #use database
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))' #create table
            mycursor.execute(query)
        except:
            mycursor.execute('use admindata')
            
        query='select* from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already Exists')
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)' #insertion query
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin

#GUI start from here

signup_window=Tk()
signup_window.title('SignUp Page')
signup_window.resizable(False,False)

#This is a bg img

background=ImageTk.PhotoImage(file="E:/Attendance_tracking_system/college_img/bg.jpg")
bgLabel=Label(signup_window,image=background)
bgLabel.grid()


frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)
heading=Label(frame,text='Create An Account',font=('Martian Mono',22,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=('Martian Mono',10,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Martian Mono',10,'bold'),bg='firebrick1',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=10)
passwordEntry=Entry(frame,width=30,font=('Martian Mono',10,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


confirmLabel=Label(frame,text='Confirm Password',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=10)
confirmEntry=Entry(frame,width=30,font=('Martian Mono',10,'bold'),bg='firebrick1',fg='white')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)
check=IntVar()
termsandcondition=Checkbutton(frame,text='I agree to the Terms & Condition',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='SignUp',font=('Martian Mono',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text='Already have an account?',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log In',font=('Martian Mono',10,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=200,y=400)
signup_window.mainloop()



        