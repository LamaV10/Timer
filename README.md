# Timer

This is a really simple timer written in python. After a given time it will play your music. 

# Usage

In order to have music playing you have to create a folder named "Music" inside "Source/" and then put your music in there.
After that you can execute the setup.sh script and choose "1", which will bring you to the module responsible for the music (music.py).
Now you can put your titel in line 7.
Neovim, Vim, Nano and Vscode/ium are supported in this script.
Let me know which editors you want to be added!

# Linux 

If you are on Linux, you can also copy the timer.sh file into the /bin directory. 
Before copying it you should rename the file to something like "timer", so the command will later be "timer" and not "timer.sh".  
Then you have to modify the path from the "timer" script (originally timer.sh) to cd to your "Timer" folder location. 


This is an example of how your file could look like:
cd /home/*your_username/folder/location*/Source/
python main.py


Now you should be able to directly type the command "timer" into your terminal.
(This is just experimental!)

# Requirements

- Python with the dependencies from requirements.txt installed
- Bash to execute the scripts
