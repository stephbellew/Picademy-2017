from sense_hat import SenseHat # importing Sense Hat library
from time import sleep #Importing time library and method sleep
sense = SenseHat() # setting up sensehat
sense.low_light = True # setting the led light to low


r = (255,0,0) 
w = (255,255,255)
g = (0,255,0)

door11 = [
        w,w,r,w,w,w,r,w,
        w,r,r,w,w,r,r,w,
        w,w,r,w,w,w,r,w,
        w,w,r,w,w,w,r,w,
        w,w,r,w,w,w,r,w,
        w,w,r,w,w,w,r,w,
        w,w,r,w,w,w,r,w,
        w,r,r,r,w,r,r,r,
        ]

pic11 = [
        g,g,w,w,w,w,g,g,
        g,g,w,w,w,w,g,g,
        g,g,r,r,r,r,g,g,
        g,g,r,r,r,r,g,g,
        g,g,r,r,r,r,g,g,
        r,r,r,r,r,r,g,g,
        r,r,r,r,r,r,g,g,
        r,r,r,r,r,r,g,g,
        
        ]

sense.show_message("On the 11th day of xmas")
while True:
    sense.set_pixels(door11)
    #sense.show_letter('7', back_colour = (255,0,0), text_colour=(0,0,255))
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels(pic11)
            sleep(4)
            
        else:
            sense.show_message("Error")




        
    
