import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
p = GPIO.PWM(2, 100)
try:
    while(1):
        ds = int(input('duty cycle (%)...'))
        #p = GPIO.PWM(2, 100)
        p.start(ds)
        #input('Press to stop...')
        #p.stop()
    
finally:
    GPIO.cleanup()