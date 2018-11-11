from tkinter import *

root = Tk()

photo = PhotoImage(file="tomsface.png") # File must be in the same directory as the python file
label = Label(root, image=photo) # image must be set inside a label so it can be placed anywhere.
label.pack() # positions it wherever it decides to go.

root.mainloop()
