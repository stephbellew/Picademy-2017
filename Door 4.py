from sense_hat import SenseHat
from time import sleep
sense = SenseHat ()
sense.low_light=True

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
w = (255, 255, 255)


bauble = [
w, w, g, g, g, g, w, w,
w, r, r, r, r, r, r, w,
g, g, g, g, g, g, g, g,
b, b, b, b, b, b, b, b,
g, g, g, g, g, g, g, g,
r, r, r, r, r, r, r, r,
w, g, g, g, g, g, g, w,
w, w, g, g, g, g, w, w,
]
sense.show_message("On the 4th day of xmas")
while True:
    sense.show_letter("4", b, w)
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels (bauble)
            sleep (2)
        else:
            sense.show_message("Error")

                      

