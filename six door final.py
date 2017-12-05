from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.low_light=True
sense.clear()

g = (0, 255, 0) #green
w = (255, 255, 255) # white
r = (255, 0, 0) # red
y = (255, 255, 0) # yellow

sense.show_letter("6", g,w,)
sleep(2)

random = [
      r,r,r,g,g,r,r,r,
      r,r,r,g,g,r,r,r,
      r,r,r,g,g,r,r,r,
      g,g,g,g,g,g,g,g,
      g,g,g,g,g,g,g,g,
      r,r,r,g,g,r,r,r,
      r,r,r,g,g,r,r,r,
      r,r,r,g,g,r,r,r,
]

while True:
    sense.show_letter("6", g,w,)
    event = sense.stick.wait_for_event()
    if event.action =="pressed":
        if event.direction == "down":
            sense.set_pixels(random)
            sleep(2)
        else:
            sense.show_message("Error")

