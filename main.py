from PIL import Image
import numpy as np
import os

def createImage(text):
    pixels = [[(255, 0, 255), (0, 255, 0)],
              [(255, 255, 255), (0, 255, 0)],
              [(255, 0, 255), (0, 255, 0)]]

    array = np.array(pixels, dtype=np.uint8)

    image = Image.fromarray(array)
    image.save(text + ".png")


def main():
    text = input("Enter text to convert to subpixel image: ")
    imgname = text
    i = 1
    
    while os.path.isfile(imgname + ".png"):
        imgname = imgname + str(i)
        i += i

    
    createImage(imgname)

    
        


if __name__ == '__main__':
    main()
