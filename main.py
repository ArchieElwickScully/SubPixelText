from PIL import Image
import numpy as np
import os

class Letters:
    def __init__(self):
        self.letters = {"A" :
                            {"top" : [0, 1, 0],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 1],
                             "bot" : [1, 0, 1]},
                        "B" :
                            {"top" : [1, 0, 0],
                             "mto" : [1, 1, 0],
                             "mbo" : [1, 0, 1],
                             "bot" : [1, 1, 1]},
                        "C" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 0, 0],
                             "mbo" : [1, 0, 0],
                             "bot" : [1, 1, 1]},
                        "D" :
                            {"top" : [0, 1, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 0, 1],
                             "bot" : [0, 1, 1]},
                        "E" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 1, 1],
                             "mbo" : [1, 0, 0],
                             "bot" : [1, 1, 1]},
                        "F" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 0, 0],
                             "mbo" : [1, 1, 1],
                             "bot" : [1, 0, 0]},
                        "G" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 1, 1],
                             "mbo" : [0, 0, 1],
                             "bot" : [1, 1, 1]},
                        "H" :
                            {"top" : [1, 0, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 1],
                             "bot" : [1, 0, 1]},
                        "I" :
                            {"top" : [1, 1, 1],
                             "mto" : [0, 1, 0],
                             "mbo" : [0, 1, 0],
                             "bot" : [1, 1, 1]},
                        "J" :
                            {"top" : [1, 1, 1],
                             "mto" : [0, 1, 0],
                             "mbo" : [0, 1, 0],
                             "bot" : [1, 1, 0]},
                        "K" :
                            {"top" : [1, 1, 0],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 0],
                             "bot" : [1, 0, 1]},
                        "L" :
                            {"top" : [1, 0, 0],
                             "mto" : [1, 0, 0],
                             "mbo" : [1, 0, 0],
                             "bot" : [1, 1, 1]},
                        "M" :
                            {"top" : [1, 0, 1],
                             "mto" : [1, 1, 1],
                             "mbo" : [1, 0, 1],
                             "bot" : [1, 0, 1]},
                        "N" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 0, 1],
                             "bot" : [1, 0, 1]},
                        "O" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 0, 1],
                             "bot" : [1, 1, 1]},
                        "P" :
                            {"top" : [1, 1, 0],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 0],
                             "bot" : [1, 0, 0]},
                        "Q" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 1],
                             "bot" : [0, 0, 1]},
                        "R" :
                            {"top" : [1, 1, 0],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 0],
                             "bot" : [1, 0, 1]},
                        "S" :
                            {"top" : [1, 1, 1],
                             "mto" : [1, 0, 0],
                             "mbo" : [0, 1, 1],
                             "bot" : [1, 1, 1]},
                        "T" :
                            {"top" : [1, 1, 1],
                             "mto" : [0, 1, 0],
                             "mbo" : [0, 0, 0],
                             "bot" : [0, 1, 0]},
                        "U" :
                            {"top" : [1, 0, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 0, 1],
                             "bot" : [1, 1, 1]},
                        "V" :
                            {"top" : [1, 0, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 0, 1],
                             "bot" : [0, 1, 0]},
                        "W" :
                            {"top" : [1, 0, 1],
                             "mto" : [1, 0, 1],
                             "mbo" : [1, 1, 1],
                             "bot" : [1, 0, 1]},
                        "X" :
                            {"top" : [1, 0, 1],
                             "mto" : [0, 1, 0],
                             "mbo" : [0, 1, 0],
                             "bot" : [1, 0, 1]},
                        "Y" :
                            {"top" : [1, 0, 1],
                             "mto" : [1, 1, 1],
                             "mbo" : [0, 0, 1],
                             "bot" : [1, 1, 1]},
                        "Z" :
                            {"top" : [1, 1, 1],
                             "mto" : [0, 0, 1],
                             "mbo" : [1, 1, 0],
                             "bot" : [1, 1, 1]},
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
