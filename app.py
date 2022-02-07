from concurrent.futures import wait
from sys import argv
import tkinter as tk
from PIL import Image
import tkinter
import time
# if argv[1] == "conv-data":
#     print("converting to data...")
#     data.main()
# elif argv[1] == "conv-png":
#     print("converting to image...")
#     png.main()

root = tkinter.Tk()
root.title('image convert')

entry = tkinter.Entry(root)
entry.pack()

def p(n):
    global img
    img = n
    main(img)
    print("converting...")
    time.sleep(2)
    print("done!")


button = tkinter.Button(root, text="convert to data",command = lambda: p(entry.get()))
button.pack()

entry2 = tkinter.Entry(root)
entry2.pack()

def p2(n2):
    global Idata
    Idata = n2
    main2(Idata)
    print("converting...")

    

button2 = tkinter.Button(root, text="convert to image", command = lambda: p2(entry2.get()))
button2.pack()

def main(img):
    
    output = "out.txt"
    
    with open(output, 'wb') as out:
        
        #! open image and list its data
        img = Image.open(img)
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

def main2(Idata):
  outputFile = "out.png"
  rawData = open(Idata, "rb")
  data = rawData.read()
  rawData.close()
  pixelList = []
  tempData = []
  print("Creating pixels...")

  for i in data:
    if (len(tempData) == 3):
      pixelList.append((tempData[0],tempData[1],tempData[2]))
      tempData = []
    tempData.append(i)
  if (len(tempData) > 0):
    for i in range(3 - len(tempData)):
      tempData.append(0)
    pixelList.append((tempData[0],tempData[1],tempData[2]))
  #gets closest whole number that makes a perfect square
  imgRes = int(-(-len(pixelList)**.5//1))
  print("Writing image...")
  img = Image.new('RGB', (imgRes, imgRes))
  img.putdata(pixelList)
  img.save(outputFile)

root.mainloop()