import turtle as t
import time
import snake_game as sg
import food as f
import scoreboard as S
s=t.Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("My snake Game")
s.tracer(0)

# starting_snake=[(0,0),(-20,0),(-40,0)]

b=sg.snake()
F=f.food()
sco=S.score()
s.listen()
s.onkey(key="Left",fun=b.left)
s.onkey(key="Right",fun=b.right)
s.onkey(key="Up",fun=b.up)
s.onkey(key="Down",fun=b.down)
game_on=True
while(game_on):
    s.update()
    time.sleep(0.1)
    b.move()
    # collision with food
    if b.head.distance(F)<15:
        F.refresh()
        sco.incsco()
        b.extend()
        print("Ghavla")
    # collision with wall
    if b.head.xcor()<-280 or b.head.xcor()>280 or b.head.ycor()<-280 or b.head.ycor()>280:
        game_on=False
        sco.off()
    # collision with tail
    for segment in b.seg[1:]:#[1:]it is use for slicing because of this except )th postion array traverce from 1st position
        if b.head.distance(segment)<7:
            game_on=False
            sco.off()







s.exitonclick()


