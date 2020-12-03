import array
import math
from ola.ClientWrapper import ClientWrapper


wrapper = None
spotHeight = 84 #The height of the spotlight above the stage in inches (Z axis)
spotLength = 120 #The position of the spotlight from the front left corner of the stage in inches (X axis)

x = 0 #horizontal axis; length
y = 0 #vertical axis; width
z = 0 #up down axis; height
#        Z
#        ^    Y
#        |  /
#        | /
#        |/
#(0,0,0) +---------> X
turn = 0
tilt = 0
#The starting/"zero" DMX turn value used to change the starting position of the spotlight
turnZero = 85
#The starting/"zero" DMX tilt value used to change the starting position of the spotlight
tiltZero = 135
#Sets the Tick rate in milliseconds
TICK_INTERVAL = 100
testData = open("testdata", "r")

def main():
    global x, y, z
    line = testData.readline()
    data = line.split(',')
    x = int(data[0])
    y = int(data[1])
    z = int(data[2])
    print(str(x) + " " + str(y))
    # input = raw_input("Enter x:\n")
    # x = int(input)
    # input = raw_input("Enter y:\n")
    # y = int(input)
    angle = calculateTurnAngle(x, y, z)
    turn = turnZero + ((angle/90)*43)
    angle = calculateTiltAngle(x, y, z)
    tilt = ((angle/90)*135)
    sendDMXFrame(turn, tilt)
    wrapper.AddEvent(TICK_INTERVAL, main)

def sendDMXFrame(turn, tilt):
    data = array.array('B', [int(turn),0,int(tilt),0,0,255,255,255,255])
    wrapper.Client().SendDmx(1, data)
    print ("Running...")

def calculateTurnAngle(x, y, z):
    global spotLength
    tempWidth = spotLength - x
    tempDist = y
    angle = math.atan(float(tempWidth)/tempDist)
    return math.degrees(angle)

def calculateTiltAngle(x, y, z):
    global spotHeight, spotLength
    dist = math.sqrt(math.pow((x-spotLength), 2) + math.pow(y,2))
    angle = math.atan(float(max(0,spotHeight-z))/dist)
    return math.degrees(angle)

class Channel:
    def __init__(self, name, dmxchan):
        self.name = name
        self.dmxchan = dmxchan


wrapper = ClientWrapper()
wrapper.AddEvent(TICK_INTERVAL, main)
wrapper.Run()
