from tkinter import * 

# GRID GIVES MORE ROW & COLUMN CONTROL THAN PACK DOES

root = Tk()

label_1 = Label(root, text="Email:")
label_2 = Label(root, text="Password:")

# "entry" provides a blank field where the user can type something in.
entry_1 = Entry(root)
entry_2 = Entry(root)

# Indicating whereabouts the grid will be placed. Column can be called here as well, but it is always set at zero.
label_1.grid(row=0) # This is going to be on top
label_2.grid(row=1) # This is going to be on bottom

entry_1.grid(row=0, column=1)  # "column=1 is the SECOND column, since computers start counting at 0.
entry_2.grid(row=1, column=1)

root.mainloop()
