from tkinter import * 

# GRID GIVES MORE ROW & COLUMN CONTROL THAN PACK DOES

# Does NOT accept left, right, center. Instead uses N,E,S,W:
# North=top
# East=right
# South=bottom
# West=left

root = Tk()

label_1 = Label(root, text="Email:")
label_2 = Label(root, text="Password:")

# "entry" provides a blank field where the user can type something in.
entry_1 = Entry(root)
entry_2 = Entry(root)

# Indicating whereabouts the grid will be placed. Columns can be called here as well, but it is always set at zero, so unnecessary.

label_1.grid(row=0, sticky=E) # This is going to be on top and "sticky=E" aligns it to the right.
label_2.grid(row=1, sticky=E) # This is going to be on bottom and "sticky=E" aligns it to the right.
# Now both Email & Password will be aligned to the right.

entry_1.grid(row=0, column=1)  # "column=1 is the SECOND column, since computers start counting at 0.
entry_2.grid(row=1, column=1)  # "column=1 is the SECOND column, since computers start counting at 0.

c = Checkbutton(root, text="Keep me logged in") # Declaring a checkbutton for the user to tick
c.grid(columnspan=2) # This will take up 2 columns/cells and merge them together.


root.mainloop()
