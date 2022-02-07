#!/usr/bin/env python3
import data2png as data
import png2data as png
from sys import argv

if len(argv) < 2:
	print("""Usage:
    app.py conv-data <Input File> <Output image name>
    app.py conv-png <Input image file> <Output data/txt file>
	    """)
	exit()

if argv[1] == "conv-data":
    print("converting to data to image...")
    data.main()
elif argv[1] == "conv-png":
    print("converting to image to data...")
    png.main()
