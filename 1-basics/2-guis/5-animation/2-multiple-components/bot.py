from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="umbrella.gif")
        self.bike_image = PhotoImage(file="bike.gif")
         
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 200
        self.ball_y_pos = 20
        self.ball_x_change = -10
        self.ball_y_change = 10

        self.bike_x_pos = 300
        self.bike_y_pos = 200
        self.bike_x_change = 10
        self.bike_y_change = 10

        
        # add components
        self.add_ball_image_label()
        self.add_bike_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change 
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        #IMAGE ONE

        #right
        if self.ball_x_pos >= 384:
            self.ball_x_change = -self.ball_x_change

        #bottom
        if self.ball_y_pos <= 0:
            self.ball_y_change = -self.ball_y_change

        #left
        if self.ball_x_pos <= 0:
            self.ball_x_change = -self.ball_x_change

        #top
        if self.ball_y_pos >= 384:
            self.ball_y_change = -self.ball_y_change



        #IMAGE TWO
            
        self.bike_x_pos = self.bike_x_pos + self.bike_x_change 
        self.bike_y_pos = self.bike_y_pos + self.bike_y_change
        self.bike_image_label.place(x=self.bike_x_pos, 
                                    y=self.bike_y_pos)

        #right
        if self.bike_x_pos <= 0:
            self.bike_x_change = -self.bike_x_change

        #bottom
        if self.bike_y_pos <= 0:
            self.bike_y_change = -self.bike_y_change

        #left
        if self.bike_x_pos >= 384:
            self.bike_x_change = -self.bike_x_change

        #top
        if self.bike_y_pos >= 384:
            self.bike_y_change = -self.bike_y_change


        
        self.after(100, self.tick)

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)



    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.place(x=self.bike_x_pos,
                                    y=self.bike_y_pos)
        self.bike_image_label.configure(image=self.bike_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
     
