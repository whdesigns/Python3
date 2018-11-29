from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.first_image = PhotoImage(file="first.gif")
        self.second_image = PhotoImage(file="second.gif")
        self.third_image = PhotoImage(file="third.gif")
         
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.first_x_pos = 0
        self.first_y_pos = 20
        self.first_x_change = 10
   

        self.second_x_pos = 384
        self.second_y_pos = 200
        self.second_x_change = 10


        self.third_x_pos = 0
        self.third_y_pos = 370
        self.third_x_change = 10
        self.num_ticks = 0
        


        
        # add components
        self.add_first_image_label()
        self.add_second_image_label()
        self.add_third_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function
    def tick(self):
        self.num_ticks = self.num_ticks + 1
        self.first_x_pos = self.first_x_pos + self.first_x_change 
        self.first_y_pos = self.first_y_pos 
        self.first_image_label.place(x=self.first_x_pos, 
                                    y=self.first_y_pos)
    

        if (self.num_ticks % 4 == 0):
            if self.first_x_pos >= 420:
                self.first_x_change = -self.first_x_change

        if self.first_x_pos <= 0:
            self.first_x_change = -self.first_x_change




        #IMAGE TWO
        if (self.num_ticks % 4 == 0):
            self.second_x_pos = self.second_x_pos + self.second_x_change
            self.second_image_label.place(x=self.second_x_pos, 
                                    y=self.second_y_pos)
            
            if self.second_x_pos <= 0:
                self.second_x_change = -self.second_x_change



        #right
        if self.second_x_pos <= 0:
            self.second_x_change = -self.second_x_change

        #left
        if self.second_x_pos >= 384:
            self.second_x_change = -self.second_x_change





       #IMAGE THREE
            
        self.third_x_pos = self.third_x_pos + self.third_x_change 
        self.third_image_label.place(x=self.third_x_pos, 
                                    y=self.third_y_pos)

        #right
        if self.third_x_pos <= 0:
            self.third_x_change = -self.third_x_change


        #left
        if self.third_x_pos >= 384:
            self.third_x_change = -self.third_x_change




        
        self.after(100, self.tick)

    # the ball image
    def add_first_image_label(self):
        self.first_image_label = Label()
        self.first_image_label.place(x=self.first_x_pos,
                                    y=self.first_y_pos)
        self.first_image_label.configure(image=self.first_image)



    def add_second_image_label(self):
        self.second_image_label = Label()
        self.second_image_label.place(x=self.second_x_pos,
                                    y=self.second_y_pos)
        self.second_image_label.configure(image=self.second_image)



    def add_third_image_label(self):
        self.third_image_label = Label()
        self.third_image_label.place(x=self.third_x_pos,
                                    y=self.third_y_pos)
        self.third_image_label.configure(image=self.third_image)
     
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
     
