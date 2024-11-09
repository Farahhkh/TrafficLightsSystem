import time
from machine import Pin
from neopixel import NeoPixel
from nec import NEC_16, SAMSUNG
max_lum =100

rgb_led_num =   22
rgb_led_pin =   Pin(rgb_led_num, Pin.OUT)
rgb_led     =   NeoPixel(rgb_led_pin, 1) 



isPowerOn=1
rgb_led[0]=(0,255,0)
rgb_led.write()
def remoteSwitch(data, addr, ctrl):
    global isPowerOn
    
    if data > 0:     
        print('data {:02x}'.format(data)) 
        if data == 0xa2 and isPowerOn:
            rgb_led[0]=(0,0,0)
            rgb_led.write()
            isPowerOn=0
        elif data == 0xa2 and not isPowerOn:
            rgb_led[0]=(0,255,0)
            rgb_led.write()
            isPowerOn=1

        if isPowerOn:
               
            if data == 0x30 and rgb_led[0] == (0,255,0): 
                rgb_led[0]=(0,0,0)
                rgb_led.write()
                flash_yellow()
                rgb_led[0]=(255,0,0)
                rgb_led.write()
                
               
            if data == 0x18 and rgb_led[0] == (255,0,0):
                rgb_led[0]=(0,0,0)
                rgb_led.write()
                flash_yellow()
                rgb_led[0]=(0,255,0)
                rgb_led.write()


ir = NEC_16(Pin(15,Pin.IN),remoteSwitch)


def flash_yellow():
    for i in range(0,5):
        rgb_led[0]=(255,255,0)
        rgb_led.write()
        time.sleep_ms(500)
        rgb_led[0]=(0,0,0)
        rgb_led.write()
        time.sleep_ms(500)
