from tkinter import *

class WillsButtons:
    def __init__(self, master):  # Anytime you see "master" this means the root or main window
        frame = Frame(master) # declaring frame is equal to the main window or parent
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("WOW, This actually worked!")

root = Tk()
w = WillsButtons(root) # Calls the master 
root.mainloop()
