from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        #Direction randomizer
        starts = [-3, -2, -2, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        #Ensure ball bounces off sides of screen
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:     #Check to see if the ball touches the ceiling
            self.y = 1      #If so, start bouncing down

        if pos[3] >= self.canvas_height:    #Check to see if the ball touches the bottom of screen
            self.y = -1     #If so, start bouncing up

        if pos[0] <= 0:     #Check to see if ball touches left sides
            self.x = 3      #If so, start bouncing right

        if pos[2] >= self.canvas_width:     #Check to see if ball touches right side
            self.x = -3     #If so, start boucning left

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

    def draw(self):
        pass
tk = Tk()
tk.title("Pong Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


