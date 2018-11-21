from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    # Initialise the Gui object
    # Self = the function belongs to this name
    # Pass = placeholder. Does nothing
    def __init__(self):
        super().__init__()

         # load resources
        self.ambulance_image = PhotoImage(file="ambulance.gif")


        # Set window attributes
        self.title("Newsletter")
        self.configure(bg="white",
                       height=400,
                       width=500,
                       pady=20,
                       padx=20)


        # Add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        self.add_ambulance_image_label()

        self.add_subscribe_button()

    def add_heading_label(self):
        # 1) Create the component
        self.heading_label = Label()
        self.heading_label.pack(side=TOP)
        # 2) Style the component
        self.heading_label.configure(font="Arial 24", bg="white", text="RECEIVE OUR NEWSLETTER", padx=30, pady=30)


    # 3) Assigning events to the component

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.pack()
        self.instruction_label.configure(font="Arial 10", bg="white", text="Please enter your email below to receive our newsletter.", pady=15 )

    def add_subscribe_button(self):
        # Create the component
        self.subscribe_button = Button()
        self.subscribe_button.pack()
        self.subscribe_button.configure(font="Arial 10", bg="white", text="Subscribe", width=50)
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)
        
 
    def subscribe_button_clicked(self, event):
        num_clicks = self.email_entry.get()
        messagebox.showinfo("Gui", "Subscribed!")


    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(font="Arial 10", bg="white", text="Email:")


    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
        self.email_entry.configure(font="Arial 10", bg="white", width=30)
            
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.pack(side=RIGHT)
        self.ambulance_image_label.configure(image=self.ambulance_image,height=10, width=10, padx=10, pady=10)
        
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()
        self.email_frame.configure(pady=30, bg="white")
