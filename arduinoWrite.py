import serial
import time

arduino = '/dev/ttyACM0'
# serialLED.timeout = 1

class Arduino():

    def __init__(self):
        self.blink = 0
        self.ledState = 1
        self.serialLED = serial.Serial(arduino, 9600, timeout=1)

    def setBlink(self, blinkBit):
        self.blink = blinkBit

    def setState(self, state):
        self.ledState = state

    def getState(self):
        return self.ledState

    # Set light to on
    def setLight(self):
        self.serialLED.write('h'.encode())
        #serialLED.close()

    # Set light to off
    def setLightOff(self):
        self.serialLED.write('l'.encode())
        #serialLED.close()

    # Set light to blink
    def setBlink(self, breakBit, blinkSpeed):
        for i in range(0,10):
            if (breakBit == 1):
                serialLED.write('l'.encode())
                break
            self.serialLED.write('l'.encode())
            time.sleep(1)
            self.serialLED.write('h'.encode())
            time.sleep(1)

    if __name__ == "__main__":
        print(__name__)
        pass

# Get temperature sensor readings
def getData():
    serialTemp = serial.Serial(arduino, 9600)
    serialTemp.timeout = 1
    temp = None
    while not temp:
        temp = serialTemp.readline().decode('ascii')
        print(temp)
    serialTemp.close()
    return temp