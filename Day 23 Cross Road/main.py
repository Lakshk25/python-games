import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(user.go_up , "Up")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars() 

    #Detect collision with car
    for car in car_manager.all_cars: 
        if car.distance(user) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing

    if user.is_at_finish_line():
        user.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    

screen.exitonclick()
