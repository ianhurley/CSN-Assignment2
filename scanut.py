import BlynkLib
from sense_hat import SenseHat
from time import sleep

BLYNK_AUTH = 'q1v6KTg1fFECJJ7mLuAaktu2z2SX5uPj'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#initialise SenseHAT
sense = SenseHat()
sense.clear()

#intro
sense.show_message("ScaNut") 

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

sense.clear()
while True:
    blynk.run()
    for event in sense.stick.get_events():
    # Check if the joystick was pressed
        if event.action == "pressed":
      
      # Check which direction
            if event.direction == "up":
                sense.set_pixels(smileHappy)     # Up arrow
                blynk.virtual_write(0, 255) #green
                blynk.virtual_write(2, 0) #yellow
                blynk.virtual_write(1, 0) #red
            elif event.direction == "down":
                sense.set_pixels(smileAngry)      # Down arrow
                blynk.virtual_write(0, 0) #green
                blynk.virtual_write(2, 0) #yellow
                blynk.virtual_write(1, 255) #red
            elif event.direction == "left": 
                sense.set_pixels(smileSad)      # Left arrow
                blynk.virtual_write(0, 0) #green
                blynk.virtual_write(2, 255) #yellow
                blynk.virtual_write(1, 0) #red
            elif event.direction == "right":
                sense.set_pixels(smileSad)      # Right arrow
            elif event.direction == "middle":
                sense.show_letter("M")      # Enter key
        
        # Wait a while and then clear the screen
            sleep(0.5)
            sense.clear()