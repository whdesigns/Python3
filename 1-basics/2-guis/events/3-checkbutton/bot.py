from tkinter import *


class Gui(Tk):
    # Initialise the Gui object
    # Self = the function belongs to this name
    # Pass = placeholder. Does nothing
    def __init__(self):
        super().__init__()


        # Set window attributes
        self.title("Song Maker")
        self.configure(bg="white",
                       height=400,
                       width=500,
                       pady=20,
                       padx=20)


        # Add components
        self.add_heading_label()
        self.add_questionone_label()
        self.add_questiontwo_label()
        self.add_questionthree_label()
        self.add_checkbox1_Checkbutton()
     
       
        

    def add_heading_label(self):
        # 1) Create the component
        self.heading_label = Label()
        self.heading_label.pack(side=TOP)
        # 2) Style the component
        self.heading_label.configure(font="Arial 24", bg="white", text="Passport Checker", padx=30, pady=30)


    # 3) Assigning events to the component

    def add_questionone_label(self):
        self.questionone_label = Label()
        self.questionone_label.pack(side=LEFT)
        self.questionone_label.configure(font="Arial 10", bg="white", text="1. Photo matches face?", pady=15 )


    def add_checkbox1_Checkbutton(self):
        option1 = Checkbutton()
        option2 = Checkbutton()
        C1 = Checkbutton(text = "Yes", variable = option1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
        C2 = Checkbutton(text = "No", variable = option2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
        C1.pack(side=BOTTOM)
        C2.pack(side=BOTTOM)
        

    def add_questiontwo_label(self):
        self.questiontwo_label = Label()
        self.questiontwo_label.pack(side=LEFT)
        self.questiontwo_label.configure(font="Arial 10", bg="white", text="2. Passport has at least 6 months validity?", pady=15 )



    def add_questionthree_label(self):
        self.questionthree_label = Label()
        self.questionthree_label.pack(side=LEFT)
        self.questionthree_label.configure(font="Arial 10", bg="white", text="3. Visa, if required, is valid?", pady=15 )




#.................................................................................................................
 
 
