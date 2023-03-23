# Import required Libraries
import subprocess
from tkinter import *
from PIL import Image, ImageTk
import cv2
import function.realtime_dominant_color as dominant_realtime
import numpy as np


# Create an instance of TKinter Window or frame
win= Tk()

# Set the size of the window
width= win.winfo_screenwidth()
height= win.winfo_screenheight()
#setting tkinter window size
win.geometry("%dx%d" % (width, height))
win.option_add('*Font', 'times 30')
win.title('Dominant Color image Program (โปรแกรมระบุสีที่มีในภาพ)')
win.configure(bg='#616161')


label =Label(win)
def back():
 cap.release() 
 win.quit()
 win.destroy()
 subprocess.call(["python", "main.pyw"])
b2 = Button(win, text='Back',
 width=20,command = lambda:back())
b2.grid(row=3,column=1)
   
cap= cv2.VideoCapture(0)
n_clusters = 5
def show_frames():
   label.place(relx=0.5, rely=0.5, anchor=CENTER)
   out=dominant_realtime.dominant_color(cap)
   cv2image= cv2.cvtColor(out,cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)



show_frames()


win.mainloop()