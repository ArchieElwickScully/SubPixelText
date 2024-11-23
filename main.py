from letters import *
from PIL import Image
import numpy as np
import os

def getLetters(text, brightness):
    letters = Letters()
    
    positions = ["top", "mto", "mbo", "bot"]
    
    pixels = []
    currentRow = []
    currentPixel = ()

    for pos in positions:
        for l in text:
            for subpixel in letters.get(l, pos):
                if subpixel:
                    currentPixel += (brightness,)
                else:
                    currentPixel += (0,)

            currentRow.append(currentPixel)
            currentPixel = ()
                            
        pixels.append(currentRow)
        currentRow = []

    return pixels        
        
def createImage(text, brightness, name):
    pixels = getLetters(text, brightness)

    array = np.array(pixels, dtype=np.uint8)

    image = Image.fromarray(array)
    image.save(name + ".png")


def main():
    text = input("Enter text to convert to subpixel image: ")
    brightness = int(input("Enter pixel brightness[1-255]: "))
    
    imgname = "img/" + text
    i = 1
    
    while os.path.isfile(imgname + ".png"):
        imgname = imgname + str(i)
        i += i

    createImage(text, brightness, imgname)

    print("Subpixel text created! Find it at", imgname + ".png")



if __name__ == '__main__':
    main()
