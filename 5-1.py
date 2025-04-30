import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]

def adc():
    for i in range(256):
        list = decimal2binary(i)
        for k in range(len(list)):
            GPIO.output(dac[k], list[k])
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if(compValue == 1):
            return i
    return 255


try:
    while(True):
        level = adc()
        voltage = (level/256)*3.3
        print(f"числовое значение: {level}, напряжение: {voltage:.2f}V")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()