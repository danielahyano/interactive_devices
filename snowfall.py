'''
Creative Embedded Systems Project 2
Author: Daniela Hikari Yano
Code adapted from https://www.geeksforgeeks.org/snowfall-display-using-pygame-in-python/
Date: 03/28/2023
'''

import serial
import pygame
import random
import time
from pygame import mixer


def get_input(ser):
    '''
    This function receives the serial.Serial() object as input to return the buttons values.
    The data = ser.readline() has form b'2077, 2065, 1, 1\n', where we have b'xvalue, yvalue, zvalue, buttonvalue\\n

    :param ser:
    :return:
    '''
    data = ser.readline()

    if len(str(data).split((', '))) == 4:
        data_list = str(data)[2:-3].split(', ')
        x = data_list[0]
        y = data_list[1]
        z = data_list[2]
        b = data_list[3]
        return x,y,z,b
    return None, None, None, None

def snow():
    pygame.init()

    # serial connection: (that is how we connect to the )
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = '/dev/cu.wchusbserial54350008931'
    ser.open()

    #setting up the colors
    X_SIZE = 1100
    Y_SIZE = 750
    WHITE = [255, 255, 255]
    GREEN = [0, 255, 0]
    BLUE = [0,191,255]
    SIZE = [X_SIZE, Y_SIZE]

    # Background song:
    mixer.init()
    mixer.music.load("fireplace.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    #some variables
    clock = pygame.time.Clock()
    done = False
    change = True
    a = 0

    snowFall = []
    for i in range(500):
        x = random.randrange(0, X_SIZE)
        y = random.randrange(0, Y_SIZE)
        snowFall.append([x, y])

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Snow")

    pastTime = time.time()
    produce_snow = False
    while not done:
        currentTime = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # going to add a 1s delay:
        x, y, z, b = get_input(ser)

        if x is not None:
            #press the z buttom if you want to change the color of the sky
            if int(b) == 0:
                print(b)
                if produce_snow:
                    produce_snow = False
                else:
                    produce_snow = True

            if change:
                # will change the green part of RGB based on the x axis
                g = int((180*int(x))/4095)
                # will change the red part of RGB based on the y axis
                r = int((100 * int(y)) / 4095)
                BLUE[1]= g
                BLUE[0]=r

            if currentTime - pastTime > 1 and produce_snow:
                if a >= Y_SIZE:
                    a = 0
                else:
                    a+= 0.1
                pastTime = currentTime

        screen.fill(BLUE)

        for i in range(len(snowFall)):
            if produce_snow:
                pygame.draw.circle(screen, WHITE, snowFall[i], 2)
                snowFall[i][1] += 1
                if snowFall[i][1] > Y_SIZE:
                    y = random.randrange(-50, -10)
                    snowFall[i][1] = y

                    x = random.randrange(0, X_SIZE)
                    snowFall[i][0] = x
            else:
                if snowFall[i][1] > 0:
                    pygame.draw.circle(screen, WHITE, snowFall[i], 2)
                    snowFall[i][1] += 1
                    if snowFall[i][1] > Y_SIZE:
                        y = random.randrange(-50, -1)
                        snowFall[i][1] = y

                        x = random.randrange(0, X_SIZE)
                        snowFall[i][0] = x
                else:
                    y = random.randrange(-Y_SIZE, -1)
                    snowFall[i][1] = y

        pygame.draw.rect(screen, WHITE, pygame.Rect(0, Y_SIZE - a, X_SIZE, Y_SIZE))
        pygame.display.flip()
        clock.tick(2000)
    pygame.quit()

if __name__ == "__main__":
   snow()

# Arduino code below
# int xyzPins[] = {13, 12, 17};  //x,y,z pins
# int b = 1;
# int lastState = HIGH; // the previous state from the input pin
# int currentState;
#
# void setup() {
#   Serial.begin(9600);
#   pinMode(xyzPins[2], INPUT_PULLUP);  //z axis is a button.
#   pinMode(21, INPUT_PULLUP);  //button.
# }
# void loop() {
#   int xVal = analogRead(xyzPins[0]);
#   int yVal = analogRead(xyzPins[1]);
#   int zVal = digitalRead(xyzPins[2]);
#   currentState = digitalRead(21);
#
#   if(lastState == LOW && currentState == HIGH){
#     // Serial.println("The state changed from LOW to HIGH");
#     b = 0;
#   }
#   lastState = currentState;
#   // Serial.print(buttonVal);
#   Serial.printf("%d, %d, %d, %d", xVal, yVal, zVal, b);
#   b = 1;
#   Serial.print('\n');
#   delay(100);
# }