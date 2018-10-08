#import evdev
from evdev import InputDevice, categorize, ecodes
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from squid import *
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

#creates object 'gamepad' to store the data
#you can call it whatever you like
#gamepad = InputDevice('/dev/input/event0')
char = ''
#prints out device info at start
#print(gamepad)
currentSpeed = 0

rgb = Squid(19, 20, 21)
while True:
    try:
        gamepad = InputDevice('/dev/input/event0')
        print(gamepad)
        gamepad.repeat = (500, 150)
        print(gamepad.repeat)
        rgb.set_color(GREEN)
        for event in gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value != 0 and event.value != 2:
                    rgb.set_color(BLUE)
                if event.value == 2:
                    rgb.set_color(PURPLE)
                    #time.sleep(.2)
                myMotor1.setSpeed(currentSpeed)
                myMotor2.setSpeed(currentSpeed)
                myMotor3.setSpeed(currentSpeed)
                myMotor4.setSpeed(currentSpeed)
#                print(categorize(event))
                if ecodes.ecodes['KEY_D'] == event.code and event.value == 1:
                    char = "D"
                    #myMotor1.setSpeed(180)
                    #myMotor2.setSpeed(180)
                    myMotor3.setSpeed(255)
                    myMotor4.setSpeed(255)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
                    #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    #myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                elif ecodes.ecodes['KEY_B'] == event.code and event.value == 1:
                    char = "B"
                elif ecodes.ecodes['KEY_C'] == event.code and event.value == 1:
                    char = "C"
                elif ecodes.ecodes['KEY_A'] == event.code and event.value == 1:
                    char = "A"
                    myMotor1.setSpeed(255)
                    myMotor2.setSpeed(255)
                    #myMotor3.setSpeed(180)
                    #myMotor4.setSpeed(180)
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    #myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    #myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                    #time.sleep(1)
                elif ecodes.ecodes['KEY_E'] == event.code and event.value == 1:
                    char = "E"
                elif ecodes.ecodes['KEY_F'] == event.code and event.value == 1:
                    char = "F"
                elif ecodes.ecodes['KEY_G'] == event.code and event.value == 1:
                    char = "G"
                elif ecodes.ecodes['KEY_H'] == event.code and event.value == 1:
                    char = "H"
                elif ecodes.ecodes['KEY_I'] == event.code and event.value == 1:
                    char = "I"
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                elif ecodes.ecodes['KEY_J'] == event.code and event.value == 1:
                    char = "J"
                    myMotor1.setSpeed(255)
                    myMotor2.setSpeed(255)
                    myMotor3.setSpeed(105)
                    myMotor4.setSpeed(105)
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                elif ecodes.ecodes['KEY_K'] == event.code and event.value == 1:
                    char = "K"
                    myMotor1.setSpeed(105)
                    myMotor2.setSpeed(105)
                    myMotor3.setSpeed(255)
                    myMotor4.setSpeed(255)
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                elif ecodes.ecodes['KEY_L'] == event.code and event.value == 1:
                    char = "L"
                elif ecodes.ecodes['KEY_M'] == event.code and event.value == 1:
                    char = "M"
                elif ecodes.ecodes['KEY_N'] == event.code and event.value == 1:
                    char = "N"
                elif ecodes.ecodes['KEY_O'] == event.code and event.value == 1:
                    char = "O"
                elif ecodes.ecodes['KEY_P'] == event.code and event.value == 1:
                    char = "P"
                elif ecodes.ecodes['KEY_Q'] == event.code and event.value == 1:
                    char = "Q"
                elif ecodes.ecodes['KEY_R'] == event.code and event.value == 1:
                    char = "R"
                elif ecodes.ecodes['KEY_S'] == event.code and event.value == 1:
                    char = "S"
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                elif ecodes.ecodes['KEY_T'] == event.code and event.value == 1:
                    char = "T"
                elif ecodes.ecodes['KEY_U'] == event.code and event.value == 1:
                    char = "U"
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                elif ecodes.ecodes['KEY_V'] == event.code and event.value == 1:
                    char = "V"
                elif ecodes.ecodes['KEY_W'] == event.code and event.value == 1:
                    char = "W"
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
#                    time.sleep(1)
                elif ecodes.ecodes['KEY_X'] == event.code and event.value == 1:
                    char = "X"
                elif ecodes.ecodes['KEY_Y'] == event.code and event.value == 1:
                    char = "Y"
                elif ecodes.ecodes['KEY_Z'] == event.code and event.value == 1:
                    char = "Z"
                elif ecodes.ecodes['KEY_1'] == event.code and event.value == 1:
                    char = "1"
                    currentSpeed = 25
                    myMotor1.setSpeed(25)
                    myMotor2.setSpeed(25)
                    myMotor3.setSpeed(25)
                    myMotor4.setSpeed(25)
                elif ecodes.ecodes['KEY_2'] == event.code and event.value == 1:
                    char = "2"
                    currentSpeed = 55
                    myMotor1.setSpeed(55)
                    myMotor2.setSpeed(55)
                    myMotor3.setSpeed(55)
                    myMotor4.setSpeed(55)
                elif ecodes.ecodes['KEY_3'] == event.code and event.value == 1:
                    char = "3"
                    currentSpeed = 80
                    myMotor1.setSpeed(80)
                    myMotor2.setSpeed(80)
                    myMotor3.setSpeed(80)
                    myMotor4.setSpeed(80)
                elif ecodes.ecodes['KEY_4'] == event.code and event.value == 1:
                    char = "4"
                    currentSpeed = 105
                    myMotor1.setSpeed(105)
                    myMotor2.setSpeed(105)
                    myMotor3.setSpeed(105)
                    myMotor4.setSpeed(105)
                elif ecodes.ecodes['KEY_5'] == event.code and event.value == 1:
                    char = "5"
                    currentSpeed = 130
                    myMotor1.setSpeed(130)
                    myMotor2.setSpeed(130)
                    myMotor3.setSpeed(130)
                    myMotor4.setSpeed(130)
                elif ecodes.ecodes['KEY_6'] == event.code and event.value == 1:
                    char = "6"
                    currentSpeed = 155
                    myMotor1.setSpeed(155)
                    myMotor2.setSpeed(155)
                    myMotor3.setSpeed(155)
                    myMotor4.setSpeed(155)
                elif ecodes.ecodes['KEY_7'] == event.code and event.value == 1:
                    char = "7"
                    currentSpeed = 180
                    myMotor1.setSpeed(180)
                    myMotor2.setSpeed(180)
                    myMotor3.setSpeed(180)
                    myMotor4.setSpeed(180)
                elif ecodes.ecodes['KEY_8'] == event.code and event.value == 1:
                    char = "8"
                    currentSpeed = 205
                    myMotor1.setSpeed(205)
                    myMotor2.setSpeed(205)
                    myMotor3.setSpeed(205)
                    myMotor4.setSpeed(205)
                elif ecodes.ecodes['KEY_9'] == event.code and event.value == 1:
                    char = "9"
                    currentSpeed = 230
                    myMotor1.setSpeed(230)
                    myMotor2.setSpeed(230)
                    myMotor3.setSpeed(230)
                    myMotor4.setSpeed(230)
                elif ecodes.ecodes['KEY_0'] == event.code and event.value == 1:
                    char = "0"
                    currentSpeed = 255
                    myMotor1.setSpeed(255)
                    myMotor2.setSpeed(255)
                    myMotor3.setSpeed(255)
                    myMotor4.setSpeed(255)
                if ecodes.ecodes['KEY_D'] == event.code and event.value == 2:
                    char = "D-H"
                    #myMotor1.setSpeed(180)
                    #myMotor2.setSpeed(180)
                    myMotor3.setSpeed(255)
                    myMotor4.setSpeed(255)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
                    #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    #myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                if ecodes.ecodes['KEY_B'] == event.code and event.value == 2:
                    char = "B-H"
                if ecodes.ecodes['KEY_C'] == event.code and event.value == 2:
                    char = "C-H"
                if ecodes.ecodes['KEY_A'] == event.code and event.value == 2:
                    char = "A-H"
                    myMotor1.setSpeed(255)
                    myMotor2.setSpeed(255)
                    #myMotor3.setSpeed(180)
                    #myMotor4.setSpeed(180)
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    #myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    #myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                if ecodes.ecodes['KEY_E'] == event.code and event.value == 2:
                    char = "E-H"
                if ecodes.ecodes['KEY_F'] == event.code and event.value == 2:
                    char = "F-H"
                if ecodes.ecodes['KEY_G'] == event.code and event.value == 2:
                    char = "G-H"
                if ecodes.ecodes['KEY_H'] == event.code and event.value == 2:
                    char = "H-H"
                if ecodes.ecodes['KEY_I'] == event.code and event.value == 2:
                    char = "I-H"
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                if ecodes.ecodes['KEY_J'] == event.code and event.value == 2:
                    char = "J-H"
                if ecodes.ecodes['KEY_K'] == event.code and event.value == 2:
                    char = "K-H"
                if ecodes.ecodes['KEY_L'] == event.code and event.value == 2:
                    char = "L-H"
                if ecodes.ecodes['KEY_M'] == event.code and event.value == 2:
                    char = "M-H"
                if ecodes.ecodes['KEY_N'] == event.code and event.value == 2:
                    char = "N-H"
                if ecodes.ecodes['KEY_O'] == event.code and event.value == 2:
                    char = "O-H"
                if ecodes.ecodes['KEY_P'] == event.code and event.value == 2:
                    char = "P-H"
                if ecodes.ecodes['KEY_Q'] == event.code and event.value == 2:
                    char = "Q-H"
                if ecodes.ecodes['KEY_R'] == event.code and event.value == 2:
                    char = "R-H"
                if ecodes.ecodes['KEY_S'] == event.code and event.value == 2:
                    char = "S-H"
                    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                if ecodes.ecodes['KEY_T'] == event.code and event.value == 2:
                    char = "T-H"
                if ecodes.ecodes['KEY_U'] == event.code and event.value == 2:
                    char = "U-H"
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.BACKWARD)
                    myMotor4.run(Adafruit_MotorHAT.BACKWARD)
                if ecodes.ecodes['KEY_V'] == event.code and event.value == 2:
                    char = "V-H"
                if ecodes.ecodes['KEY_W'] == event.code and event.value == 2:
                    char = "W-H"
                    myMotor1.run(Adafruit_MotorHAT.FORWARD)
                    myMotor2.run(Adafruit_MotorHAT.FORWARD)
                    myMotor3.run(Adafruit_MotorHAT.FORWARD)
                    myMotor4.run(Adafruit_MotorHAT.FORWARD)
                if ecodes.ecodes['KEY_X'] == event.code and event.value == 2:
                    char = "X-H"
                if ecodes.ecodes['KEY_Y'] == event.code and event.value == 2:
                    char = "Y-H"
                if ecodes.ecodes['KEY_Z'] == event.code and event.value == 2:
                    char = "Z-H"
                if ecodes.ecodes['KEY_1'] == event.code and event.value == 2:
                    char = "1-H"
                if ecodes.ecodes['KEY_2'] == event.code and event.value == 2:
                    char = "2-H"
                if ecodes.ecodes['KEY_3'] == event.code and event.value == 2:
                    char = "3-H"
                if ecodes.ecodes['KEY_4'] == event.code and event.value == 2:
                    char = "4-H"
                if ecodes.ecodes['KEY_5'] == event.code and event.value == 2:
                    char = "5-H"
                if ecodes.ecodes['KEY_6'] == event.code and event.value == 2:
                    char = "6-H"
                if ecodes.ecodes['KEY_7'] == event.code and event.value == 2:
                    char = "7-H"
                if ecodes.ecodes['KEY_8'] == event.code and event.value == 2:
                    char = "8-H"
                if ecodes.ecodes['KEY_9'] == event.code and event.value == 2:
                    char = "9-H"
                if ecodes.ecodes['KEY_0'] == event.code and event.value == 2:
                    char = "0-H"

                time.sleep(.12)
                #if event.value != 0 and event.value != 2:
                if event.value == 0:
                    turnOffMotors()
                if event.value != 0:
                    print(char)
                    rgb.set_color(OFF)

                #turnOffMotors()
#                time.sleep(1)
#    except KeyboardInterrupt:

    except:
        rgb.set_color(RED)
        continue
