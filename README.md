**IMPORTANT README. READ THIS FOR CLEAR INSTRUCTIONS ON HOW TO MAKE THIS PROJECT WORK SUCCESSFULLY**


# Audio-Record-Playback-using-Raspberry-Pi

This is a simple project to record and playback audio using a raspberry pi in mp3 format
The project uses two push buttons to record and playback audio.
When the record button is long pressed, the project starts recording audio.
When the record button is released, the project stops recording and the audio is saved first as a .wav file and is then encoded into .mp3 format using pydub and saved onto the sd card in the raspberry pi 4.
The recording is saved in a directory called "recordings". If the directory doesnt already exist, the python script automatically creates the directory and saves the audio in the directory.
When the play button is pressed, the project plays the recorded audio through a usb speaker.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**COMPONENTS:**
1-Raspberry Pi 4B
2- Micro SD Card
3- USB Microphone
4- USB/AUX Speaker


**How to setup:
**
1- Format the sd card as fat32


2- Use raspberry pi imager to flash the pi os onto the sd card. download from here: https://www.raspberrypi.com/software/


3- Setup the raspberry pi and connect to wifi network


4- Open terminal using ctrl+alt+t


5- Create a directory called "Project" using the command:
    
    mkdir Project
    
6- Now if you type in ls into the terminal you can see a directory called Project has been made.


7- Now change to this new directory using:
    
    cd Project
    

8- Install the ffmpeg dependency for pydub using:
    
    sudo apt-get install ffmpeg
    
    
9- Now install a virtual environment package using:
    
    sudo apt-get install python3-venv

    

10- Create the virtual environment using:
    
    python3 -m venv venv
    
    
11- Activate the virtual environment using:
    
    source venv/bin/activate
    
    
12- Now download and extract the file saved from this respository in the Project 


13- Make sure that the virtual environment is activated before you install the libraries otherwise it will give an error.


14- To activate the environment if not already activated, use: 
    
    source venv/bin/activate
    
15- Install the required libraries using:


  Pydub:
  For working with audio files
  
    pip install pydub
    

Pygame:
  For playing audio through speakers

    pip install pygame


RPi.GPIO:
  For the GPIO coniguration

    pip install RPi.GPIO


Pyaudio:
  For recording audio from USB Microphone

    pip install pyaudio



16- Run the python script using:
    
    python3 audio_recorder.py

