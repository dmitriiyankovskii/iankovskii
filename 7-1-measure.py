import RPi.GPIO as GPIO
import time
import math
import matplotlib.pyplot as plt
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
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

def show_leds(num):
    list = [0, 0, 0, 0, 0, 0, 0, 0]
    n = math.trunc((num/256)*8)
    for i in range(n):
        list[i] = 1
    GPIO.output(leds, list)

try:
    measure_data = []
    t1 = time.time()
    GPIO.output(troyka, GPIO.HIGH)
    num = 0
    while(num<=200):
        num = adc()
        show_leds(num)
        measure_data.append(num)
        
        
    GPIO.output(troyka, GPIO.LOW)  
    while(adc()>=193):
        num = adc()
        show_leds(num)
        measure_data.append(num)
        
    t2 = time.time()
    duration = t2 - t1
    T = duration/len(measure_data)
    q = 1/T
    qs = 3.3/256
    print("Частота: ", q)
    print("шаг квантования: ", qs)
    print("время измерений: ", duration)   

    measure_data_str = [str(item) for item in measure_data]
    with open("data.txt", "w") as f:
        f.write("\n".join(measure_data_str))    
    plt.plot(data.txt) 
    plt.show()
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()