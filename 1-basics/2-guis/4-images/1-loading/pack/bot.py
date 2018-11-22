from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="ambulance.gif")
        self.bike_image = PhotoImage(file="bike.gif")
        self.plane_image = PhotoImage(file="plane.gif")
        
        # set window attributes
        self.title("TRANSPORT")
        
        # add components
        self.add_heading_label()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()


    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.pack(side=TOP)
        self.heading_label.configure(font="Arial 24", text="TRANSPORT", pady=50)

        
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.pack(side=LEFT)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=200,
                                             width=200)

    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.pack(side=RIGHT)
        self.bike_image_label.configure(image=self.bike_image,
                                             height=200,
                                             width=200)
 
    def add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.pack(side=RIGHT)
        self.plane_image_label.configure(image=self.plane_image,
                                             height=200,
                                             width=200)
 

 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
