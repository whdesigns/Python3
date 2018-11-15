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
        self.add_lyrc2add_label()
        self.add_entrybox_entry()
        self.add_add_button()
        self.add_lyrics_label()
        self.add_listBox_listbox()
     
       
        

    def add_heading_label(self):
        # 1) Create the component
        self.heading_label = Label()
        self.heading_label.pack(side=TOP)
        # 2) Style the component
        self.heading_label.configure(font="Arial 24", bg="white", text="Song Maker", padx=30, pady=30)


    # 3) Assigning events to the component

    def add_lyrc2add_label(self):
        self.lyrc2add_label = Label()
        self.lyrc2add_label.pack()
        self.lyrc2add_label.configure(font="Arial 10", bg="white", text="Lyric to add:", pady=15 )



    def add_entrybox_entry(self):
        self.entrybox_entry = Entry()
        self.entrybox_entry.pack()
        self.entrybox_entry.configure(bg="white", width=50)
        
   
 
    def add_add_button(self):
        self.add_button = Button()
        self.add_button.pack()
        self.add_button.configure(font="black", text="Add", bg="white", width=5)
        self.add_button.bind("<ButtonRelease-1>", self.add_button_clicked)


    def add_button_clicked(self, event):
        lyric = self.entrybox_entry.get()
        self.listBox_listbox.insert(END, lyric)

	
  

    def add_lyrics_label(self):
        self.lyrics_label = Label()
        self.lyrics_label.pack()
        self.lyrics_label.configure(font="Arial 10", bg="white", text="Lyrics:", pady=15)



    def add_listBox_listbox(self):
        self.listBox_listbox = Listbox()
        self.listBox_listbox.pack()
        self.listBox_listbox.configure(bg="white", width=30)
    


    
