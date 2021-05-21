from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("270x80")
root.maxsize(270,80)
root.minsize(270,80)
root.title("My Clock")
root.config(background="black")
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    a.config(text = current_time)
    jk = now.strftime("%p")
    b.config(text = jk)
    a.after(1000,time)

a = Label(root,font=('Arial',40,'bold'),fg="#fc6203",bg="black")
b = Label(root,font=('Arial',20,'bold'),fg="#fc6203",bg="black")
time()
a.place(x=0,y=0)
b.place(x=215,y=24)
root.mainloop()