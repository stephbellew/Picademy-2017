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
o = (255, 165, 0)
c = (0, 0, 125)

number5 = [
    w, w, w, w, w, w, w, w,
    w, w, r, r, r, r, w, w,
    w, w, r, w, w, w, w, w,
    w, w, r, r, r, r, w, w,
    w, w, w, w, w, r, w, w,
    w, w, w, w, w, r, w, w,
    w, w, r, r, r, r, w, w,
    w, w, w, w, w, w, w, w,
    ]


door5 = [
    y, y, y, b, b, y, y, y,
    y, y, y, b, b, y, y, y,
    y, y, b, b, b, b, y, y,
    y, y, w, w, w, w, y, y,
    y, w, w, c, c, w, w, y,
    y, w, w, w, w, w, w, y,
    y, w, r, r, r, r, w, y,
    y, y, w, w, w, w, y, y,
    ]
sense.show_message("On the 5th day of Xmas")
while True:
    sense.set_pixels(number5)
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels(door5)
            sleep(2)
        else:
            sense.show_message("Error")
