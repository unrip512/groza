import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]




def abc():
    
    for val in range(256):
        GPIO.output(dac, decimal2binary(val))
        time.sleep(0.005)
        if GPIO.input(comp) == False :
            return int(val)


try:
    while(1):
        p = abc()
        print("p = ", p)


    
    
finally:
     for i in dac:
        GPIO.output(i, 0)

