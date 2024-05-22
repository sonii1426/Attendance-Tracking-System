from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# GUI FOR RESET

def forget_pass():

    def change_pass():
        if usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpwdEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=reset_window)
        elif passwordEntry.get()!=confirmpwdEntry.get():
            messagebox.showerror('Error','New password and confirm password are not matching',parent=reset_window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='Admin123',database='admindata')
            mycursor=con.cursor()
            query='select* from data where username=%s'
            mycursor.execute(query,(usernameEntry.get()))
            row=mycursor.fetchone
            if row==None:
                messagebox.showerror('Error','Incorrect Password',parent=reset_window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(passwordEntry.get(),usernameEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is Reset Login with new password',parent=reset_window)
                reset_window.destroy()

    def user_enter(event):
        if usernameEntry.get()=='Username':
            usernameEntry.delete(0,END)

    def password_enter(event):
        if passwordEntry.get()=='New Password':
            passwordEntry.delete(0,END)

    def confirmpwd_enter(event):
        if confirmpwdEntry.get()=='Confirm Password':
            confirmpwdEntry.delete(0,END)

    #GUI part
    reset_window=Toplevel()
    reset_window.title('Reset Password')
    reset_window.resizable(False,False)

    background=ImageTk.PhotoImage(file="C:/Users/dtdik/OneDrive/Desktop/Attendance_tracking_system/college_img/background.jpg")
    bgLabel=Label(reset_window,image=background)
    bgLabel.grid()

    heading=Label(reset_window,text='Reset Password',font=('Martian Mono',22,'bold'),bg='white',fg='firebrick1')
    heading.place(x=485,y=60)

    usernameEntry=Entry(reset_window,width=25,font=('Martian Mono',10,'bold'),bd=0,fg='firebrick1')
    usernameEntry.place(x=485,y=125)
    usernameEntry.insert(0,'Username')
    usernameEntry.bind('<FocusIn>',user_enter)

    frame1=Frame(reset_window,width=250,height=2,bg='firebrick1')
    frame1.place(x=485,y=150)

    passwordEntry=Entry(reset_window,width=25,font=('Martian Mono',10,'bold'),bd=0,fg='firebrick1')
    passwordEntry.place(x=485,y=190)
    passwordEntry.insert(0,'New Password')
    passwordEntry.bind('<FocusIn>',password_enter)

    frame2=Frame(reset_window,width=250,height=2,bg='firebrick1')
    frame2.place(x=485,y=215)

    confirmpwdEntry=Entry(reset_window,width=25,font=('Martian Mono',10,'bold'),bd=0,fg='firebrick1')
    confirmpwdEntry.place(x=485,y=260)
    confirmpwdEntry.insert(0,'Confirm Password')
    confirmpwdEntry.bind('<FocusIn>',confirmpwd_enter)

    frame3=Frame(reset_window,width=250,height=2,bg='firebrick1')
    frame3.place(x=485,y=290)

    submitButton=Button(reset_window,text='SUBMIT',font=('Martian Mono',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=18,cursor='hand2',command=change_pass)
    submitButton.place(x=485,y=350)

    reset_window.mainloop() 


#Functions 

def signup_page():
    Login_window.destroy()
    import signup

def user_login():
    if emailEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Admin123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use studentdata'
        mycursor.execute(query)
        query='select* from student,attendance where email=%s and password=%s'
        mycursor.execute(query,(emailEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            Login_window.destroy()
            import user

def admin_login():
    if emailEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Admin123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return

        query='use admindata'
        mycursor.execute(query)
        query='select* from data where email=%s and password=%s'
        mycursor.execute(query,(emailEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            Login_window.destroy()
            import admin

def hide():
    openeye.config(file='E:/Attendance_tracking_system/college_img/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='E:/Attendance_tracking_system/college_img/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if emailEntry.get()=='Email':
        emailEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)



#GUI part
Login_window=Tk()
Login_window.title('SignIn Page')
Login_window.resizable(False,False)

background=ImageTk.PhotoImage(file="E:/Attendance_tracking_system/college_img/bg.jpg")
bgLabel=Label(Login_window,image=background)
bgLabel.grid()


heading=Label(Login_window,text='User LogIn',font=('Martian Mono',22,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

emailEntry=Entry(Login_window,width=25,font=('Martian Mono',10,'bold'),bd=0,fg='firebrick1')
emailEntry.place(x=580,y=200)
emailEntry.insert(0,'Email')
emailEntry.bind('<FocusIn>',user_enter)

frame1=Frame(Login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(Login_window,width=25,font=('Martian Mono',10,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(Login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file="E:/Attendance_tracking_system/college_img/openeye.png")
eyeButton=Button(Login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(Login_window,text='Forgeot password?',font=('Martian Mono',10,'bold'),bd=0,bg='white',fg='firebrick1',activebackground='white',cursor='hand2',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(Login_window,text='User LogIn',font=('Martian Mono',10,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=12,cursor='hand2',command=user_login)
loginButton.place(x=578,y=350)

adminButton=Button(Login_window,text='Admin LogIn',font=('Martian Mono',10,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=12,command=admin_login,cursor='hand2')
adminButton.place(x=730,y=350)

orLable=Label(Login_window,text='-------------- OR ---------------',font=('Open Sans',16),bg='white',fg='firebrick1')
orLable.place(x=583,y=400)

fb_logo=PhotoImage(file="E:/Attendance_tracking_system/college_img/facebook.png")
fbLabel=Label(Login_window,image=fb_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file="E:/Attendance_tracking_system/college_img/google.png")
goggleLabel=Label(Login_window,image=google_logo,bg='white')
goggleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file="E:/Attendance_tracking_system/college_img/twitter.png")
twitterLabel=Label(Login_window,image=twitter_logo,bg='white',width=32,height=32)
twitterLabel.place(x=740,y=440)

donthaveaccount=Label(Login_window,text='Dont have an account?',font=('Martian Mono',10,'bold'),bg='white',fg='firebrick1')
donthaveaccount.place(x=590,y=500)

signupButton=Button(Login_window,text='SignUP',font=('Martian Mono',10,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=signup_page)
signupButton.place(x=740,y=500)
Login_window.mainloop()