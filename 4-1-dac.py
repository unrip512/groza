import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try :
    print("Ведите целое число от 0 до 255 :  ")
    b = int(input())

    if( b > 0 and b <= 255) :
        a = int(b)

        val = decimal2binary(a)

        GPIO.output(dac, val)

        print("Предполагаемое значение:", 3.3 * a / 256)
        time.sleep(2)
        
    
except Exception: 
    print('ERROR')

finally: 
     for i in dac:
        GPIO.output(i, 0)
