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
	    cout << "Time is over! Press control + c to quit." << "\n";
	    playAudio();
	    run = false;
	}
	currUnixTime++;
	sleep(1);
    }
}
