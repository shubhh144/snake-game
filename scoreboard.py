import turtle as t
class score(t.Turtle):
    def __init__(self):
        super().__init__()
        with open("D:\\Coding\\python\\ch-2\\day20_snake\\hs.txt","r+") as file:
            hs=int(file.read().strip())
            self.hs=hs
        self.s=0
        self.penup()
        self.goto(-20,270)
        self.color("white")
        self.update()
        self.hideturtle()
        self.pendown()
       
    def incsco(self):
        self.s+=1
        self.clear()
        self.update()
        
    def update(self):
        self.write(f"SCORE:-{self.s}\tHigh Score:-{self.hs}", font=("Times New Roman", 12, "normal"))
    def off(self):
        with open("D:\\Coding\\python\\ch-2\\day20_snake\\hs.txt","r+") as file:
            # hs=int(file.read().strip())
            # print(hs)
            if self.hs>=self.s:
                pass
                # self.hs=hs
            else:
                file.truncate(0) 
                file.write(str(self.s))
                file.seek(0)
                hs2=int(file.read().strip())
                self.hs=hs2

            # print(hs)
            
            
            # else:
            #     self.hs=hs
        self.penup()
        self.goto(-30,0)
        self.color("white")
        self.write(f"Game over\nHigh Score:-{self.hs}\nSCORE:-{self.s}", font=("Times New Roman", 14, "normal"))
        self.hideturtle()
        self.pendown()
        
            

        
        
