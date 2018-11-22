from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

    # load images
        self.map_image = PhotoImage(file="map.gif")
        self.bus_image = PhotoImage(file="bus.gif")
        self.red_icon_image = PhotoImage(file="red_marker.gif")
        self.black_icon_image = PhotoImage(file="black.gif")

        # Add components
        self.add_heading_label()
        self.add_map_frame()
        self.add_map_image_label()
        self.add_bus_image_label()
     

    # set window properties
        self.title("BUS JOURNEY")

    
    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.pack(fill=X)
        self.heading_label.configure(font="Arial 18",
                                     text="Bus Journey")

    def add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.pack(fill=X)
        self.map_frame.configure(width=500, height=500)


    def add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)


    def add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>",self.bus_move)


    def bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
        self.bus_image_label.place(x=event.x, y=event.y) 





    
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
