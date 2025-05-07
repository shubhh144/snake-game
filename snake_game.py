import turtle as t
import tkinter as tk
from tkinter import messagebox
SNAKE_POS=[(0,0),(-20,0),(-40,0)]
FORW=20
class snake:
    
    def __init__(self):
        self.seg=[]
        self.create()
        self.head=self.seg[0]
     

        
        
    def create(self):
        for position in SNAKE_POS:
            self.add(position)
            
    def add(self,position):
        sap=t.Turtle("square")
        sap.color("white")
        sap.penup()
        sap.goto(position)
        self.seg.append(sap)
    def extend(self):
        self.add(self.seg[-1].position())
    def move(self):
        for i in range(len(self.seg)-1,0,-1):
            x=self.seg[i-1].xcor()
            y=self.seg[i-1].ycor()
            self.seg[i].goto(x,y)
        self.seg[0].forward(10)
    def left(self):
        if(self.seg[0].heading()!=0):
            self.seg[0].setheading(180)
    def right(self):
        if(self.seg[0].heading()!=180):
            self.seg[0].setheading(0) 
    def up(self):
        if(self.seg[0].heading()!=270):
            self.seg[0].setheading(90)
    def down(self):
        if(self.seg[0].heading()!=90):
            self.seg[0].setheading(270)



    # #for window to choose hardness level
    # def lev(self):
    #     root = tk.Tk()
    #     root.title("Levels")
    #     root.geometry("400x300")
    #     question_label = tk.Label(root, text="CHOOSE THE LEVEL", font=("Arial", 14))
    #     question_label.pack(pady=10)
    #     self.var = tk.StringVar(value="")
    #     self.options = [
    #     ("NORMAL", "A"),
    #     ("MEDIUM", "B"),
    #     ("FAST", "C"),
    #     ]
    #     for text, value in self.options:
    #         tk.Radiobutton(root, text=text, variable=self.var, value=value, font=("Arial", 12)).pack(anchor="w")
    #     submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12), bg="blue", fg="white")
    #     submit_button.pack(pady=20)
    # def check_answer(self):
    #     selected_option = self.var.get()  # Get selected option
    #     if selected_option == "A":
    #         self.level=10
    #     elif selected_option == "B":
    #         self.level=20
    #     elif selected_option == "C":
    #         self.level=30