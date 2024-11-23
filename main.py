from PIL import Image
import numpy as np
import os

class Letters:
    def __init__(self):
        self.letters = {"A" :
                 {"top" : [0, 1, 0],
                  "mto" : [1, 0, 1],
                  "mbo" : [1, 1, 1],
                  "bot" : [1, 0, 1]
                  }
        }

    def get(self, letter, pos):
        return self.letters[letter.upper()][pos]

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
        
def createImage(text, name):
    pixels = getLetters(text, 255)

    array = np.array(pixels, dtype=np.uint8)

    image = Image.fromarray(array)
    image.save(name + ".png")


def main():
    text = input("Enter text to convert to subpixel image: ")
    imgname = "img/" + text
    i = 1
    
    while os.path.isfile(imgname + ".png"):
        imgname = imgname + str(i)
        i += i

    createImage(text, imgname)
        


if __name__ == '__main__':
    main()
