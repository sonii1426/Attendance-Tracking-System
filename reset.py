from tkinter import*
from PIL import ImageTk
#Functions
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
reset_window=Tk()
reset_window.title('Reset Password')
reset_window.resizable(False,False)

background=ImageTk.PhotoImage(file="E:/Attendance_tracking_system/college_img/background.jpg")
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

submitButton=Button(reset_window,text='SUBMIT',font=('Martian Mono',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=18,cursor='hand2')
submitButton.place(x=485,y=350)

reset_window.mainloop()