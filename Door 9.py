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
o = (0, 0, 0)
c = (0, 0, 125)

number9 = [
    w, w, w, w, w, w, w, w,
    w, w, w, r, r, r, w, w,
    w, w, r, w, w, r, w, w,
    w, w, r, w, w, r, w, w,
    w, w, w, r, r, r, w, w,
    w, w, w, w, w, r, w, w,
    w, w, w, w, w, r, w, w,
    w, w, w, w, w, r, w, w,
    ]

door9 = [
    c, w, c, c, c, c, w, c,
    w, w, w, c, c, w, w, w,
    c, w, c, c, c, c, w, c,
    c, c, c, w, c, c, c, c,
    c, c, w, w, w, c, c, c,
    c, w, c, w, c, c, w, c,
    w, w, w, c, c, w, w, w,
    c, w, c, c, c, c, w, c,
    ]

door9a = [
    c, w, c, c, c, c, w, c,
    w, c, w, c, c, w, c, w,
    c, w, c, c, c, c, w, c,
    c, c, c, w, c, c, c, c,
    c, c, w, c, w, c, c, c,
    c, w, c, w, c, c, w, c,
    w, c, w, c, c, w, c, w,
    c, w, c, c, c, c, w, c,
    ]

sense.show_message("On the 9th day of Xmas")
while True:
    sense.set_pixels(number9)
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        if event.direction == "down":
            sense.set_pixels(door9)
            sleep(0.5)
            sense.set_pixels(door9a)
            sleep(0.5)
            sense.set_pixels(door9)
            sleep(0.5)
            sense.set_pixels(door9a)
            sleep(0.5)
            sense.set_pixels(door9)
            sleep(0.5)
            sense.set_pixels(door9a)
            sleep(0.5)
            sense.set_pixels(door9)
            sleep(0.5)
            sense.set_pixels(door9a)
            sleep(2)
            
        else:
            sense.show_message("Error")
