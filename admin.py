from tkinter import*
import ttkthemes
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import pymysql
import mysql.connector
from PIL import ImageTk
import datetime
import time
# Functions

def take_attendance():
    def add_attendance():
        if idEntry.get()=='' or statuscombo.get()=='Status' or timeEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=status)
        else:
            try:
                query='insert into attendance values(%s,%s,%s,%s,%s)'
                mycursor.execute(query,(sidEntry.get(),idEntry.get(),statuscombo.get(),cal.get_date(),timeEntry.get()))
                con.commit()
                result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=status)
                if result:
                    idEntry.delete(0,END)
                    statuscombo.delete(0,END)
                    cal.delete(0,END)
                    timeEntry.delete(0,END)
                else:
                    pass

            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=status)
                return




    status=Toplevel()
    status.title('Attendance')
    status.resizable(0,0)
    sidLabel=Label(status,text='SID',font=('times new roman',15,'bold'),foreground='red4')
    sidLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    sidEntry = Entry(status, font=('roman', 15, 'bold'), width=24)
    sidEntry.grid(row=0, column=1, pady=15, padx=10)

    idLabel=Label(status,text='ID',font=('times new roman',15,'bold'),foreground='red4')
    idLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(status, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=1, column=1, pady=15, padx=10)

    statusLabel=Label(status,text='Attendance',font=('times new roman',15,'bold'),foreground='red4')
    statusLabel.grid(row=2,column=0,sticky=W,padx=30,pady=15)
    statuscombo=ttk.Combobox(status,width=24,values=('Status','Present','Absent'),font=('roman',15,'bold'),state='readonly')
    statuscombo.set('Status')
    statuscombo.grid(row=2, column=1, pady=15, padx=10)

    dateLabel=Label(status,text='Date',font=('times new roman',15,'bold'),foreground='red4')
    dateLabel.grid(row=3,column=0,sticky=W,padx=30,pady=15)
    cal=DateEntry(status,selectmod='Day')
    cal.grid(row=3, column=1, pady=15, padx=10)

    timeLabel=Label(status,text='Time',font=('times new roman',15,'bold'),foreground='red4')
    timeLabel.grid(row=4,column=0,sticky=W,padx=30,pady=15)
    timeEntry=Entry(status, font=('roman', 15, 'bold'), width=24)
    timeEntry.grid(row=4,column=1,padx=10,pady=15)



    submitButton=ttk.Button(status,text='Submit',command=add_attendance)
    submitButton.grid(row=5,columnspan=2,padx=15)


def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        admin_window.destroy()
    else:
        pass


def toplevel_data(title,button_text,command):
    global idEntry,nameEntry,coursecombo,emailEntry,passwordEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.resizable(0,0)
    screen.grab_set()
    idLabel=Label(screen,text='ID',font=('times new roman',15,'bold'),foreground='red4')
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel=Label(screen,text='Name',font=('times new roman',15,'bold'),foreground='red4')
    nameLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=2, column=1, pady=15, padx=10)

    courseLabel=Label(screen,text='Course',font=('times new roman',15,'bold'),foreground='red4')
    courseLabel.grid(row=3,column=0,sticky='w',padx=30,pady=15)
    coursecombo=ttk.Combobox(screen,width=24,values=('select course','FyBscIT','SyBscIT','TyBscIT','FYBCA','SyBca','TyBca'),font=('roman',15,'bold'),state='readonly')
    coursecombo.set('Select Course')
    coursecombo.grid(row=3, column=1, pady=15, padx=10)


    emailLabel=Label(screen,text='Email',font=('times new roman',15,'bold'),foreground='red4')
    emailLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=4, column=1, pady=15, padx=10)

    passwordLabel=Label(screen,text='Password',font=('times new roman',15,'bold'),foreground='red4')
    passwordLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    passwordEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    passwordEntry.grid(row=5, column=1, pady=15, padx=10)

    submitButton=ttk.Button(screen,text=button_text,command=command)
    submitButton.grid(row=6,columnspan=2,padx=15)

    if title=='UPDATE STUDENT':
        indexing=student_table.focus()
        print(indexing)
        content=student_table.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        coursecombo.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        passwordEntry.insert(0,listdata[4])



