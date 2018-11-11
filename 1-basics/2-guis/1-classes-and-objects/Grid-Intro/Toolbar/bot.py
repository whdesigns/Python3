from tkinter import *

# | CREATING DROP DOWN MENUS |

def doNothing():
    print("ok ok I won't...")

root = Tk()

menu = Menu(root)
root.config(menu=menu) #States that we're setting up a menu and its equal the variable declared above.

subMenu = Menu(root)
menu.add_cascade(label="File", menu=subMenu) # This is the name of the file e.g. "File" and "submenu" is where it will be placed.
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing) # Adding another item to the menu.
subMenu.add_separator() # This will create a lines to separate one group of items from another e.g. much like \n.
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu) # Creating another item in the main menu
menu.add_cascade(label="Edit", menu=editMenu) # Naming the drop down menu
editMenu.add_command(label="Redo", command=doNothing) # Naming the item inside the menu



# | CREATING A TOOLBAR |

toolbar = Frame(root, bg="blue") # Step One: Create a frame that stretches under the main menu and will hold several tools

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2) # Providing extra space for the button

toolbar.pack(side=TOP, fill=X)

root.mainloop()
