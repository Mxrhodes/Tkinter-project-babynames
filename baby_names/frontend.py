from Tkinter import *
import backend

window=Tk()

window.wm_title("Baby Names")

""" 
Making this 12 * 10
 """


#================ Callback Functions =======================
def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(),gender_text.get(),submit_text.get()):
        list1.insert(END,row[1])

def boy_command():
    list1.delete(0,END)
    for row in backend.search(gender="Boy"):
        list1.insert(END,row)

def girl_command():
    list1.delete(0,END)
    for row in backend.search(gender="Girl"):
        list1.insert(END,row)

def add_command():
    list1.delete(0,END)
    backend.insert(name_text.get(),gender_text.get(),submit_text.get())

def generate_command():
    list1.delete(0,END)
    backend.insertGeneratedName()
    
#================ Labels =======================
l1=Label(window,text="Name:")
l1.grid(row=3,column=1)
l2=Label(window,text="Gender:")
l2.grid(row=3,column=3)
l3=Label(window,text="Submitted By:")
l3.grid(row=3,column=5)


#================ Entry =======================
searchby_text=StringVar()
e1=Entry(window,textvariable=searchby_text)
e1.grid(row=0,column=1,rowspan=1,columnspan=6)

name_text=StringVar()
e2=Entry(window,textvariable=name_text)
e2.grid(row=3,column=2)

gender_text=StringVar()
e3=Entry(window,textvariable=gender_text)
e3.grid(row=3,column=4)

submit_text=StringVar()
e4=Entry(window,textvariable=submit_text)
e4.grid(row=3,column=6)



#================ Display box =======================
list1=Listbox(window,height=6,width=35)
list1.grid(row=6,column=0,rowspan=8,columnspan=4)

sb1=Scrollbar(window)
sb1.grid(row=6,column=3,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#list1.bind('<<ListboxSelect>>',(get_selected_row))



#================ Buttons =======================
b1=Button(window,text="Search",width=12,command=search_command)
b1.grid(row=0,column=5)
b2=Button(window,text="Boy Names",width=12,command=boy_command)
b2.grid(row=5,column=1)
b3=Button(window,text="Girl Names",width=12,command=girl_command)
b3.grid(row=5,column=3)
b4=Button(window,text="Add",width=12)
b4.grid(row=3,column=7)


window.mainloop()