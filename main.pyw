import subprocess
from tkinter import *

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
b3.place(relx=0.5, rely=0.4, anchor=CENTER)

def capture():
    win.destroy()
    subprocess.call(["python", "capture.py"])
b3 = Button(win, text='Capture', 
   width=20,command = lambda:capture())
b3.place(relx=0.5, rely=0.5, anchor=CENTER)
win.mainloop()