# uPy_Debounce_Switch

### Debounce a switch using interrupts.


Creates an __interrupt handler__ that's called when the switch pin changes state (i.e., __rising or falling edge trigger__). If a debounce cycle has not already been started, the handler creates a __one-shot  timer__, and then takes some action. While this timer is running, any additional interrupts are ignored. After the timer expires, the debounce cycle is cleared so it can begin again.

```
switch.irq(handler=sw_event, trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING)

debounce_timer.init(mode=Timer.ONE_SHOT, period=debounce_delay, callback=debounce_clear)
 ```
 

#### Resources:

https://docs.micropython.org/en/latest/library/machine.Pin.html?highlight=pin#machine.Pin

https://docs.micropython.org/en/latest/library/machine.Timer.html


<br>

<img src = "./images for README/Raspberry Pi Pico pinout better.png" width = "800"/>

<br>

https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html

<br>

### Digital Inputs: Pullup vs. Pulldown Resistors

<img src = "./images for README/NO switch.png" width = "600"/> 

<img src = "./images for README/NC switch.png" width = "600"/> 

