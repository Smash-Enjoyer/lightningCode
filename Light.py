import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.2)

colors = [[0,0,255],[255,0,0],[255,255,255]]
speed = 0.01
times = 50
i = 0
color = [0,0,255]
fOrange1 = (255,54,0)
fOrange2 = (255,74,0)
fOrange3 = (255,34,0)
red = (255,0,0)
black = (0,0,0)
purple = (250,0,250)
fColors = [fOrange1,fOrange2,fOrange3,red,black]
lightningColor = [[255,255,255],[0,255,0]]

def lightning(color,lColors, speed = 0.1):
    delay = random.random()*5 + 0.5
    np.fill(color)
    np.show()
    time.sleep(delay)
    ind = random.randint(0, len(lColors)-1)
    for i in range(10):
        np.fill(lColors[ind])
        np.show()
        time.sleep(0.1)
        np.fill([0,0,0])
        np.show()
    np.fill(color)
    np.show()


np.fill(red)
while True:
    lightning(purple,lightningColor)
