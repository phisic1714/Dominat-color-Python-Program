import subprocess
from tkinter import *
from PIL import Image, ImageTk
import cv2
import function.color_detect as color_detect

# Create an instance of TKinter Window or frame
win= Tk()

# Set the size of the window
width= win.winfo_screenwidth()
height= win.winfo_screenheight()
#setting tkinter window size
win.geometry("%dx%d" % (width, height))
win.option_add('*Font', 'times 30')
win.title('Dominant Color image Program (โปรแกรมระบุสีที่มีในภาพ)')

label =Label(win)
def realtime():
    win.destroy()
    subprocess.call(["python", "realtime.py"])
b3 = Button(win, text='Realtime', 
   width=20,command = lambda:realtime())
b3.grid(row=4,column=1)

def capture():
    win.destroy()
    subprocess.call(["python", "capture.py"])
b3 = Button(win, text='Capture', 
   width=20,command = lambda:capture())
b3.grid(row=5,column=1)
win.mainloop()