def update_data():
    query='update student set name=%s,course=%s,email=%s,password=%s,where id=%s'
    mycursor.execute(query,(nameEntry.get(),coursecombo.get(),emailEntry.get(),passwordEntry.get(),idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id{idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()

    
def show_student():
    query='select student.id,name,course,email,password,status,date,time from student,attendance'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values=data)

def delete_student():
    indexing=student_table.focus()
    print(indexing)
    content=student_table.item(indexing)
    content_id=content['values'][0]
    query='delete from student,attendance where student.id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted','ID {content_id} is deleted successfully')
    query='select* from student,attendance'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values=data)


def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or coursecombo.get()=='' or emailEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=screen)

    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),coursecombo.get(),emailEntry.get(),passwordEntry.get()))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                coursecombo.delete(0,END)
                emailEntry.delete(0,END)
                passwordEntry.delete(0,END)
            else:
                pass

        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return

        query='select* from student,attendance'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            datalist=list(data)
            student_table.insert('',END,values=datalist)



def connect_database():
    def connect():
        global mycursor, con
        try:
            con=pymysql.connect(host='localhost',user='root',password='Admin123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentdata'
            mycursor.execute(query)
            query='use studentdata'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(50),course varchar(50),email varchar(50),password varchar(50))'
            mycursor.execute(query)
            query='create table attendance(sid int not null primary key,id int references student.id,status varchar(30),date varchar(30),time varchar(30))'
            mycursor.execute(query)
        except:
            query='use studentdata'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database connection is successful',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        attendanceButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20))
    usernameLabel.grid(row=1,column=0,padx=20)
    userEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20))
    passwordLabel.grid(row=2,column=0,padx=20)
    passEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passEntry.grid(row=2,column=1,padx=40,pady=20)

    connButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connButton.grid(row=3,columnspan=2)






def login_page():
    admin_window.destroy()
    import signin

def clock():
    global date,current_time
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


admin_window=ttkthemes.ThemedTk()
admin_window.get_themes()
admin_window.set_theme('radiance')
admin_window.title('Admin Page')
admin_window.resizable(0,0)
admin_window.geometry('1174x600+100+0')

datetimeLabel=Label(admin_window,font=('times new roman',18,'bold'),fg='firebrick1')
datetimeLabel.place(x=5,y=5)
clock() 

s='Attendance Tracking System'
sliderLabel=Label(admin_window,text='s',font=('arial',28,'italic bold'),width=30,fg='firebrick1')
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(admin_window,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)
logoutButton=ttk.Button(admin_window,text='Log Out',cursor='hand2',command=login_page)
logoutButton.place(x=980,y=40)


leftFrame=Frame(admin_window)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='E:/Attendance_tracking_system/college_img/students.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','ADD STUDENT',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','UPDATE',update_data))
updatestudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=4,column=0,pady=20)

attendanceButton=ttk.Button(leftFrame,text='Attendance',width=25,cursor='hand2',state=DISABLED,command=take_attendance)
attendanceButton.grid(row=5,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=6,column=0,pady=20)






rightFrame=Frame(admin_window)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
#Treeview
student_table=ttk.Treeview(rightFrame,columns=('Id','Name','Course','Email','Password','Status','Date','Time'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=student_table.xview)
scrollBarY.config(command=student_table.yview)
scrollBarX.pack(side=TOP,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
student_table.pack(fill=BOTH,expand=0.5)

student_table.heading('Id',text='Id')
student_table.heading('Name',text='Name')
student_table.heading('Course',text='Course')
student_table.heading('Email',text='Email')
student_table.heading('Password',text='Password')
student_table.heading('Status',text='Attendance')
student_table.heading('Date',text='Date')
student_table.heading('Time',text='Time')

student_table.column('Id',width=50,anchor=CENTER)
student_table.column('Name',width=300,anchor=CENTER)
student_table.column('Course',width=300,anchor=CENTER)
student_table.column('Email',width=300,anchor=CENTER)
student_table.column('Password',width=300,anchor=CENTER)
student_table.column('Status',width=200,anchor=CENTER)
student_table.column('Date',width=100,anchor=CENTER)
student_table.column('Time',width=100,anchor=CENTER)


student_table.config(show='headings')
style=ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial',15,'bold'),foreground='red4')
admin_window.mainloop()