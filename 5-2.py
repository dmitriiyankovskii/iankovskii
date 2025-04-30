import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]

def adc():
    num = 128
    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)

    if(GPIO.input(comp) == 1):
        num-=128
        num+=64
    else:
        num+= 64
    
    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)
    
    if(GPIO.input(comp) == 1):
        num-=64
        num+=32
    else:
        num+= 32
    
    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)

    if(GPIO.input(comp) == 1):
        num-=32
        num+=16
    else:
        num+= 16
        
    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)

    if(GPIO.input(comp) == 1):
        num-=16
        num+=8
    else:
        num+= 8
    
    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)

    if(GPIO.input(comp) == 1):
        num-=8
        num+=4
    else:
        num+= 4

    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)

    if(GPIO.input(comp) == 1):
        num-=4
        num+=2
    else:
        num+= 2
    
    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)
        
    if(GPIO.input(comp) == 1):
        num-=2
        num+=1
    else:
        num+= 1

    GPIO.output(dac, decimal2binary(num))
    time.sleep(0.001)

    if(GPIO.input(comp) == 1):
        num-=1
    else:
        num+= 0
    
    GPIO.output(dac, decimal2binary(num))
    
    
    return num
try:
    while(True):
        num = adc()
        voltage = (num/256)*3.3
        print(f"числовое значение: {num}, напряжение: {voltage:.2f}V")
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()