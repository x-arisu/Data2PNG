import data2png as data
import png2data as png
from sys import argv

if argv[1] == "conv-data":
    print("converting to data...")
    data.main()
elif argv[1] == "conv-png":
    print("converting to image...")
    png.main()