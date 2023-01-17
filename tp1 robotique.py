from pyb import Switch
from pyb import LED


led_R = LED(1)
led_G = LED(2)
led_B = LED(3)
# 1=red, 2=green, 3=blue

sw = pyb.Switch()

def cycle():
    counter = 0
    buttonState = ''
    buttonState = sw.value()
    print(buttonState)
    if buttonState == True:
        counter = counter + 1
        print(counter)

    elif counter == 0:
        led_R.off() 
        led_G.off() 
        led_B.off() 

    elif counter == 1:
        led_R.on() 
        led_G.off() 
        led_B.off()

    elif counter == 2:
        led_R.off() 
        led_G.on() 
        led_B.off() 

    elif counter == 3:
        led_R.off() 
        led_G.off() 
        led_B.on()

    else:
        counter = 0

sw.callback(cycle())