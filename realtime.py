# Import required Libraries
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
win.configure(bg='#616161')

label =Label(win)
b1 = Button(win, text='Start', 
   width=20,command = lambda:start())
b1.grid(row=2,column=1) 

label =Label(win)
def back():
 win.destroy()
 subprocess.call(["python", "main.py"])
b2 = Button(win, text='Back',
 width=20,command = lambda:back())
b2.grid(row=3,column=1)

def start():
    global img1,img2,img3,img4
    pixels_x=280
    pixels_y=210
    ret, frame = cap.read()
    
    color_detect.dominant_color('record/captured_image.jpg')
    img1=Image.open('record/captured_image.jpg')
    img2=Image.open('record/output.png')
    img3=Image.open('record/my_plot1.png')
    img4=Image.open('record/my_plot.png')
    img1 = ImageTk.PhotoImage(img1.resize((pixels_x, pixels_y)))
    img2 = ImageTk.PhotoImage(img2.resize((pixels_x, pixels_y)))
    img3 = ImageTk.PhotoImage(img3.resize((pixels_x, pixels_y)))
    img4 = ImageTk.PhotoImage(img4.resize((pixels_x, pixels_y)))
    Label(win, image=img1).place(x=750,y=250)
    Label(win, image=img2).place(x=1010,y=250)
    Label(win, image=img3).place(x=750,y=450)
    Label(win, image=img4).place(x=1010,y=450)
    label.after(5000, start)
    
    
cap= cv2.VideoCapture(0)
def show_frames():
   label.place(x=50,y=250)
   # Get the latest frame and convert into Image
   ret, frame = cap.read()
   cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   cv2.imwrite('record/captured_image.jpg', frame)
   label.after(20, show_frames)


# run first time

show_frames()

# Create a Label Widget to display the text or Image

win.mainloop()