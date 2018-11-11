from tkinter import *
import tkinter.messagebox # Brings messagebox to the screen e.g. alerts

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years")

answer = tkinter.messagebox.askquestion("Question 1", "Do you like emojis?")

if answer == "yes":
    print(":) :( :p")
root.mainloop()
