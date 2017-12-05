from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.low_light=True
sense.clear()

g = (0, 255, 0) #green
w = (255, 255, 255) # white
r = (255, 0, 0) # red


sense.show_letter("2", g,w,)
sleep(2)

cane = [
      r,r,r,r,r,r,r,r,
      r,r,g,w,g,r,r,r,
      r,r,w,r,w,r,r,r,
      r,r,r,r,g,r,r,r,
      r,r,r,r,w,r,r,r,
      r,r,r,r,g,r,r,r,
      r,r,r,r,w,r,r,r,
      r,r,r,r,g,r,r,r,
]

while True:
    sense.show_letter("2", g,w,)
    event = sense.stick.wait_for_event()
    if event.action =="pressed":
        if event.direction == "down":
            sense.set_pixels(cane)
            sleep(2)
        else:
            sense.show_message("Error")


