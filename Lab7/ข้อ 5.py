import RPi.GPIO as GPIO
import time
import drivers
from time import sleep

display = drivers.Lcd()
display.lcd_clear()

SW1  = 27  
SW2  = 17

lcd_position = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
labSide = [\
'LAB7           ',\
' LAB7          ',\
'  LAB7         ',\
'   LAB7        ',\
'     LAB7      ',\
'      LAB7     ',\
'       LAB7    ',\
'        LAB7   ',\
'         LAB7  ',\
'          LAB7 ',\
'           LAB7 ',\
'            LAB7 ']
try:
    while True:
	
        if GPIO.event_detected(SW1):
            print("Writing to LCD !!!")
            lcd_position += 1
            if lcd_position >= 12:
                lcd_position = 11
            print(f"SW1 Pressed : {lcd_position}")
            display.lcd_display_string(labSide[lcd_position], 1)
        elif GPIO.event_detected(SW2):
            print("Writing to LCD !!!")
            lcd_position -= 1
            if lcd_position <= 0:
                lcd_position = 0
            print(f"SW1 Pressed : {lcd_position}")
            display.lcd_display_string(labSide[lcd_position], 1)
            

except KeyboardInterrupt:

    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    GPIO.cleanup()

    print("\nBye...")
