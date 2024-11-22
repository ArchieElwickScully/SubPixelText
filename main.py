from PIL import Image
import os


def main():
    text = input("Enter text to convert to subpixel image: ")
    imgname = text
    i = 1
    
    while os.path.isfile(imgname + ".png"):
        imgname = imgname + str(i)
        i += i

    with open(imgname + ".png", "w") as f:
        print("file created, writing to file")

    
    


if __name__ == '__main__':
    main()
