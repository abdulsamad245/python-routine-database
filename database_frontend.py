from tkinter import *
import tkinter
import database_backend

win=Tk()

win.wm_title('MY DAILY ROUTINE DATABASE')

def get_selected_row(event):
    global selected_row
    index=list.curselection()[0]
    selected_row=list.get(index)
    print(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[6])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[2])


def delete_command():
    database_backend.delete(selected_row[0])
    #list.delete(list.curselection()[0],list.curselection()[0])
    list.delete(ANCHOR)
    print(selected_row[0])

    
    


def view_command():
    list.delete(0,END)
    for rows in database_backend.view():
        list.insert(END,rows)


def search_command():
    list.delete(0,END)
    for rows in database_backend.search(date_text.get(),earnings_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()):
        list.insert(END,rows)


def add_command():
        database_backend.insert(date_text.get(),earnings_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())
        list.delete(0,END)
        list.insert(END,(date_text.get(),earnings_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()))









l1=Label(win,text='Date')
l1.grid(row=0,column=0)

l2=Label(win,text='Earnings')
l2.grid(row=0,column=2)

l1=Label(win,text='Exercise')
l1.grid(row=1,column=0)

l3=Label(win,text='Study')
l3.grid(row=1,column=2)

l4=Label(win,text='Diet')
l4.grid(row=2,column=0)

l5=Label(win,text='Python')
l5.grid(row=2,column=2)

date_text=StringVar()
e1=Entry(win,textvariable=date_text)
e1.grid(row=0,column=1)

earnings_text=StringVar()
e3=Entry(win,textvariable=earnings_text)
e3.grid(row=0,column=3)

exercise_text=StringVar()
e4=Entry(win,textvariable=exercise_text)
e4.grid(row=1,column=1)

study_text=StringVar()
e5=Entry(win,textvariable=study_text)
e5.grid(row=1,column=3)

diet_text=StringVar()
e6=Entry(win,textvariable=diet_text)
e6.grid(row=2,column=1)

python_text=StringVar()
e2=Entry(win,textvariable=python_text)
e2.grid(row=2,column=3)

list=Listbox(win,height=8,width=45)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

sb= tkinter.Scrollbar(win,command=list.yview)
sb.grid(row=3,column=2,columnspan=1,rowspan=9)


b1=Button(win,text='ADD',width=12,pady=5,command=add_command)
b1.grid(row=3,column=3)



b2=Button(win,text='Search',width=12,pady=5,command=search_command)
b2.grid(row=4,column=3)


b3=Button(win,text='Delete ',width=12,pady=5,command=delete_command)
b3.grid(row=5,column=3)


b4=Button(win,text='View All',width=12,pady=5,command=view_command)
b4.grid(row=6,column=3)


b5=Button(win,text='Close',width=12,pady=5,command=win.destroy)
b5.grid(row=7,column=3)


list.bind('<<ListboxSelect>>',get_selected_row)




win.mainloop()