'''
Debounce a switch using interrupts.

Creates an interrupt handler that's called when the switch pin changes state (i.e., rising or falling edge trigger).
If a debounce cycle has not already been started, the handler creates a one-shot timer. While this timer is running,
any additional interrupts are ignored. After the timer expires, the desired action is taken (i.e., the sw_callback function
is called), and the debounce cycle is cleared so it can begin again.

https://docs.micropython.org/en/latest/library/machine.Pin.html?highlight=pin#machine.Pin
https://docs.micropython.org/en/latest/library/machine.Timer.html
'''

from machine import Pin, Timer

sw_pin = 15
switch = Pin(sw_pin, Pin.IN, Pin.PULL_UP)

debounce_delay = 50   # ms 
debounce_started = False
debounce_timer = Timer()

led_builtin_pin = 25  # RPi Pico built-in LED
led = Pin(led_builtin_pin, Pin.OUT)
led.value(not switch.value()); # set initial value

       
def debounce_clear(timer): 
    global debounce_started, switch
    debounce_started = False
    # take some action ...
    sw_callback(switch)
        
def sw_event(pin):
    global sw_pin, debounce_started, debounce_timer, debounce_delay, led
    if(debounce_started):
        return
    else:
        debounce_started = True
        debounce_timer.init(mode=Timer.ONE_SHOT, period=debounce_delay, callback=debounce_clear)

def sw_callback(pin):
    led.value(not pin.value()) 
    print( 'Pin %d: prev %s,\tcurr %s' % (sw_pin, bool(not pin.value()), bool(pin.value())) )
 
 
# display initial switch state
print( 'Pin %d: initial state %s' % (sw_pin, bool(switch.value())) )

switch.irq(handler=sw_event, trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING)

# loop
while True:
    pass