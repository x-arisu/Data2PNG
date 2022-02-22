#!/usr/bin/env python3
from PIL import Image

def imgToData(filePath, output):
    
    with open(output, 'wb') as out:
        
        #! open image and list its data
        img = Image.open(filePath)
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
