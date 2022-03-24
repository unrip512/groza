import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac,GPIO.OUT)



def dec2bin(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try :

    print("Введите период ...")
    T = int(input())

    
    for i in range(256):
         val = dec2bin(i)
         GPIO.output(dac, val)
         time.sleep(T/512)
    for i in range(255, 1, -1):
         val = dec2bin(i)
         GPIO.output(dac, val)
         time.sleep(T/512)


finally: 
     for i in dac:
        GPIO.output(i, 0)