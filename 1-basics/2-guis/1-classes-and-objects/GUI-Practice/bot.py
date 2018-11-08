from tkinter import *

class Gui(Tk):
        #initialise the Gui object
        def __init__(self):
                super().__init__()

                # Set window attributes
                self.title("Newsletter")
                self.configure(bg = "white",
                               height=250,
                               width=500)

                # Add components
                self.add_heading_label()
                self.add_instruction_label()
                self.add_subscribe_button()
                self.add_email_label()
                self.add_entry()
                

        def add_heading_label(self):
                #1. create the components
                self.heading_label = Label()
                self.heading_label.place(x=25, y=50)

                # 2. style the components
                self.heading_label.configure(font = "Arial 24",
                                             bg="white",
                                             text = "RECIEVE OUR NEWSLETTER")

                
                # 3. assign events to the component
                # todo

        def add_instruction_label(self):
                self.instruction_label = Label()
                self.instruction_label.place(x=75, y=100)
                self.instruction_label.configure(font="Arial 10",
                                            bg="white",
                                            anchor="center",
                                            text = "Please enter your email below to receive our newsletter.")
                
        def add_subscribe_button(self):
                self.subscribe_button = Button ()
                self.subscribe_button.place(x=50, y=200)
                self.subscribe_button.configure(font="Arial 10",
                                            bg="white",
                                            anchor="center",
                                            text="Subscribe",
                                            width="50")

        def add_email_label(self):
                self.email_label = Label()
                self.email_label.place(x=100, y=150)
                self.email_label.configure(font="Arial 10", bg="white", text="Email:")



        def add_entry(self):
                self.add_entry = Entry()
                self.add_entry.place(x=150, y=150)
                self.add_entry.configure(font="Arial 10", bg="white", width="30")

