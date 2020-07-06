import serial
import time

arduino = '/dev/ttyACM0'
serialLED = serial.Serial(arduino, 9600, timeout=1)
# serialLED.timeout = 1

class Arduino():

    blink = 0

    def setBlink(self, blinkBit):
        blink = blinkBit

    # Set light to on
    def setLight(self):
        serialLED.write('h'.encode())
        #serialLED.close()

    # Set light to off
    def setLightOff(self):
        serialLED.write('l'.encode())
        #serialLED.close()

    # Set light to blink
    def setBlink(self, breakBit, blinkSpeed):
        for i in range(0,10):
            if (breakBit == 1):
                serialLED.write('l'.encode())
                break
            serialLED.write('l'.encode())
            time.sleep(1)
            serialLED.write('h'.encode())
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