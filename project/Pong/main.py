from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

screen=Screen()


screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle=Paddle((350,0))
r_paddle=Paddle((-350,0))
ball=Ball()

screen.listen()
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")
screen.onkey(r_paddle.go_up,"w")
screen.onkey(r_paddle.go_down,"s")

game_is_on=True
while game_is_on:
	time.sleep(0.1)
	screen.update()
	ball.move()
	#detect collision with the wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	#detect collsion with the paddle
	if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	#checking for the l_paddle miss
	if ball.xcor() >380:
		ball.miss()

	#checking for the r_paddle miss
	if ball.xcor() < -380:
	 	ball.miss()
	




screen.exitonclick()