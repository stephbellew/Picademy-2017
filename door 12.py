from sense_hat import SenseHat
from time import sleep
sense = SenseHat ()
sense.low_light=True

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
w = (255, 255, 255)
br = (165, 42, 42)
e = (0, 0, 0)
y = (255, 255, 0)
p = (255, 105, 180)

door12 =[
w, w, w, w, w, w, w, w, 
w, b, w, w, b, b, b, w,
w, b, w, w, w, w, b, w,
w, b, w, w, w, w, b, w,
w, b, w, w, w, b, w, w,
w, b, w, w, b, w, w, w,
w, b, w, w, b, b, b, w,
w, w, w, w, w, w, w, w,
]

rudolf = [   
y, w, w, w, w, w, w, y,
w, y, y, w, w, y, y, w,
y, y, w, br, br, w, y, y,
w, y, br, br, br, br, y, w,
w, br, br, br, br, br, br, w,
w, br, br, r, r, br, br, w,
w, br, br, r, r, br, br, w,
w, w, br, br, br, br, w, w,
]

sense.show_message("On the 12th day of xmas")
while True:
    sense.set_pixels(door12)
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels (rudolf)
            sleep (2)
        else:
            sense.show_message("Error")


