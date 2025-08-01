#include <ctime>
#include <chrono>
#include <iostream>
#include <unistd.h>

using namespace std;
int main(){
    const auto p1 = std::chrono::system_clock::now();
    auto currUnixTime = std::chrono::duration_cast<std::chrono::seconds>(p1.time_since_epoch()).count();

    int time;
    cout << "Minutes: ";
    cin >> time;
    time = (time * 60) + currUnixTime;

    bool run = true;
    while(run){
	if(currUnixTime == time || currUnixTime > time){
	    cout << "Time is over" << "\n";
	    run = false;
	}
	sleep(1);
    }
}
