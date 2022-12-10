import BlynkLib
from sense_hat import SenseHat
from time import sleep

import pymongo
from pymongo import MongoClient

# connecting to MongoDB Atlas cloud database
cluster = MongoClient("mongodb+srv://scanut:scanut@cluster0.x0cl6dg.mongodb.net/test")

db = cluster["ScaNutDB"]
collection = db["confectionary"]

BLYNK_AUTH = 'q1v6KTg1fFECJJ7mLuAaktu2z2SX5uPj'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#initialise SenseHAT
sense = SenseHat()
sense.clear()

#intro
sense.show_message("ScaNut")

#barcode scan function
def barcodeScan():

    hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

    hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }

    fp = open('/dev/hidraw0', 'rb')


    barcode = ""
    shift = False

    done = False

    while not done:

        ## Get the character from the HID
        buffer = fp.read(8)
        for c in buffer:
            if int(c) > 0:

                ##  40 is carriage return which signifies
                ##  we are done looking for characters
                if int(int(c)) == 40:
                    done = True
                    break;

                ##  If we are shifted then we have to 
                ##  use the hid2 characters.
                if shift: 

                    ## If it is a '2' then it is the shift key
                    if int(int(c)) == 2 :
                        shift = True

                    ## if not a 2 then lookup the mapping
                    else:
                        barcode += hid2[ int(int(c)) ]
                        shift = False

                ##  If we are not shifted then use
                ##  the hid characters

                else:

                    ## If it is a '2' then it is the shift key
                    if int(int(c)) == 2 :
                        shift = True

                    ## if not a 2 then lookup the mapping
                    else:
                        barcode += hid[ int(int(c)) ]
                
    print("Product: ", barcode)
    barcode = int(barcode) #convert string to int
    return barcode


#set sensehat led options

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

def scaNut():
    barcode = barcodeScan()
    result = "contains nuts"
    my_str = str(result)
    myquery = {"_id": (barcode),"Ingredients": {'$regex': 'nut'}}
    mydoc = collection.find(myquery)
    for ingredients in mydoc:
	    return result



def scanTrace():
    barcode = barcodeScan()
    result = "contains traces"
    my_str = str(result)
    myquery = {"_id": (barcode),"May contain": {'$regex': 'nut'}}
    mydoc = collection.find(myquery)
    for ingredients in mydoc:
	    return result


sense.clear()
while True:
    blynk.run()
    nut = scaNut()
    trace = scanTrace()
    if nut == "contains nuts":
        print("WARNING: Contains Nuts :(")
        sense.set_pixels(smileAngry)  
        blynk.virtual_write(0, 0) #green
        blynk.virtual_write(3, " ") #green
        blynk.virtual_write(2, 0) #yellow
        blynk.virtual_write(5, " ") #yellow
        blynk.virtual_write(1, 255) #red
        blynk.virtual_write(4, "Contains Nuts :(") #red
    elif trace == "contains traces":
        print("WARNING: Contains Traces :|")
        sense.set_pixels(smileSad)
        blynk.virtual_write(0, 0) #green
        blynk.virtual_write(3, " ") #green
        blynk.virtual_write(2, 255) #yellow
        blynk.virtual_write(5, "Contains Traces :|") #yellow
        blynk.virtual_write(1, 0) #red
        blynk.virtual_write(4, " ") #red
    else:
        print("Safe To Eat :)")
        sense.set_pixels(smileHappy)     # Up arrow
        blynk.virtual_write(0, 255) #green
        blynk.virtual_write(3, "Safe to Eat :)") #green
        blynk.virtual_write(2, 0) #yellow
        blynk.virtual_write(5, " ") #yellow
        blynk.virtual_write(1, 0) #red
        blynk.virtual_write(4, " ") #red
    sleep(0.5)
    sense.clear()