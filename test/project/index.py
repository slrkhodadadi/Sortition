from tkinter import *
from PIL import ImageTk, Image
from random import randint
# images.jpeg
master = Tk()
master.title("Sortition")
master.geometry("300x400")
master.resizable(width=False,height=False)
# master.iconbitmap('@/home/admin-s/myFile/code/python/test/project/Secret-Files-2-3-icon.png')


def show():
   
    if r.get() == "":
        r.set("no")
    proc=True
    list1=[]
    
    if participants.get() >= win.get():
        
        try:
            while proc:
                rand=randint(1,participants.get())
                if r.get()=="no":
                    if rand not in list1:
                        list1.append(rand)
                else:
                    list1.append(rand)
                if len(list1)==win.get():
                    print(len(list1))
                    proc=False        
            # lbl1=Label(master,text=list1,fg="green").pack()
            for list in list1:
                  listbox1.insert(0,list)
            listbox1.insert(0,"-------------------------------------------------")
          
        except:
            lbl2=Label(master,text="please enter valid number..." ,fg="red")
            lbl2.pack()
    else:
            lbl3=Label(master,text="please enter valid numbeer..." ,fg="red")
            lbl3.pack()
        
        
lbl1 = Label(master, text="Please enter the number of your participants :")
lbl1.pack()

participants= IntVar()
e1=Entry(master,textvariable=participants)
e1.pack()

lbl2 = Label(master, text="Please enter the number of your winners :")
lbl2.pack()

win=IntVar()
e2=Entry(master,textvariable=win)
e2.pack()

          
r = StringVar()
c= Checkbutton(master,text="multiple times win",variable=r,offvalue="no",onvalue="yes")
c.pack()

btn1=Button(master,text="click",command=show)
btn1.pack()

sb = Scrollbar(master)

listbox1=Listbox(master,width=35,height=6)
listbox1.pack()

listbox1.configure(yscrollcommand=sb.set)
sb.configure(command=listbox1.yview)
btn2=Button(master,text="delete",command=lambda:listbox1.delete(0,END))
btn2.pack()


btn3=Button(master,text="exit",command=lambda:listbox1.quit())
btn3.pack()

# lbl1.grid(row=0, column=0)
# lbl2.grid(row=1, column=0)
master.mainloop()
