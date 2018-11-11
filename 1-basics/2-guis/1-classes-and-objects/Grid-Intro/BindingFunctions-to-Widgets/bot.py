from tkinter import *

# | BINDING FUNCTIONS TO WIDGETS |

root = Tk()
def print_name(): # Declaring a function called print_name
    print("Hello my name is Will") # Printing some text related to that function

button_1 = Button(root, text="Print my name", command=print_name) # Use COMMAND to bind the function to a widget
button_1.pack() # Call the button function

root.mainloop()
