from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load images
        self.cactus_image = PhotoImage(file="cactus.gif")
        self.cactus2_image = PhotoImage(file="cactus2.gif")

  # set window properties
        self.title("CACTUS")

        # add components
        self.add_heading_label()
        self.add_cactus_image_label()
        self.add_flip_button()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.pack(fill=X)
        self.heading_label.configure(font="Arial 18",
                                     text="Cactus Leaves")

    def add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.pack(fill=X)
        self.cactus_image_label.configure(image=self.cactus_image)

    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.pack()
        self.flip_button.configure(text="Flip")
        self.flip_button.bind("<ButtonRelease-1>", self.left_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.right_clicked)

    def left_clicked(self, event):
        self.cactus_image_label.configure(image=self.cactus_image)

    def right_clicked(self, event):
        self.cactus_image_label.configure(image=self.cactus2_image)
    
    
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
