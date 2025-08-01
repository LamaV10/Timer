#include "music.h"
#include <ctime>
#include <chrono>
#include <iostream>
#include <unistd.h>
#include <mpg123.h>
#include <ao/ao.h>

void audioInit();
void playAudio();

using namespace std;
void printTime(int time, int currUnixTime){
    int timeLeft;
    int timeLeftMin;
    int secondsOfCurrMinuts;
    timeLeft = time - currUnixTime;
    timeLeftMin = timeLeft / 60;
    secondsOfCurrMinuts = timeLeft - ((timeLeft / 60) * 60);

    if(timeLeft > 60){
	cout << "\r" << timeLeftMin << ":" << secondsOfCurrMinuts << " " <<std::flush;
    } else {
	cout << "\r" << timeLeft << " " <<std::flush;
    }
}

int main(){
    audioInit();
    const auto p1 = std::chrono::system_clock::now();
    auto currUnixTime = std::chrono::duration_cast<std::chrono::seconds>(p1.time_since_epoch()).count();

    int time;
    cout << "Minutes: ";
    cin >> time;
    time = (time * 60) + currUnixTime;

    bool run = true;
    while(run){
	if(currUnixTime == time || currUnixTime > time){
	    cout << "\n" << "Time is over! Press control + c to quit." << "\n";
	    playAudio();
	    run = false;
	}
	printTime(time, currUnixTime);
	currUnixTime++;
	sleep(1);
    }
}
