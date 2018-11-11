from tkinter import * 

root = Tk()


one = Label(root, text="One", bg="red", fg="white") # Creating a Label named "one" and setting the background to red and font to white.
one.pack() # Calling the pack, with no parameters.

two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) # X stretches the label across the pageso it'll fit the parent

three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) # "Y" drags the label down indefinitely. 

root.mainloop()
