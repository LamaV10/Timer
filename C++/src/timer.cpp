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

    if(secondsOfCurrMinuts < 10 && timeLeftMin >= 1){
	cout << "\r" << timeLeftMin << " : 0" << secondsOfCurrMinuts << " min" << "  " <<std::flush;
    } else if(timeLeft > 60){
	cout << "\r" << timeLeftMin << " : " << secondsOfCurrMinuts << " min" << "  " <<std::flush;
    } else {
	cout << "\r" << timeLeft << " secs" << "   " <<std::flush;
    }
}

int main(){
    audioInit();
    const auto p1 = std::chrono::system_clock::now();
    auto currUnixTime = std::chrono::duration_cast<std::chrono::seconds>(p1.time_since_epoch()).count();

    double time;
    cout << "Minutes: ";
    cin >> time;
    time = double(time * 60.0) + double(currUnixTime);

    bool run = true;
    while(run){
	if(currUnixTime == time || currUnixTime > time){
	    cout << "\n" << "Time is over! Press control + c to quit." << "\n";
	    playAudio();
	    run = false;
	}
	currUnixTime++;
	printTime(time, currUnixTime);
	sleep(1);
    }
}
