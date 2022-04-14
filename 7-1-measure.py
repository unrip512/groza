import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
comp = 4
troyka = 17

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setup(troyka, GPIO.OUT, )
GPIO.setup(comp, GPIO.IN)

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
    return number


try: 
    GPIO.output(troyka, 1)
    t = 0
    a = 0
    list = [0]
    
    with open("/home/b01-109/data.txt", "w") as outfile:
        while(a == 0) :
            p = abc()
            if p >= 250:
                a = 1
            time.sleep(0.25)
            t = t + 1 
            outfile.write(str(p))
            outfile.write('\n')

        GPIO.output(troyka, 0)

        while(a == 1) :
            p = abc()
            if p <= 5:
                a = 0
            time.sleep(0.25)
            t = t + 1
            outfile.write(str(p))
            outfile.write('\n')

        

    with open("/home/b01-109/data.txt", "r") as outfile:
        for line in outfile:
            list.append(int(line))

    plt.plot(list)
    plt.show()

    

finally:
     for i in dac:
        GPIO.output(i, 0)

    

    
append

