import webbrowser,random,openpyxl,os,pytz
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='2004',database='d')
mycursor=mydb.cursor()
database={}
wb=openpyxl.load_workbook('Book1.xlsx')
wb2=openpyxl.load_workbook('new_Book1.xlsx')
wb3=openpyxl.load_workbook('Learner.xlsx')
x=2
facts=['President Kennedy was the fastest random speaker in the world with upwards of 350 words per minute.',
       'In the average lifetime, a person will walk the equivalent of 5 times around the equator.','Odontophobia is the fear of teeth.',
       'Cats sleep 16 to 18 hours per day.','The most common name in the world is Mohammed.','According to suicide statistics, Monday is the most favored day for self-destruction.',
       'The most money ever paid for a cow in an auction was $1.3 million.','Every year about 98% of the atoms in your body are replaced.',
       'Elephants are the only mammals that cannot jump.','Women are 37% more likely to go to a psychiatrist than men are.','The average person makes about 1,140 telephone calls each year.']    
notify={}
points=0
logintime=0
sheet=wb.active
sheet2=wb2.active
sheet3=wb3.active
for i in range(2,sheet2.max_row+1):
    database.update({sheet2.cell(row=i,column=1).value:sheet2.cell(row=i,column=2).value})
print('''WELCOME TO LEARNER!! THE NO. 1 LEARNING PLATFORM''')
a=int(input('Enter 0 to create an account or any other number to login :'))
if a==0:
#Account creation    
    newid=input('Create your LEARNERTAG :')
    while(True):
        if newid not in database:
            while x>1:
                if sheet2['A'+(str(x))].value==None:
                    sheet2['A'+(str(x))]=newid
                    wb2.save('new_Book1.xlsx')
                    break
                else:
                    x+=1
            break
        else:
            newid=input('''Oops! LEARNERTAG already in use :(
please enter another one !''')
    while(True):
        x=2
        while(True):
            profession=input('Enter s if you are a student or t if you are a teacher-')
            if profession=='s' or profession=='t':
                while x>1:
                    if sheet2['C'+(str(x))].value==None:
                        sheet2['C'+(str(x))]=profession
                        wb2.save('new_Book1.xlsx')
                        break
                    else:
                        x+=1
                break
            else:
                print('Please enter s or t only')
        newpswd=input('Create your password : ')
        x=2
        if len(newpswd)>=8:
            while x>1:
                if sheet2['B'+(str(x))].value==None:
                    sheet2['B'+(str(x))]=newpswd
                    wb2.save('new_Book1.xlsx')
                    for i in range(5,11):
                        sheet2.cell(row=x,column=i).value=0
                        wb2.save('new_Book1.xlsx')
                    break
                else:
                    x+=1
            print('You have successfully created your account!Now you can safely login.')
            break
        else:
            print('Please enter a password containing a minimum of 8 characters')
for i in range(2,sheet2.max_row+1):
    database.update({sheet2.cell(row=i,column=1).value:sheet2.cell(row=i,column=2).value})

#Login
while(True):
    userid=input('Enter your LEARNERTAG :')
    pswd=input('Enter your password :')
    for i in range(2,sheet2.max_row+1):
        if sheet2.cell(row=i,column=1).value==userid:
            number=i
    if (userid in database) and (database[userid]==pswd):
        sheet2.cell(row=number,column=8).value+=1
        wb2.save('new_Book1.xlsx')
        logintime=datetime.now(pytz.timezone('Asia/Kolkata'))
        break
    else:
        print('Wrong credentials entered.Please enter correct credentials!')    
##After logging in the user can choose what he wants to do
##0-Search
##1-is to enroll for a new course       
##2-is to view points and progress  
##3-is to view other users
##4-To view your to-do list
##5-To schedule a task or time yourself
##6-To access notes
##7-To take a test/quiz
##8-Website
##9-Settings and Log out
print('Good to see you back, ',userid)
print('Did you know:',random.choice(facts))
print('Kindly switch to the tkinter tab. Once you have interacted with those buttons kindly switch back here.')
number=0
quit=''
for i in range(2,sheet2.max_row+1):
    if sheet2.cell(row=i,column=1).value==userid:
        number=i
def notestable():
    mycursor.execute('create table if not exists notes(name varchar(255),link varchar(255))')
    notesfetch=mycursor.fetchall()
    for i in notesfetch:
        print(i)
    mydb.commit()
def testtable():
    mycursor.execute('create table if not exists test(name varchar(255),link varchar(255))')
    testfetch=mycursor.fetchall()
    for i in testfetch:
        print(i)
    mydb.commit()
