from tkinter import *
import sqlite3
from tkinter import messagebox as msg
import os
import sys



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#sqlite3 connection
conn = sqlite3.connect(resource_path('ld.db'))
cursor = conn.cursor()


#code for main window(root) connection to tkinter
root = Tk()
root.geometry('500x600')
root.title('LIBRARY DASHBOARD')
root.maxsize(500,600)
root.minsize(500,600)



#code for SEARCH ISSUED BOOKS button on issuedStBookDetails() function page----
def SIBooks():
    try:
        cursor.execute('select book.id,book.name,book.author from book,student,issue where book.id = issue.id and student.roll=issue.roll and issue.roll='+issuedRoll.get()+' order by book.id')

    except sqlite3.OperationalError:
        msg.showerror('ERROR','OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE')
        issuedStBookDetails()
    else:
        if cursor.fetchall()==[]:
            msg.showinfo('ISSUED BOOKS DETAILS','NO ISSUED BOOK FOUND TO THIS ROLL NUMBER')
            issuedStBookDetails()
        else:
            cursor.execute('select book.id,book.name,book.author from book,student,issue where book.id = issue.id and student.roll=issue.roll and issue.roll='+issuedRoll.get()+' order by book.id')            
            SIBooksFrame = Frame(root,bg='#fffbe6',width =500,height=600)
            SIBooksFrame.grid(row=0,column=0)
            SIBooksFrame.pack_propagate(False)
            SIBooksFrame.tkraise()

            Label(SIBooksFrame, text='ISSUED BOOKS DETAILS',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',20,'bold')).pack(pady =(55,20))
            listbox = Listbox(SIBooksFrame,height = 16,width = 500,bg = '#fffbe6',font =('Arial',12,'bold'),fg = 'black')
            for i in cursor.fetchall():
                listbox.insert(END,i)
            listbox.pack(padx=20)
            msg.showinfo('DETAILS FORMAT','ID {BOOK NAME} {BOOK AUTHOR}')
            Button(SIBooksFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= issuedStBookDetails).pack(pady = (20,0))
            Button(SIBooksFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)



#code for ISSUE BOOK DETAILS on viewstudentdetails() function page
def issuedStBookDetails():
    ISBDFrame = Frame(root,bg='#fffbe6',width =500,height=600)
    ISBDFrame.grid(row=0,column=0)
    ISBDFrame.pack_propagate(False)
    ISBDFrame.tkraise()

    Label(ISBDFrame,text = 'ISSUED BOOKS DETAILS',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 55)
    Label(ISBDFrame,text = 'ENTER STUDENT ROLL', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (60,3))
    global issuedRoll
    issuedRoll=Entry(ISBDFrame,font=('Arial',12,'bold'),justify = 'center')
    issuedRoll.focus()
    issuedRoll.pack(pady = (3,15))

    #buttons on issuedStBookDetails() function page

    Button(ISBDFrame,text ='SEARCH ISSUED BOOKS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',11,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 20,cursor= 'hand2',command =SIBooks).pack(pady =(35,10))
    Button(ISBDFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=viewstudentDetails).pack()




#code for ALL STUDENT DETAILS button on viewstudentdetails() function page
def allStudentDetails():
    cursor.execute('select * from student order by roll')
    AsDFrame = Frame(root,bg='#fffbe6',width=500,height =600)
    AsDFrame.grid(row=0,column=0)
    AsDFrame.pack_propagate(False)
    AsDFrame.tkraise()
        
    listbox = Listbox(AsDFrame,height = 20,width = 500,bg = '#fffbe6',
                          font =('Arial',12,'bold'),fg = 'black')
    Label(AsDFrame,text = 'ALL STUDENTS DETAILS',fg='#80669d',bg='#fffbe6',font=('TkMenuFont',20,'bold')).pack(pady=(55,20))
    for i in cursor.fetchall():
        listbox.insert(END,i)
    listbox.pack(padx=20)
    msg.showinfo('DETAILS FORMAT','ROLL {NAME} PHONE_NUMBER')
    Button(AsDFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= viewstudentDetails).pack(pady = (20,0))




#code for SEARCH button on studentByName() function page
def searchStByName():
    cursor.execute('select *from student where name like "'+studentName.get()+'%"')
    if cursor.fetchall() ==[]:
        msg.showinfo('STUDENT DETAILS','NO STUDENT FOUND')
        studentByName()
    else:
        cursor.execute('select * from student where name like "'+studentName.get()+'%" order by roll')
        searchStFrame = Frame(root,bg='#fffbe6',width =500,height=600)
        searchStFrame.grid(row=0,column=0)
        searchStFrame.pack_propagate(False)
        searchStFrame.tkraise()

        Label(searchStFrame, text='STUDENT DETAILS',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',20,'bold')).pack(pady =(55,20))
        cursor.execute('select * from student where name like "'+studentName.get()+'%" order by roll')
        listbox = Listbox(searchStFrame,height = 16,width = 500,bg = '#fffbe6',font =('Arial',12,'bold'),fg = 'black')
        for i in cursor.fetchall():
            listbox.insert(END,i)
        listbox.pack(padx=20)
        msg.showinfo('DETAILS FORMAT','ROLL {NAME} PHONE_NUMBER')
        Button(searchStFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= studentByName).pack(pady = (20,0))
        Button(searchStFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
    




#code for SEARCH BY NAME on viewstudentDetails() function page
def studentByName():
    StBNameFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    StBNameFrame.grid(row=0,column =0)
    StBNameFrame.pack_propagate(False)
    StBNameFrame.tkraise()

    Label(StBNameFrame,text = 'VIEW STUDENT DETAILS',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 55)
    Label(StBNameFrame,text = 'ENTER STUDENT NAME', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (60,3))
    global studentName
    studentName=Entry(StBNameFrame,font=('Arial',12,'bold'),justify = 'center')
    studentName.focus()
    studentName.pack(pady = (3,15))

    #buttons on studentbyName() function page

    Button(StBNameFrame,text ='SEARCH',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=searchStByName).pack(pady =(35,10))
    Button(StBNameFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=viewstudentDetails).pack()





#code for DETAILS button on viewstudentDetails() function page
def studentDetails():
    try:
        cursor.execute('select * from student where roll = '+viewRoll.get())
    except sqlite3.OperationalError:
        msg.showerror('ERROR','OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE')
        viewstudentDetails()
    else:
        if cursor.fetchall()==[]:
            msg.showinfo('STUDENT DETAILS','NO STUDENT FOUND WITH THIS ROLL NUMBER')
            viewstudentDetails()
        else:
            cursor.execute('select * from student where roll = '+viewRoll.get())
            msg.showinfo('STUDENT DETAILS',cursor.fetchall())        
            viewstudentDetails()



#code for ADD button on addStudent() frame
def addStButton():
    addStButtonframe = Frame(root,bg = '#fffbe6',width = 500, height = 600)
    addStButtonframe.grid(row = 0,column = 0)
    addStButtonframe.pack_propagate(False)
    addStButtonframe.tkraise()

    
    try:
        cursor.execute("insert into student values ("+Stroll.get()+",'"+Stname.get()+"' ,"+Stphone.get()+")")
    except sqlite3.IntegrityError :
        cursor.execute('select * from student where roll ='+Stroll.get())
        Label(addStButtonframe,text = 'STUDENT OF THIS ROLL IS ALREADY PRESENT', fg ='red', bg = '#fffbe6',font=('TkMenuFont',12,'bold')).pack(pady =(180,40))
        Label(addStButtonframe, text = cursor.fetchall(), fg = 'black',bg = '#fffbe6',font = ('Arial',10,'bold')).pack(pady=(30,140))
        Button(addStButtonframe,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=addStudent).pack()
        Button(addStButtonframe,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady = 10)
          

    except sqlite3.OperationalError:
        
        Label(addStButtonframe, text = 'OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE',fg='red',bg = '#fffbe6',font =('TkMenuFont',12,'bold')).pack(pady =200)
        
        Button(addStButtonframe,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=addStudent).pack()
        Button(addStButtonframe,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)


    else :
        conn.commit()
        cursor.execute('select * from student where roll ='+Stroll.get())
        Label(addStButtonframe,text = 'DONE, SUCCESSFULLY ADDED',fg ='#537FE7',bg = '#fffbe6',font =('TkMenuFont',20,'bold')).pack(pady = (180,20))
        Label(addStButtonframe,text=cursor.fetchall(),fg = 'black',bg='#fffbe6', font = ('Arial',10,'bold')).pack(pady=(30,140))
        Button(addStButtonframe,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=addStudent).pack()
        Button(addStButtonframe,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)






#code for ADD STUDENT button on viewstudentDetails() function page
def addStudent():
    addStudentFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    addStudentFrame.grid(row=0,column =0)
    addStudentFrame.pack_propagate(False)
    addStudentFrame.tkraise()

    Label(addStudentFrame,text = 'ADD STUDENT',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',25,'bold')).pack(pady=35)

    Label(addStudentFrame,text = 'ENTER STUDENT ROLL', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    global Stroll,Stname,Stphone
    Stroll=Entry(addStudentFrame,font=('Arial',12,'bold'),justify = 'center')
    Stroll.focus()
    Stroll.pack(pady = (3,15))

    Label(addStudentFrame,text = 'ENTER STUDENT NAME', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    Stname = Entry(addStudentFrame,font=('Arial',12,'bold'),justify = 'right')
    Stname.pack(pady =(3,15))

    Label(addStudentFrame,text = 'ENTER STUDENT PHONE', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    Stphone = Entry(addStudentFrame,font=('Arial',12,'bold'),justify = 'center')
    Stphone.pack(pady=(3,15))


    #buttons of addStudent() function page
    Button(addStudentFrame,text ='ADD',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command =addStButton).pack(pady=(30,0))

    Button(addStudentFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= viewstudentDetails).pack(pady = 10)
    



#code for STUDENT DETAILS button on home page
def viewstudentDetails():
    viewsdetailsFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    viewsdetailsFrame.grid(row=0,column =0)
    viewsdetailsFrame.pack_propagate(False)
    viewsdetailsFrame.tkraise()

    Label(viewsdetailsFrame,text = 'VIEW STUDENT DETAILS',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 55)
    global viewRoll
    Label(viewsdetailsFrame,text = 'ENTER STUDENT ROLL', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (0,3))
    viewRoll=Entry(viewsdetailsFrame,font=('Arial',12,'bold'),justify = 'center')
    viewRoll.focus()
    viewRoll.pack(pady = (3,15))

    #buttons on viewstudentDetails() page
    Button(viewsdetailsFrame,text ='DETAILS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 9,cursor='hand2',command=studentDetails).pack()
    
    Button(viewsdetailsFrame,text = 'ADD STUDENT',bg ='#E5BEEC',fg='#2A3F4F',font=('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#e5beec',width =13,cursor ='hand2',command=addStudent).pack(pady=(30,0))
    Button(viewsdetailsFrame,text ='SEARCH BY NAME',bg ='#E5BEEC',fg = '#2A3F4F',font=('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width =15,cursor='hand2',command=studentByName).pack(pady=10)
    Button(viewsdetailsFrame,text ='ALL STUDENTS DETAILS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 20,cursor='hand2',command=allStudentDetails).pack(pady = (0,10))
    Button(viewsdetailsFrame,text ='ISSUED BOOKS DETAILS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 21,cursor='hand2',command=issuedStBookDetails).pack(pady = 0)
    Button(viewsdetailsFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= loadFrame1).pack(pady = 30,side='bottom')
    





#code for (ISSUED BOOK DETAILS) in viewbookdetails() function page
def IssuedBooksDetails():
    IBDFrame = Frame(root,bg='#fffbe6',width =500,height=600)
    IBDFrame.grid(row=0,column=0)
    IBDFrame.pack_propagate(False)
    IBDFrame.tkraise()

    Label(IBDFrame, text='ISSUED BOOKS DETAILS',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',20,'bold')).pack(pady =(55,20))
    cursor.execute('select book.id,book.name,author,student.* from book,student,issue where book.id = issue.id and student.roll=issue.roll order by book.id')
    listbox = Listbox(IBDFrame,height = 20,width = 500,bg = '#fffbe6',font =('Arial',12,'bold'),fg = 'black')
    for i in cursor.fetchall():
        listbox.insert(END,i)
    listbox.pack(padx=20)
    msg.showinfo('DETAILS FORMAT','ID {BOOK NAME} {AUTHOR NAME} STUDENT_ROLL {STUDENT NAME} STUDENT_PHONE')
    Button(IBDFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= viewbookDetails).pack(pady = (20,0))




#code for (ALL BOOKS DETAILS) in viewbookdetails() function page
def AllBooksDetails():
    try:
        cursor.execute('select * from book order by id')
    except sqlite3.OperationalError:
        msg.showerror('ERROR','OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE')
        viewbookDetails()
    else:
        ABDFrame = Frame(root,bg='#fffbe6',width=500,height =600)
        ABDFrame.grid(row=0,column=0)
        ABDFrame.pack_propagate(False)
        ABDFrame.tkraise()
        
        listbox = Listbox(ABDFrame,height = 20,width = 500,bg = '#fffbe6',
                          font =('Arial',12,'bold'),fg = 'black')
        Label(ABDFrame,text = 'ALL BOOKS DETAILS',fg='#80669d',bg='#fffbe6',font=('TkMenuFont',20,'bold')).pack(pady=(55,20))
        for i in cursor.fetchall():
            listbox.insert(END,i)
        listbox.pack(padx=20)
        msg.showinfo('DETAILS FORMAT','ID {BOOK NAME} {AUTHOR NAME} QTY')
        Button(ABDFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= viewbookDetails).pack(pady = (20,0))

        
#code for SEARCH button on searchbyName() function page
def search():
    cursor.execute('select *from book where name like "'+bookName.get()+'%"')
    if cursor.fetchall() ==[]:
        msg.showinfo('BOOK DETAILS','NO BOOK FOUND')
        searchbyName()
    else:
        cursor.execute('select * from book where name like "'+bookName.get()+'%"')
        searchFrame = Frame(root,bg='#fffbe6',width =500,height=600)
        searchFrame.grid(row=0,column=0)
        searchFrame.pack_propagate(False)
        searchFrame.tkraise()

        Label(searchFrame, text='BOOK DETAILS',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',20,'bold')).pack(pady =(55,20))
        cursor.execute('select * from book where name like "'+bookName.get()+'%"')
        listbox = Listbox(searchFrame,height = 16,width = 500,bg = '#fffbe6',font =('Arial',12,'bold'),fg = 'black')
        for i in cursor.fetchall():
            listbox.insert(END,i)
        listbox.pack(padx=20)
        msg.showinfo('DETAILS FORMAT','ID {BOOK NAME} {AUTHOR NAME} QTY')
        Button(searchFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= searchbyName).pack(pady = (20,0))
        Button(searchFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
    



#code for (SEARCH BY NAME) on viewbookdetails() function page
def searchbyName():
    SBNameFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    SBNameFrame.grid(row=0,column =0)
    SBNameFrame.pack_propagate(False)
    SBNameFrame.tkraise()

    Label(SBNameFrame,text = 'VIEW BOOK DETAILS',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 55)
    Label(SBNameFrame,text = 'ENTER BOOK NAME', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (60,3))
    global bookName
    bookName=Entry(SBNameFrame,font=('Arial',12,'bold'),justify = 'center')
    bookName.focus()
    bookName.pack(pady = (3,15))

    #buttons on searchbyName() function page

    Button(SBNameFrame,text ='SEARCH',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=search).pack(pady =(35,10))
    Button(SBNameFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=viewbookDetails).pack()

    
    


#code for details button on viewbookdetails() function page
def details():
    try:
        cursor.execute('select * from book where id = '+viewbookId.get())
    except sqlite3.OperationalError:
        msg.showerror('ERROR','OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE')
        viewbookDetails()
    else:
        if cursor.fetchall()==[]:
            msg.showinfo('BOOK DETAILS','NO BOOK FOUND')
            viewbookDetails()
        else:
            cursor.execute('select * from book where id = '+viewbookId.get())
            msg.showinfo('BOOK DETAILS',cursor.fetchall())        
            viewbookDetails()



#code for veiw book details button in home page
def viewbookDetails():
    viewbdetailsFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    viewbdetailsFrame.grid(row=0,column =0)
    viewbdetailsFrame.pack_propagate(False)
    viewbdetailsFrame.tkraise()

    Label(viewbdetailsFrame,text = 'VIEW BOOK DETAILS',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 55)
    global viewbookId
    Label(viewbdetailsFrame,text = 'ENTER BOOK ID', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (0,3))
    viewbookId=Entry(viewbdetailsFrame,font=('Arial',12,'bold'),justify = 'center')
    viewbookId.focus()
    viewbookId.pack(pady = (3,15))

    #buttons on viewbookDetails() page
    Button(viewbdetailsFrame,text ='DETAILS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 8,cursor='hand2',command =details).pack()

    Button(viewbdetailsFrame,text ='SEARCH BY NAME',bg ='#E5BEEC',fg = '#2A3F4F',font=('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width =15,cursor='hand2',command=searchbyName).pack(pady=(30,0))
    Button(viewbdetailsFrame,text ='ALL BOOKS DETAILS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 17,cursor='hand2',command = AllBooksDetails).pack(pady = 10)
    Button(viewbdetailsFrame,text ='ISSUED BOOKS DETAILS',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',10,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 21,cursor='hand2',command=IssuedBooksDetails).pack(pady = 0)
    Button(viewbdetailsFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= loadFrame1).pack(pady = 30,side='bottom')
    

    

#code for return button on Return() funtion page
def ReturnButton():
    returnbuttonFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    returnbuttonFrame.grid(row = 0,column=0)
    returnbuttonFrame.pack_propagate(False)
    returnbuttonFrame.tkraise()

    try :
        cursor.execute('delete from issue where id ='+returnbookId.get()+' and roll='+returnstudentRoll.get())
    except sqlite3.OperationalError:
        Label(returnbuttonFrame, text = 'OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE',fg='red',bg = '#fffbe6',font =('TkMenuFont',12,'bold')).pack(pady =200)
        
        Button(returnbuttonFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=Return).pack()
        Button(returnbuttonFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
    else:
        cursor.execute('update book set copy = copy+1 where id ='+returnbookId.get())
        conn.commit()
        Label(returnbuttonFrame,text = 'DONE, SUCCESSFULLY RETURNED',fg ='#537FE7',bg = '#fffbe6',font =('TkMenuFont',18,'bold')).pack(pady = (180))
        Button(returnbuttonFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=Return).pack()
        Button(returnbuttonFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)




#code for return book on home page
def Return():
    returnFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    returnFrame.grid(row =0,column =0)
    returnFrame.pack_propagate(False)
    returnFrame.tkraise()

    Label(returnFrame,text = 'RETURN BOOK TO LIBRARY',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 65)
    global returnbookId,returnstudentRoll

    Label(returnFrame,text = 'ENTER BOOK ID', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (30,3))
    returnbookId=Entry(returnFrame,font=('Arial',12,'bold'),justify = 'center')
    returnbookId.focus()
    returnbookId.pack(pady = (3,15))

    Label(returnFrame,text = 'ENTER STUDENT ROLL NUMBER', fg = 'black',bg='#fffbe6',font = ('Arial',16,'bold')).pack(pady=(25,3))
    returnstudentRoll=Entry(returnFrame,font=('Arial',12,'bold'),justify = 'center')
    returnstudentRoll.pack(pady = (3,45))

    #button in Return() function

    returnButton = Button(returnFrame,text ='RETURN',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 10,cursor= 'hand2',command = ReturnButton)
    returnButton.pack()

    Button(returnFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= loadFrame1).pack(pady = 10)
    




#code for issue button on issueBookFrame() function
def issueButtonFrame():
    issuebuttonFrame = Frame(root,bg = '#fffbe6',width = 500,height = 600)
    issuebuttonFrame.grid(row =0, column =0)
    issuebuttonFrame.pack_propagate(False)
    issuebuttonFrame.tkraise()

    try:
        cursor.execute('pragma foreign_keys = 1')
        cursor.execute('insert into issue values('+issuebookId.get()+','+issuestudentroll.get()+')')
    except sqlite3.OperationalError:
        Label(issuebuttonFrame, text = 'OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE',fg='red',bg = '#fffbe6',font =('TkMenuFont',12,'bold')).pack(pady =200)
        Button(issuebuttonFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=issueBookFrame).pack()
        Button(issuebuttonFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
    
    except sqlite3.IntegrityError :
        Label(issuebuttonFrame, text = 'BOOK ID OR/AND ROLL NUMBER DOES NOT EXIST',fg = 'red',bg ='#fffbe6',font =('TkMenuFont',12,'bold')).pack(pady=200)

        Button(issuebuttonFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=issueBookFrame).pack()
        Button(issuebuttonFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady =10)
    else:
        cursor.execute('update book set copy = copy-1 where id ='+issuebookId.get())
        conn.commit()
        
        Label(issuebuttonFrame,text = 'DONE, SUCCESSFULLY ISSUED',fg ='#537FE7',bg = '#fffbe6',font =('TkMenuFont',20,'bold')).pack(pady = (180,100))
        #Label(issuebuttonFrame,text=cursor.fetchall(),fg = 'black',bg='#fffbe6', font = ('Arial',10,'bold')).pack(pady=(30,140))
        Button(issuebuttonFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=issueBookFrame).pack()
        Button(issuebuttonFrame,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
                    
                
            



#code for issue book button on homepage
def issueBookFrame():
    issuebookFrame =Frame(root,bg = '#fffbe6',width = 500,height = 600)
    issuebookFrame.grid(row =0 ,column = 0)
    issuebookFrame.pack_propagate(False)
    issuebookFrame.tkraise()

    Label(issuebookFrame,text ='ISSUE BOOK',bg = '#fffbe6',fg = '#80669d',font = ('TkMenuFont',25,'bold')).pack(pady=35)

    global issuebookId,issuestudentroll
    
    Label(issuebookFrame,text = 'ENTER BOOK ID', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (30,3))
    issuebookId=Entry(issuebookFrame,font=('Arial',12,'bold'),justify = 'center')
    issuebookId.focus()
    issuebookId.pack(pady = (3,15))

    Label(issuebookFrame,text = 'ENTER STUDENT ROLL NUMBER', fg = 'black',bg='#fffbe6',font = ('Arial',16,'bold')).pack(pady=(25,3))
    issuestudentroll=Entry(issuebookFrame,font=('Arial',12,'bold'),justify = 'center')
    issuestudentroll.pack(pady = (3,45))

    #button in issueBookFrame() function

    issueButton = Button(issuebookFrame,text ='ISSUE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 10,cursor= 'hand2',command=issueButtonFrame)
    issueButton.pack()

    Button(issuebookFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= loadFrame1).pack(pady = 10)






#code for DELETE BOOK button in deletebookFrame() function
def deletebookButton():
    deletebookButton = Frame(root,bg = '#fffbe6',width = 500,height=600)
    deletebookButton.grid(row = 0,column = 0)
    deletebookButton.pack_propagate(False)
    deletebookButton.tkraise()

    try:
        cursor.execute('pragma foreign_keys = ON')
        cursor.execute("delete from book where id="+delbookId.get())
    except sqlite3.OperationalError :
        Label(deletebookButton, text = 'OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE',fg='red',bg = '#fffbe6',font =('TkMenuFont',12,'bold')).pack(pady =200)
        
        Button(deletebookButton,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=deletebookFrame).pack()
        Button(deletebookButton,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
    except sqlite3.IntegrityError:
        Label(deletebookButton,text = 'CANNOT DELETE THIS BOOK BECAUSE',fg = 'red',bg ='#fffbe6',font=('TkMenuFont',15,'bold')).pack(pady=(200,10))
        Label(deletebookButton,text='THIS BOOK IS ISSUED TO SOMEONE',fg = 'red',bg ='#fffbe6',font=('TkMenuFont',15,'bold')).pack(pady=(10,150))
        Button(deletebookButton,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=deletebookFrame).pack()
        Button(deletebookButton,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)        
    else:
        conn.commit()
        Label(deletebookButton,text = 'DONE, SUCCESSFULLY DELETED',fg ='#537FE7',bg = '#fffbe6',font =('TkMenuFont',20,'bold')).pack(pady = (180))
        Button(deletebookButton,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=deletebookFrame).pack()
        Button(deletebookButton,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)
        



#code for delete book function
def deletebookFrame():
    deletebookFrame =Frame(root,bg = '#fffbe6',width = 500,height = 600)
    deletebookFrame.grid(row =0 ,column = 0)
    deletebookFrame.pack_propagate(False)
    deletebookFrame.tkraise()

    Label(deletebookFrame,text = 'DELETE BOOK FROM LIBRARY',fg ='#80669d',bg = '#fffbe6',font = ('TkMenuFont',20,'bold')).pack(pady = 55)
    Label(deletebookFrame,text = 'ENTER BOOK ID', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (60,3))
    global delbookId
    delbookId=Entry(deletebookFrame,font=('Arial',12,'bold'),justify = 'center')
    delbookId.focus()
    delbookId.pack(pady = (3,15))

    #buttons on deletebookframe function

    Button(deletebookFrame,text ='DELETE BOOK',bg = 'red',fg='#FBDF07',font =('TkHeadingFont',12,'bold'),
               activebackground='red',activeforeground='#0A2647',width = 12,cursor= 'hand2',command=deletebookButton).pack(pady =(35,10))
    Button(deletebookFrame,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=loadFrame1).pack()
    
    


#code for ADD button in loadAddbook function
def addButtonfunction():
    addButtonframe = Frame(root,bg = '#fffbe6',width = 500, height = 600)
    addButtonframe.grid(row = 0,column = 0)
    addButtonframe.pack_propagate(False)
    addButtonframe.tkraise()
    try:
        cursor.execute("insert into book values ("+bookId.get()+",'"+bookName.get()+"','"+bookAuthor.get()+"',"+bookQuantity.get()+")")
    except sqlite3.IntegrityError :
        cursor.execute('select * from book where id ='+bookId.get())
        Label(addButtonframe,text = 'BOOK OF THIS ID IS ALREADY PRESENT', fg ='red', bg = '#fffbe6',font=('TkMenuFont',12,'bold')).pack(pady =(180,40))
        Label(addButtonframe, text = cursor.fetchall(), fg = 'black',bg = '#fffbe6',font = ('Arial',10,'bold')).pack(pady=(30,140))
        Button(addButtonframe,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
               activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=loadAddbook).pack()
        Button(addButtonframe,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady = 10)
          

    except sqlite3.OperationalError:
        
        Label(addButtonframe, text = 'OOPS! IT SEEMS LIKE YOU ENTERED INVALID VALUE',fg='red',bg = '#fffbe6',font =('TkMenuFont',12,'bold')).pack(pady =200)
        
        Button(addButtonframe,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=loadAddbook).pack()
        Button(addButtonframe,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)


    else :
        conn.commit()
        cursor.execute('select * from book where id ='+bookId.get())
        Label(addButtonframe,text = 'DONE, SUCCESSFULLY ADDED',fg ='#537FE7',bg = '#fffbe6',font =('TkMenuFont',20,'bold')).pack(pady = (180,20))
        Label(addButtonframe,text=cursor.fetchall(),fg = 'black',bg='#fffbe6', font = ('Arial',10,'bold')).pack(pady=(30,140))
        Button(addButtonframe,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=loadAddbook).pack()
        Button(addButtonframe,text ='HOME PAGE',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 12,cursor= 'hand2',command=loadFrame1).pack(pady=10)




#code for add book function 
def loadAddbook():
    frame2 = Frame(root,bg = '#fffbe6',width =500,height =600)
    frame2.grid(row = 0,column = 0)
    frame2.pack_propagate(False)
    frame2.tkraise()

    Label(frame2,text = 'ADD BOOK',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',25,'bold')).pack(pady=35)

    Label(frame2,text = 'ENTER BOOK ID', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    global bookId,bookName,bookAuthor,bookQuantity
    bookId=Entry(frame2,font=('Arial',12,'bold'),justify = 'center')
    bookId.focus()
    bookId.pack(pady = (3,15))

    Label(frame2,text = 'ENTER BOOK NAME', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    bookName = Entry(frame2,font=('Arial',12,'bold'),justify = 'right')
    bookName.pack(pady =(3,15))

    Label(frame2,text = 'ENTER AUTHOR NAME', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    bookAuthor = Entry(frame2,font=('Arial',12,'bold'),justify = 'right')
    bookAuthor.pack(pady=(3,15))

    Label(frame2,text = 'ENTER NUMBER OF COPIES', fg = 'black',bg='#fffbe6',font =('Arial',16,'bold')).pack(pady = (10,3))
    bookQuantity = Entry(frame2,font =('Arial',12,'bold'),justify= 'center')
    bookQuantity.pack(pady=(3,15))

    #buttons of loadAddbook function
    addButton = Button(frame2,text ='ADD',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor= 'hand2',command=addButtonfunction)
    addButton.pack()

    Button(frame2,text ='BACK',bg = '#E5BEEC',fg='#2A2F4F',font =('TkHeadingFont',12,'bold'),
                        activebackground='#2A2F4F',activeforeground='#E5BEEC',width = 6,cursor='hand2',command= loadFrame1).pack(pady = 10)


#code for main home page
def loadFrame1():
    frame1 = Frame(root, width = 500,height = 600,bg = '#fffbe6')
    frame1.grid(row = 0 ,column = 0)
    frame1.pack_propagate(False)
    frame1.tkraise()


    Label(frame1,text = 'LIBRARY DASHBOARD',fg = '#80669d',bg='#fffbe6',font=('TkMenuFont',25,'bold')).pack(pady = 35)


    #buttons of loadFrame1 function
    button1 = Button(frame1,text = 'ADD BOOK',bg = '#7A3E65',fg='#F6E1C3',font =('TkHeadingFont',15,'bold'),activebackground='#F6E1C3',
                 activeforeground='#7A3E65',cursor = 'hand2',command=loadAddbook)
    button1.pack(pady = 15)

    button2 = Button(frame1,text = 'ISSUE BOOK',bg = '#7A3E65',fg='#F6E1C3',font =('TkHeadingFont',15,'bold'),activebackground='#F6E1C3',
                 activeforeground='#7A3E65',cursor = 'hand2',command=issueBookFrame)
    button2.pack(pady = 15)

    button3 = Button(frame1,text = 'RETURN BOOK',bg = '#7A3E65',fg='#F6E1C3',font =('TkHeadingFont',15,'bold'),activebackground='#F6E1C3',
                 activeforeground='#7A3E65',cursor = 'hand2',command =Return)
    button3.pack(pady = 20)

    button4 = Button(frame1,text = 'DELETE BOOK',bg = '#7A3E65',fg='#F6E1C3',font =('TkHeadingFont',15,'bold'),activebackground='#F6E1C3',
                 activeforeground='#7A3E65',cursor = 'hand2',command=deletebookFrame)
    button4.pack(pady = 15)

    button5 = Button(frame1,text = 'STUDENT DETAILS',bg = '#7A3E65',fg='#F6E1C3',font =('TkHeadingFont',15,'bold'),activebackground='#F6E1C3',
                 activeforeground='#7A3E65',cursor = 'hand2',command=viewstudentDetails)
    button5.pack(pady = 15)

    button6 = Button(frame1,text = 'VIEW BOOK DETAILS',bg = '#7A3E65',fg='#F6E1C3',font =('TkHeadingFont',15,'bold'),activebackground='#F6E1C3',
                 activeforeground='#7A3E65',cursor = 'hand2',command = viewbookDetails)
    button6.pack(pady = 15)
    
    Label(frame1,text = 'CONTACT: 7814650715',bg='#fffbe6',font=('TkMenuFont',8,'bold')).pack(side='bottom')
    Label(frame1,text = 'MADE BY: VK KANKERWAL',bg='#fffbe6',font=('TkMenuFont',8,'bold')).pack(side='bottom')
    

loadFrame1()


root.mainloop()
