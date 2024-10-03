import time
import math
import pygame
import music
from pygame import mixer

pygame.init()

stop = 0

#amount of time is being set
userDelay = float(input("Minutes: "))
delay = userDelay * 60
unix_time_diff = time.time() + delay 
current_time = time.time()

run = True 
while run:
    # music import/play
    current_time = time.time()

    leftoverTime = unix_time_diff - current_time
    printMinutes = leftoverTime / 60
    printSeconds = unix_time_diff - current_time
    secondsFromMinutes = round(userDelay) * 60

    if current_time > unix_time_diff:
        music.music()

    if current_time > unix_time_diff:
        stop = int(input("Type 1 and press enter to stop the timer: "))
    
    if leftoverTime <= 60:
        print(round(printSeconds, 1), "s")

    if leftoverTime > 60:
        print(math.trunc(printMinutes),":", round(printSeconds - secondsFromMinutes), "min")

    if printSeconds - secondsFromMinutes < 0:
        userDelay = userDelay - 1

    if stop == 1:
        run = False 
