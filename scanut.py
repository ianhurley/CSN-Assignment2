from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r = (255,0,0)
g = (0,255,0)
y = (255,255,0)

b = (0,0,0)

smileAngry = [
  b,r,r,r,r,r,r,b,
  r,r,r,r,r,r,r,r,
  r,r,b,r,r,b,r,r,
  r,r,r,r,r,r,r,r,
  r,r,r,r,r,r,r,r,
  r,r,b,b,b,b,r,r,
  r,r,b,r,r,b,r,r,
  b,r,r,r,r,r,r,b
  ]

smileHappy = [
  b,g,g,g,g,g,g,b,
  g,g,g,g,g,g,g,g,
  g,g,b,g,g,b,g,g,
  g,g,g,g,g,g,g,g,
  g,b,g,g,g,g,b,g,
  g,g,b,b,b,b,g,g,
  g,g,g,g,g,g,g,g,
  b,g,g,g,g,g,g,b
  ]

smileSad = [
  b,y,y,y,y,y,y,b,
  y,y,y,y,y,y,y,y,
  y,y,b,y,y,b,y,y,
  y,y,y,y,y,y,y,y,
  y,y,y,y,y,y,y,y,
  y,b,b,b,b,b,b,y,
  y,y,y,y,y,y,y,y,
  b,y,y,y,y,y,y,b
  ]

def red():
  sense.set_pixels(smileAngry)

def green():
  sense.set_pixels(smileHappy)

def yellow():
  sense.set_pixels(smileSad)



sense.stick.direction_down = red 
sense.stick.direction_up = green 
sense.stick.direction_left = yellow 
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

while True:
  pass