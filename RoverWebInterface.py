 #!/usr/bin/python 
 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import tty, termios, time, webiopi, datetime     
import atexit

# create a default object, no changes to I2C address or frequency
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

myMotor1.setSpeed(200)
myMotor2.setSpeed(200)
myMotor3.setSpeed(200)
myMotor4.setSpeed(200)


# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#define motor's control

def forward():
 myMotor1.run(Adafruit_MotorHAT.FORWARD)
 myMotor2.run(Adafruit_MotorHAT.FORWARD)
 myMotor3.run(Adafruit_MotorHAT.FORWARD)
 myMotor4.run(Adafruit_MotorHAT.FORWARD)
 time.sleep(0.07)

def backward():
 myMotor1.run(Adafruit_MotorHAT.BACKWARD)
 myMotor2.run(Adafruit_MotorHAT.BACKWARD)
 myMotor3.run(Adafruit_MotorHAT.BACKWARD)
 myMotor4.run(Adafruit_MotorHAT.BACKWARD)
 time.sleep(0.07)


def left():
 myMotor1.run(Adafruit_MotorHAT.FORWARD)
 myMotor2.run(Adafruit_MotorHAT.FORWARD)
 #myMotor4.run(Adafruit_MotorHAT.BACKWARD)
 myMotor3.run(Adafruit_MotorHAT.BACKWARD)
 time.sleep(0.07)

def right():
 #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
 myMotor2.run(Adafruit_MotorHAT.BACKWARD)
 myMotor4.run(Adafruit_MotorHAT.FORWARD)
 myMotor3.run(Adafruit_MotorHAT.FORWARD)
 time.sleep(0.07)

def stop():
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
        myMotor2.run(Adafruit_MotorHAT.RELEASE)
        myMotor3.run(Adafruit_MotorHAT.RELEASE)
        myMotor4.run(Adafruit_MotorHAT.RELEASE)

def speed0():
        myMotor1.setSpeed(255)
        myMotor2.setSpeed(255)
        myMotor3.setSpeed(255)
        myMotor4.setSpeed(255)

def speed9():
        myMotor1.setSpeed(230)
        myMotor2.setSpeed(230)
        myMotor3.setSpeed(230)
        myMotor4.setSpeed(230)

def speed8():
        myMotor1.setSpeed(205)
        myMotor2.setSpeed(205)
        myMotor3.setSpeed(205)
        myMotor4.setSpeed(205)

def speed7():
        myMotor1.setSpeed(180)
        myMotor2.setSpeed(180)
        myMotor3.setSpeed(180)
        myMotor4.setSpeed(180)

def speed6():
        myMotor1.setSpeed(155)
        myMotor2.setSpeed(155)
        myMotor3.setSpeed(155)
        myMotor4.setSpeed(155)

def speed5():
        myMotor1.setSpeed(130)
        myMotor2.setSpeed(130)
        myMotor3.setSpeed(130)
        myMotor4.setSpeed(130)

def speed4():
        myMotor1.setSpeed(105)
        myMotor2.setSpeed(105)
        myMotor3.setSpeed(105)
        myMotor4.setSpeed(105)

def speed3():
        myMotor1.setSpeed(80)
        myMotor2.setSpeed(80)
        myMotor3.setSpeed(80)
        myMotor4.setSpeed(80)

def speed2():
        myMotor1.setSpeed(55)
        myMotor2.setSpeed(55)
        myMotor3.setSpeed(55)
        myMotor4.setSpeed(55)

def speed1():
        myMotor1.setSpeed(30)
        myMotor2.setSpeed(30)
        myMotor3.setSpeed(30)
        myMotor4.setSpeed(30)

server = webiopi.Server(port=8000, login="webiopi", password="raspberrypi")

server.addMacro(forward)
server.addMacro(backward)
server.addMacro(right)
server.addMacro(left)
server.addMacro(stop)
server.addMacro(speed1)
server.addMacro(speed2)
server.addMacro(speed3)
server.addMacro(speed4)
server.addMacro(speed5)
server.addMacro(speed6)
server.addMacro(speed7)
server.addMacro(speed8)
server.addMacro(speed9)
server.addMacro(speed0)

webiopi.runLoop()
server.stop()
