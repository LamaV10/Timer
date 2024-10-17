import time
import math
import sys
import pygame
import music
from pygame import mixer

pygame.init()

def delete_last_line():
    # Cursor up one line.
    sys.stdout.write('\x1b[1A')

    # Delete last line.
    sys.stdout.write('\x1b[2K')

stop = 0
# Amount of time is being set.
userDelay = float(input("Minutes: "))
# Full minutes that are left over.
fullMinutes = math.trunc(userDelay)
# From minutes into seconds.
delay = userDelay * 60
# Unix time + the delay the user wants.
unix_time_wanted = time.time() + delay 

run = True 
while run:
    # current unix time
    current_time = time.time()

    # Left over time between unix time and the desiered user time. 
    leftoverTime = unix_time_wanted - current_time
    # Minutes that are left over rounded down! 
    printMinutes = math.trunc(leftoverTime / 60)
    # Total seconds that are left over
    printSeconds = unix_time_wanted - current_time
    # Minutes rounded down & multiplied by 60 to get the seconds from the full minutes. This is being subtracted from the total seconds to get the leftover seconds in a minute.  
    secondsFromMinutes = (math.trunc(printSeconds)- (fullMinutes * 60))

    if current_time >= unix_time_wanted:
        music.music()

    if current_time >= unix_time_wanted:
        stop = int(input("Type 1 and press enter to stop the timer: "))
   
    # Prints seconds if the there are no more full minutes. 
    if leftoverTime <= 60:
        print(round(printSeconds, 1), "s")
        delete_last_line()

    # Prints minutes and seconds (min : sec) when there are still full minutes.
    if leftoverTime > 60:
        print((printMinutes),":", (secondsFromMinutes), "min",)
        delete_last_line()

    # When a minute is down this fullMinutes variable is being subtracted by 1. This is important for the secondsFromMinutes calculation!
    if secondsFromMinutes < 0:
        fullMinutes -= 1 

    if stop == 1:
        run = False 
