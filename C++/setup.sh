echo "Please enter the location of your music file: "
read musicLocation

cd src/
echo "// #include "timer.cpp"
#include <ctime>
#include <chrono>
#include <iostream>
#include <unistd.h>
#include <mpg123.h>
#include <ao/ao.h>

void audioInit(){
    mpg123_init();
    ao_initialize();
}

void playAudio(){
    mpg123_handle *mh = mpg123_new(NULL, NULL);
    mpg123_open(mh, "$musicLocation");

    // set up audio output
    long rate; // Declare rate
    int channels; // Declare channels
    int encoding; // Declare encoding
    mpg123_getformat(mh, &rate, &channels, &encoding); // Get format

    // Set up the audio format structure
    ao_sample_format format;
    format.bits = 16; // Set bits per sample (usually 16 for PCM)
    format.channels = channels; // Set number of channels
    format.rate = rate; // Set sample rate
    format.byte_format = AO_FMT_NATIVE; // Set byte format (native)
    
    int driver = ao_default_driver_id();
    ao_device *device = ao_open_live(driver, &format, NULL); // Pass the format structure

    // Start playing the file
    unsigned char *buffer;
    size_t buffer_size = 4096; // Set buffer size
    buffer = (unsigned char *)malloc(buffer_size); // Allocate buffer
    size_t done;
    
    // Read and decode the audio
     while (mpg123_read(mh, buffer, buffer_size, &done) == MPG123_OK) { // Check for MPG123_OK
	    ao_play(device, (char *)buffer, done); // Use done directly
    }
    // Clean up
    free(buffer); // Free allocated buffer
    ao_close(device);
    mpg123_delete(mh);
    mpg123_exit();
    ao_shutdown();
}
" > music.cpp
fi
