#!/usr/bin/env python3
import data2png as data
import png2data as png
from sys import argv

for arg in argv:
	if "--gui" == arg:
		try:
			import tkinter as tk
			import tkinter.font as tkfont
			from tkinter import filedialog as fd
			from tkinter import messagebox
		except:
			print("An exception occurred, is tkinter installed?")
			exit
		dataPath = ""
		imgPath = ""
		def getDataPath():
			global dataPath
			dataPath = fd.askopenfile()
		def saveDataIMG():
			global dataPath
			if dataPath == "":
				messagebox.showerror("Error", "Data file not selected!")
				return
			savePath = fd.asksaveasfilename(defaultextension=".png")
			data.dataToImg(dataPath.name, savePath)
			messagebox.showinfo("Done!", "Data has been converted to image.")
		def getIMGPath():
			global imgPath
			imgPath = fd.askopenfile()
		def saveIMGData():
			global imgPath
			if imgPath == "":
				messagebox.showerror("Error", "Image file not selected!")
				return
			savePath = fd.asksaveasfilename()
			png.imgToData(imgPath.name, savePath)
			messagebox.showinfo("Done!", "Image has been converted to data.")
		window = tk.Tk()
		window.title("Data2IMG GUI")
		window.geometry('200x200')
		window.resizable(width=False, height=False)
		window.rowconfigure(1, weight=1)
		window.rowconfigure(2, weight=1)
		window.rowconfigure(3, weight=1)
		window.rowconfigure(4, weight=1)
		window.columnconfigure(1,weight=1)
		window.columnconfigure(2,weight=1)
		font = tkfont.Font(family="mono", size=14)
		dataLabel = tk.Label(window)
		dataLabel["font"] = font
		dataLabel["fg"] = "#000000"
		dataLabel["text"] = "Data2IMG"
		dataLabel["justify"] = "left"
		dataLabel.grid(column=1, row=1)
		dataButton = tk.Button(text="Open File",command=getDataPath)
		dataButton.grid(column=2, row=1)
		dataConvertButton = tk.Button(text="Convert Data2IMG",command=saveDataIMG)
		dataConvertButton.grid(column=1, row=2)

		imgLabel = tk.Label(window)
		imgLabel["font"] = font
		imgLabel["fg"] = "#000000"
		imgLabel["text"] = "IMG2Data"
		imgLabel.grid(column=1, row=3)
		imgButton = tk.Button(text="Open File",command=getIMGPath)
		imgButton.grid(column=2, row=3)
		imgConvertButton = tk.Button(text="Convert IMG2Data",command=saveIMGData)
		imgConvertButton.grid(column=1, row=4)

		window.mainloop()

if len(argv) < 2:
	print("""Usage:
    app.py conv-data <Input File> <Output image name>
    app.py conv-png <Input image file> <Output data/txt file>
    app.py --gui Enables GUI
	    """)
	exit()

if argv[1] == "conv-data":
    print("converting from data to image...")
    data.dataToImg(argv[2], argv[3])
elif argv[1] == "conv-png":
    print("converting from image to data...")
    png.imgToData(argv[2], argv[3])
