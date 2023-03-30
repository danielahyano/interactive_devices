# interactive_devices

author: Daniela Hikari Yano 

creative details at: https://danielahyano.github.io/module_2.html

## Overview:
This github directory contains the source code used for creating an Interactive Device, which I call snowfall.  
There are two parts of the code. The first one is written in C++, and is inside snowfall.ino and you need to load the code to the ESP32 (set up instructions are below). 

After loading the snowfall.ino code into the ESP32, you will run snowfall.py in your computer (this will start the program that produces snow!).
The other code is inside snowfall.py. To run it is necessary to download two libraries: pyserial and pygames (you can do this using pip). I used 
Pycharm (https://www.jetbrains.com/pycharm/) as my IDE, but you can choose an IDE you are confortable with. 

## Hardware:
- LilyGo ESP32 TTGO T-Display

- Joystick

- Button

- Cables

## Set up .ino code

The Arduino IDE can be downloaded in (https://www.arduino.cc/en/software). 

After downloading the Arduino IDE, you can follow the instructions in https://www.youtube.com/watch?v=adLUgmCJKnM (a video made by our professor) to do the setup. 

If you are on a MacBook, you may need to install: https://github.com/Xinyuan-LilyGO/LilyGo-T-Call-SIM800/issues/139#issuecomment-90439071. 

After this, you can get the code from generative_art.ino and transfer it to the ESP32 using a type C cable connected from the notebook to the device (pressing the '->' in the top left of the screen. 

