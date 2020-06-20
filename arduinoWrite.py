import serial
import time

arduino = '/dev/ttyACM0'

# Set light to on
def setLight():    
    serialLED = serial.Serial(arduino, 9600)
    serialLED.timeout = 1
    while True:
        serialLED.write('h'.encode())
        time.sleep(0.5)
        print("Light on")
    serialLED.close()


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

    # while True:
    #     temp = serialTemp.readline().decode('ascii')
    #     print(temp)
    # serialTemp.close()

# Set light to off
def setLightOff():
    serialLED = serial.Serial(arduino, 9600)
    serialLED.timeout = 1
    serialLED.write('l'.encode())
    print("Light off")

#def readTemperature():


#def setBlinkSpeed(blinkSpeed):
    


    # while True:
    #     serialLED.write('l'.encode())
    #     time.sleep(0.5)
    #     print("Light off")
    # serialLED.close()

if __name__ == "__main__":
    print(__name__)
    pass