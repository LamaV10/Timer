import time
import math
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()


# Timer for the Lapcount-collision
timer = float(input("Minuten: "))
timer = timer * 60

time.sleep(timer)

# music import/play
mixer.music.load("Music/Meat-Grinder.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

bruno = int(input("Press Enter to stop!"))
