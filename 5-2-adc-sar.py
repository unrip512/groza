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

    val = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for l in range(8):

        val[l] = 1
        
        GPIO.output(dac, val)
        time.sleep(0.005)
        if GPIO.input(comp) == False :
            val[l] = 0

    number = val[0]*128+val[1]*64+val[2]*32+val[3]*16+val[4]*8+val[5]*4+val[6]*2+val[7]

    print(number)


try:
    while(1):
        p = abc()
        time.sleep(0.5)
   
finally:
     for i in dac:
        GPIO.output(i, 0)

