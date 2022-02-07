#!/usr/bin/env python3
from PIL import Image
from sys import argv

def main():
    
    output = argv[3] if (len(argv) > 3) else "out.txt"
    
    with open(output, 'wb') as out:
        
        #! open image and list its data
        img = Image.open(argv[2])
        pixels = list(img.getdata())
        
        print("Collecting data...")
        
        #! iterate through each color channel in each pixel and append its value to a list
        #! only use RGB not RGBA
        data = [x for pixel in pixels for x in pixel[:3]]
        
        print("Data collected! Cleaning...")
        
        #! this will remove trailing 0's from the data
        #* example: data = [1, 2, 3, 4, 0, 0]
        #*          data = [1, 2, 3, 4]
        while data[-1] == 0:
            del data[-1]
        
        out.write(bytes(data))

if __name__ == '__main__':
    main()
