from machine import Pin, ADC
import time


axx = ADC(Pin(27))
axy = ADC(Pin(26))


button = Pin(16,Pin.IN, Pin.PULL_UP)
while True:
    x_value = axx.read_u16()
    y_value = axy.read_u16()
    button_value= button.value()
    print(str(x_value) +", " + str(y_value) + " -- " + str(button_value))
    time.sleep(0.1)

    