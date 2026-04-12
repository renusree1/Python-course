from tkinter import *
from datetime import date 

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

label= Label(text= "Hey there!", fg= "white", bg= "blue", height= 1, width= 300)
name_label= Label(text= "Full Name:", fg= "white")
name_entry= Entry()

def display():
    name= name_entry.get()
    global message
    message= "Welcome to the Application\n Today's date is "
    greet= "Hello" +name+ "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box= Text(height=3)

button= Button(text= "Begin", command= display, height= 1, bg= "white", fg= "black")

label.pack()
name_label.pack()
name_entry.pack()
button.pack()
text_box.pack()

root.mainloop()

