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

pudding = [
e, g, g, e, e, g, g, e,
e, e, g, r, r, g, e, e,
e, e, w, w, w, w, e, e,
e, w, br, br, br, br, w, e,
br,br, br, br, br, br, br, br,
br, br, br, br, br, br, br, br,
e, br, br, br, br, br, br, e,
e, e, br, br, br, br, e, e,
]


sense.show_message("On the 8th day of xmas")
while True:
    sense.show_letter("8", b, w)
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels (pudding)
            sleep (2)
        else:
            sense.show_message("Error")
