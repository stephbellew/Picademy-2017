from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = (255, 0, 0)
w = (255, 255, 255)
g = (0, 255, 0)
b = (102, 51, 0)
p = (255, 0, 191)
y = (255, 191, 0)
m = (128, 0, 255)
t = (0, 255, 255)

number1 = [
    w, w, w, r, r, w, w, w,
    w, w, r, r, r, w, w, w,
    w, w, r, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, r, r, r, r, w, w,
    ]


door1 = [
    w, w, w, y, y, w, w, w,
    w, w, w, g, g, w, w, w,
    w, w, w, p, g, w, w, w,
    w, w, g, g, t, g, w, w,
    w, w, g, m, g, g, w, w,
    w, g, t, g, g, p, g, w,
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, w, w, w,
    ]
sense.show_message("On the 1st day of Xmas")
while True:
    sense.set_pixels(number1)
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels(door1)
            sleep(2)
        else:
            sense.show_message("Error")


    
