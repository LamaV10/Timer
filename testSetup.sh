echo "What do you want to setup?"
echo "Wich Song is going to be played (1) or path of the Timer-folder in timer.sh (2):"
read modify


if [ $modify -eq 1 ]; then
  echo "Please enter the location of your music file: "
  read musicLocation

  cd Source/
  echo "import pygame
from pygame import mixer
pygame.init()

def music():
      # music import/play
      # change your path to your music here:
      mixer.music.load('$musicLocation')
      

      mixer.music.set_volume(0.5)
      mixer.music.play(-1)" > music.py
fi


if [ $modify -eq 2 ]; then
  path="$(pwd)" 

  echo "cd $path/Source
python main.py" > timer.sh

  echo "The path is setup. You can copy this script into your /bin directory for easier acces now!"
fi
