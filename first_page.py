# Abdullah isaacs class 2
# import modules section
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta, date
from PIL import ImageTk,Image
import re

#create window

root = tk.Tk()
root.title("Weather")
root.geometry("800x400")
root.configure(bg="black")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# image for background
pic = Canvas(root, width=800, height=400, bg="black")
pic.place(x=0,y=0)
img = ImageTk.PhotoImage(Image.open('pngegg.png'))
pic.create_image(0, 20, anchor=NW, image=img)
first_name = Label(root,text="First Name", bg="black",fg="gold", font="Times 20 bold italic")
first_name.place(x=50,y=20)
first_entry = Entry(root, textvariable="fname", bg="red", width=15)
first_entry.place(x=230, y=20)
email= Label(root,text="Email address", bg="black",fg="gold", font="Times 20 bold italic")
email.place(x=50,y=80)
email_ent=Entry(root,textvariable="age",bg="red",width=37)
email_ent.place(x=50,y=120)
id_no= Label(root,text="ID number", bg="black",fg="gold", font="Times 20 bold italic")
id_no.place(x=50,y=160)
id_ent=Entry(root,textvariable="id",bg="red",width=13)
id_ent.place(x=230,y=170)

def qualify():
    year = int(id_ent.get()[0:2])
    month = int(id_ent.get()[2:4])
    day = int(id_ent.get()[4:6])
    dob = date(int(year), int(month), int(day))
    age= str((date.today() - dob) // timedelta(days=365.2425))[2:4]
    def calc():
        if int(age) < 18:
            messagebox.showerror("Error","You must be over 18 to play")
        elif len(id_ent.get()) < 13:
            messagebox.showerror("Error","please enter a valid ID number")
        elif len(id_ent.get()) > 13:
            messagebox.showerror("Error","Please enter a valid ID  number")
        else:
            return 1
    def email_checker():
        if (re.search(regex, email_ent.get())):
            return 1
        else:
            messagebox.showerror("Error","Invalid Email")
    if calc() == 1 and email_checker() == 1:
        messagebox.showinfo("CONGRATULATIONS","LETS PLAY!!!")



qual = Button(root, text="Check if i qualify", command=qualify, bg="gold",pady=5,padx=5, width=15,height=5)
qual.place(x=450,y=100)

# def clear():
# first_entry.delete(0, END)
# email_ent.delete(0, END)
# id_ent.delete((0, END)


root.mainloop()