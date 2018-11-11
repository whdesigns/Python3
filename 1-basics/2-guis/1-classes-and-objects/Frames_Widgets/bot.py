from tkinter import * 

root = Tk()



# | HOW TO MAKE FRAMES |

topFrame = Frame(root) # A frame is an invisable layout (like rectangles in illustrator), where you can place selected widgets
topFrame.pack() # topFrame goes on the top, but does not need to be called, because by default it will be at the top anyway, due to hierarchy postioning.
bottomFrame = Frame(root) #  Creating another frame, whih will sit below the top frame.
bottomFrame.pack(side=BOTTOM) # This frame must be called to ensure it is on the bottom e.g. side=BOTTOM.



# | HOW TO MAKE WIDGETS |

# creating buttons and then assigning where they will go e.g. the topFrame.
# Assigning text to the button and then providing a colour for it.

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")



# | DISPLAYING THE WIDGETS |
