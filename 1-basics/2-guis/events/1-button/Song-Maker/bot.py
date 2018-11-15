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
        self.add_lyrics_label()
        self.add_lyricbox_entry()
        self.add_Add_button()
        self.add_lyrics2_label()
        self.add_scrollbar_Scrollbar()
     

    def add_heading_label(self):
        # 1) Create the component
        self.heading_label = Label()
        self.heading_label.pack(side=TOP)
        # 2) Style the component
        self.heading_label.configure(font="Arial 30", bg="white", fg="black", text="Song Maker")



    def add_lyrics_label(self):
        # 1) Create the component
        self.lyrics_label = Label()
        self.lyrics_label.pack(side=LEFT)
        # 2) Style the component
        self.lyrics_label.configure(font="Arial 20", bg="white", text="Lyric to add:")


    def add_lyricbox_entry(self):
        self.lyricbox_entry = Entry(self)
        self.lyricbox_entry.pack(side=LEFT)
        self.lyricbox_entry.configure(font="Arial 10", bg="white", width=30)


        
    def add_Add_button(self):
        self.Add_button = Button()
        self.Add_button.pack(side=RIGHT)
        self.Add_button.configure(font="Arial 10", bg="white", text="Add", width=10)
        


    def add_lyrics2_label(self):
        self.lyrics2_label = Label()
        self.lyrics2_label.pack(side=BOTTOM)
        self.lyrics2_label.configure(font="Arial 20", bg="white", text="Lyrics:")

        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def add_scrollbar_Scrollbar(self):
        self.scrollbar = Scrollbar()
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(Gui, yscrollcommand=scrollbar.set)
        for i in range(1000):
          listbox.insert(END, str(i))

        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=listbox.yview)
          
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
