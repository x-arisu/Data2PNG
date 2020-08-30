#!/usr/bin/env python3
from PIL import Image
from sys import argv
def main():
  outputFile = "out.data"
  if (len(argv) > 2):
    outputFile = argv[2]
  out = open(outputFile, 'wb')
  img = Image.open(argv[1])
  pixels = list(img.getdata())
  data = []
  print("Collecting data...")
  for i in range(len(pixels)):
    for x in range(3):
      data.append(pixels[i][x])
  print("Data collected! Cleaning...")
  dataFlag = False
  endDataIndex = len(data) - 1
  while(not dataFlag):
    if (data[endDataIndex] == 0):
      del data[endDataIndex]
      endDataIndex -= 1
    else:
      dataFlag = True
  out.write(bytes(data))
  out.close()
if __name__ == '__main__':
  main()
