from tkinter import*
import datetime
import time
import ttkthemes
import pymysql
from tkinter import ttk,messagebox
from PIL import ImageTk

#functions

def show():
    global mycursor, con
    try:
        con=pymysql.connect(host='localhost',user='root',password='Admin123')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error','Invalid Details',parent=user_window)
        return
    query='use studentdata'
    mycursor.execute(query)
    query='select student.id,name,course,status,date,time from student,attendance where attendance.id=%s'
    mycursor.execute(query,(idEntry.get()))
    fetched_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values=data)




def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        user_window.destroy()
    else:
        pass

def login_page():
    user_window.destroy()
    import signin

def clock():
    date=time.strftime('%d/%m/%Y')
    current_time=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'  Date:{date}\nTime:{current_time}')
    datetimeLabel.after(1000,clock)

count=0
text=''
def slider():
    global text, count
    if count==len(s):
        count=0
        text=''
    text=text+s[count] #s
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

#GUI

user_window=ttkthemes.ThemedTk()
user_window.get_themes()
user_window.set_theme('radiance')
user_window.title('Student Page')
user_window.resizable(0,0)
user_window.geometry('950x560+100+0')

datetimeLabel=Label(user_window,font=('times new roman',18,'bold'),fg='firebrick1')
datetimeLabel.place(x=5,y=5)
clock() 

s='Attendance Tracking System'
sliderLabel=Label(user_window,text='s',font=('arial',28,'italic bold'),fg='firebrick1',width=30)
sliderLabel.place(x=200,y=0)
slider()

idLabel=Label(user_window,text='ID:',font=('arial',15,'bold'),foreground='Red4')
idLabel.place(x=0,y=100)
idEntry=Entry(user_window,font=('arial',15,'bold'),width=20)
idEntry.place(x=80,y=100)

submitButton=ttk.Button(user_window,text='Show',command=show,cursor='hand2')
submitButton.place(x=30,y=150)


logoutButton=ttk.Button(user_window,text='Log Out',command=login_page,cursor='hand2')
logoutButton.place(x=820,y=0)

exitButton=ttk.Button(user_window,text='Exit',command=iexit)
exitButton.place(x=820,y=500)


logo_image=PhotoImage(file='E:/Attendance_tracking_system/college_img/students.png')
logo_Label=Label(user_window,image=logo_image)
logo_Label.place(x=400,y=80)


frame1=Frame(user_window,bg='red')
frame1.place(x=200,y=150,width=500,height=400)

scrollBarX=Scrollbar(frame1,orient=HORIZONTAL)
scrollBarY=Scrollbar(frame1,orient=VERTICAL)

student_table=ttk.Treeview(frame1,columns=('Id','Name','Course','Attendance','Date','Time'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=student_table.xview)
scrollBarY.config(command=student_table.yview)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
student_table.pack(fill=BOTH,expand=1)

student_table.heading('Id',text='Id')
student_table.heading('Name',text='Name')
student_table.heading('Course',text='Course')
student_table.heading('Attendance',text='Attendance')
student_table.heading('Date',text='Date')
student_table.heading('Time',text='Time')

student_table.config(show='headings')
student_table.column('Id',width=50,anchor=CENTER)
student_table.column('Name',width=200,anchor=CENTER)
student_table.column('Course',width=200,anchor=CENTER)
student_table.column('Attendance',width=100,anchor=CENTER)
student_table.column('Date',width=100,anchor=CENTER)
student_table.column('Time',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial',15,'bold'),foreground='red4')
user_window.mainloop()