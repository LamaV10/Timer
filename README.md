# Timer Python

This is a really simple timer written in python. After a given time it will play your music. 

## Usage

In order to setup Music just execute the setup.sh script and choose the first option. 
Then you can enter the location of your music file: 
```
# Execute script
./setup.sh
# Option 1 
1
# location of your music title 
/home/USER/Music/Your_Title.mp3
```

## Linux 

If you are on Linux, you can also copy the timer.sh file into the /bin directory. 
Before copying it you should rename the file to something like "timer", so the command will later be "timer" and not "timer.sh".  

Execute the setup.sh file and choose the second option. Your file should look like this afterwards: 

```
cd /home/*your_username/folder/location*/Timer/Source/
python main.py
```

Dont forget to make the script executable before copying it into /bin!
```
chmod +x timer
```
Now you should be able to directly type the command "timer" into your terminal.
(This is just experimental! It may be also possible on MacOS. Execute at your own RISK!!!)

## Requirements

- Python with the dependencies from requirements.txt installed
- Bash to execute the scripts (but it's also possible to do it all manually)


# Timer C++
A way more lightweight version of timer. The Python version almost consumes 10% of cpu on my main machine (Ryzen 5 5600) and upto 30% on potatos like my T430u.

Basic functionalities are already implementd. Currently the C++ version only works on linux.

## Build
Dependencies:
- libmpg123

Compile the with a binary called timer:
```
g++ -o timer timer.cpp music.cpp -lmpg123 -lao
```
Execute:
```
./timer
```
