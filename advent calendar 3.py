from sense_hat import SenseHat # importing Sense Hat library
from time import sleep #Importing time library and method sleep
sense = SenseHat() # setting up sensehat
sense.low_light = True # setting the led light to low


r = (255,0,0) 
w = (255,255,255)
s = (255,255,0)

door3 = [
        w,w,w,s,s,w,w,w,
        w,s,s,s,s,s,s,w,
        w,w,s,s,s,s,w,w,
        w,w,w,s,s,w,w,w,
        w,w,w,s,s,w,w,w,
        w,w,s,s,s,s,s,w,
        w,s,s,s,s,s,w,w,
        w,w,w,s,s,w,w,w,
        ]
 
while True:
    sense.show_letter('3', back_colour = (255,0,0), text_colour=(0,0,255))
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels(door3)
            sleep(2)
            
        else:
            sense.show_message("Error")




        
    