notestable()
testtable()
while True:
    def op0():
        #opens search engine
        webbrowser.open('https://google.com')
    def op1():
        #courses
        for i in range(2,sheet3.max_row+1):
            print(i-1,'-',sheet3.cell(row=i,column=1).value)
        course=int(input('Enter choice:'))
        if sheet3.cell(row=course+1,column=2).value!=None:
            webbrowser.open(sheet3.cell(row=course+1,column=2).value)
        else:
            print('No courses available with that choice')
        pe=sheet3.cell(row=course+1,column=3).value
        sheet2.cell(row=number,column=7).value+=int(pe)
        wb2.save('new_Book1.xlsx')
        print('You have earned',sheet3.cell(row=course+1,column=3).value,'points for completing this course')
        if sheet2.cell(row=number,column=3).value=='t':
            choose=int(input('Since you are a teacher,enter 0 to create a new course-'))
            y=2
            if choose==0:
                while y>1:
                    if sheet3['A'+(str(y))].value==None:
                        coursename=input('Enter the name of the course-')
                        link=input('Enter the course link-')
                        coursepoints=input('Enter the points for the course-')
                        sheet3['A'+(str(y))]=coursename
                        wb3.save('Learner.xlsx')
                        sheet3['B'+(str(y))]=link
                        wb3.save('Learner.xlsx')
                        sheet3['C'+(str(y))]=coursepoints
                        wb3.save('Learner.xlsx')
                        print('Course has been created')
                        break
                    else:
                        y+=1
    def op2():
        #viewing points
        print('This is your login chart compared to other users where you are the leftmost user')
        print('Your progress report:')
        print('Tests taken-',sheet2.cell(row=number,column=5).value)
        print('Notes viewed-',sheet2.cell(row=number,column=6).value)
        print('Points-',sheet2.cell(row=number,column=7).value)
        print('Logins-',sheet2.cell(row=number,column=8).value)
        print('Learning time-',sheet2.cell(row=number,column=10).value,'hours and',sheet2.cell(row=number,column=9).value,'minutes')
        t,u=[],[]
        for i in range(2,sheet2.max_row):
            t+=[sheet2.cell(row=i,column=8).value]
            u+=[i-1]
        plt.title('Login chart')
        plt.xlabel('User number')
        plt.ylabel('Number of logins')
        plt.bar(t,u)
        plt.show()
        plt.title('Points chart')
        plt.xlabel('Number of logins')
        plt.ylabel('Points')
        a=[1,2]
        b=[sheet2.cell(row=number,column=7).value,sheet2.cell(row=number,column=7).value]
        plt.plot(a,b)
        plt.show()
    def op3():
        #Displays users and notifications
        print('Learners are: ',)
        for i in range(2,sheet2.max_row+1):
            print(sheet2.cell(row=i,column=1).value,'\t Profession:',sheet2.cell(row=i,column=3).value,'\t Last online:',sheet2.cell(row=i,column=11).value)
        print('Notifications/Reminders:')
        if sheet2.cell(row=number,column=12).value==None:
            print('No notifications.')
        else:
            print(sheet2.cell(row=number,column=12).value)
        print('New user connect feature will be added to send messages to other users securely.Kindly wait for the new update.')
    def op4():
        #To-do list and calendar
        todo=input('Enter 0 to view your to do list,1 to make a new one or 2 to see events in your calendar')
        if todo=='0':
            if sheet2.cell(row=number,column=13).value==None:
                print('No to do list has been made.Please make a new one.')
            else:
                print(sheet2.cell(row=number,column=13).value)
        elif todo=='1':
            list=input('Enter your to-do list in priority from 1...')
            sheet2.cell(row=number,column=13).value=list
            wb2.save('new_Book1.xlsx')
        elif todo=='2':
            webbrowser.open('calendar.google.com')
    def op5():
        #Reminders,task scheduling and timer
        print('Success comes with persistence')
        print('Use the tutorial to create a task in task scheduler')
        webbrowser.open('https://www.youtube.com/watch?v=s_EMsHlDPnE')
        os.startfile('C:\\WINDOWS\\system32\\taskschd.msc')
        time=input('Enter reminder for course-')
        sheet2.cell(row=number,column=12).value=time
        wb2.save('new_Book1.xlsx')
        print('A reminder has been set for the same.')
        timer=input('Enter 1 if you want to time your session:')
        if timer=='1':
            webbrowser.open('https://www.online-timer.net/')
    def op6():
        #Accessing pdf notes
        notes=int(input('''Enter
        0-Photoshop notes
        1-Python notes
        2-Java notes
        3-View database
        4-Add notes to database
        5-Update database'''))
        if notes==0:
            webbrowser.open('http://164.125.174.23:8080/lee/Adobe%20Photoshop%20CS6%20Tutorial.pdf')
            sheet2.cell(row=number,column=6).value+=1
        elif notes==1:
            webbrowser.open('https://bugs.python.org/file47781/Tutorial_EDIT.pdf')
            sheet2.cell(row=number,column=6).value+=1
        elif notes==2:
            webbrowser.open('https://www.tutorialspoint.com/java/java_tutorial.pdf')
            sheet2.cell(row=number,column=6).value+=1
        elif notes==3:
            mycursor.execute('select * from notes')
            n1=mycursor.fetchall()
            if len(n1)==0:
                print('The database is empty')
            for i in n1:
                print(i)
            mydb.commit()
        elif notes==4:
            nname=input('Enter name-')
            nlink=input('Link to the notes-')
            mycursor.execute('insert into notes values(%s,%s)',(nname,nlink))
            n2=mycursor.fetchall()
            for i in n2:
                print(i)
            mydb.commit()
            print('It has been added to the database.')
        elif notes==5:
            nuname=input('Enter name of the notes which you want to update(it must exist in the database)-')
            nulink=input('Enter new link-')
            mycursor.execute('update notes set link= %s where name= %s',(nulink,nuname))
            n3=mycursor.fetchall()
            for i in n3:
                print(i)
            mydb.commit()
            print('The changes have been made.')
        else:
            print('Please enter a valid choice')
    def op7():
        #Taking an online test
        print('Please close all other applications except test window')
        os.startfile('C:\\WINDOWS\\system32\\Taskmgr.exe')
        test=input('''Enter
        0-Personality test
        1-Python test
        2-Java test
        3-View database
        4-Add tests to database
        5-Update database''')
        if test=='0':
            webbrowser.open('quiz.gretchenrubin.com')
            sheet2.cell(row=number,column=5).value+=1
        elif test=='1':
            webbrowser.open('https://www.w3schools.com/python/python_quiz.asp')
            sheet2.cell(row=number,column=5).value+=1
        elif test=='2':
            webbrowser.open('https://www.w3schools.com/java/java_quiz.asp')
            sheet2.cell(row=number,column=5).value+=1
        elif test=='3':
            mycursor.execute('select * from test')
            t1=mycursor.fetchall()
            if len(t1)==0:
                print('The database is empty')
            for i in t1:
                print(i)
            mydb.commit()
        elif test=='4':
            tname=input('Enter name-')
            tlink=input('Link to the test-')
            mycursor.execute('insert into test values(%s,%s)',(tname,tlink))
            t2=mycursor.fetchall()
            for i in t2:
                print(i)
            mydb.commit()
            print('It has been added to the database.')
        elif test=='5':
            tuname=input('Enter name of the test which you want to update(it must exist in the database)-')
            tulink=input('Enter new link-')
            mycursor.execute('update test set link= %s where name= %s',(tulink,tuname))
            t3=mycursor.fetchall()
            for i in t3:
                print(i)
            mydb.commit()
            print('The changes have been made.')
        else:
            print('Please enter a valid choice')
    def op8():
        #Link to website
        print('Visit the website to get rewards for the points you have earned or to see the T&C')
        webbrowser.open('https://learner1.yolasite.com/')       
    def op9():
        #Feedback and account settings
        feedback=input('Any queries or suggestions-contact learnerofficial@gmail.com \n''Please rate learner on a scale of 1 to 5:')
        sheet2['D'+(str(number))]=feedback
        wb2.save('new_Book1.xlsx')
        account=input('Enter 0 to delete account or any other number to exit:')
        if account=='0':
            print("Your account has been deleted.We're sorry to see you go.")
            for i in range(1,14):
                sheet2.cell(row=number,column=i).value=None
                wb2.save('new_Book1.xlsx')
            quit=input('Enter 0 to quit-')
        else:
            settings=input('Enter 0 to view settings and log out:')
            if settings=='0':
                print('Profile and user data is secure.More settings will be added in the next update.')
            last_online=datetime.now(pytz.timezone('Asia/Kolkata'))
            sheet2.cell(row=number,column=11).value=last_online
            wb2.save('new_Book1.xlsx')
            sheet2.cell(row=number,column=10).value+=(last_online.hour-logintime.hour)
            wb2.save('new_Book1.xlsx')
            sheet2.cell(row=number,column=9).value+=(last_online.minute-logintime.minute)
            wb2.save('new_Book1.xlsx')
            print('Successfully logged out.Bye! Keep learning.')
            top.destroy()
    if quit=='0':
        break
    top=tk.Tk()
    learner=tk.PhotoImage(file=r"C:\Users\Aaryan\Pictures\Screenshots\Screenshot (208).png")
    l1=tk.Label(top,image=learner)
    l2=tk.Label(top,text='Kindly switch back to the IDLE window after clicking on a button')
    option0=tk.Button(top,text='Search',fg='black',command=op0)
    option1=tk.Button(top,text='Enroll for a new course',fg='black',command=op1)
    option2=tk.Button(top,text='View points and progress',fg='black',command=op2)
    option3=tk.Button(top,text='View other users',fg='black',command=op3)
    option4=tk.Button(top,text='View to-do list',fg='black',command=op4)
    option5=tk.Button(top,text='Schedule a task or time yourself',fg='black',command=op5)
    option6=tk.Button(top,text='Access notes',fg='black',command=op6)
    option7=tk.Button(top,text='Take test/quiz',fg='black',command=op7)
    option8=tk.Button(top,text='View website',fg='black',command=op8)
    option9=tk.Button(top,text='Settings and Log out',fg='black',command=op9)
    l1.pack()
    option0.pack()
    option1.pack()
    option2.pack()
    option3.pack()
    option4.pack()
    option5.pack()
    option6.pack()
    option7.pack()
    option8.pack()
    option9.pack()
    l2.pack()
    quit=input('Enter 0 to quit-')
    if quit=='0':
        top.destroy()
        break
    top.mainloop()   
