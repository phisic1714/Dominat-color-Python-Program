# Import required Libraries
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from random import randint
import color_detect

# Create an instance of TKinter Window or frame
win= Tk()

# Set the size of the window
win.geometry('1080x610')
label =Label(win)
win.option_add('*Font', 'times 30')


b1 = Button(win, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 

def upload_file():
    global img
    '''
    f_types = [('image Files', '*.jpg'),('image Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    '''
    ret, frame = cap.read()
    
    
    
    color_detect.dominant_color()
    img = ImageTk.PhotoImage(file='captured_image.jpg')
    img1 = ImageTk.PhotoImage(file='my_plot.png')
    img2 = ImageTk.PhotoImage(file='output.png')
    Label(win, image=img).place(x=50,y=200)
    Label(win, image=img1).place(x=50,y=250)
    Label(win, image=img2).place(x=50,y=300)
    label['text'] = 5
    win.after(5000, upload_file)
    
    
cap= cv2.VideoCapture(0)

# Loop through frames from the video capture

def show_frames():
   label.place(x=50,y=100)
   # Get the latest frame and convert into Image
   ret, frame = cap.read()
   cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   cv2.imwrite('captured_image.jpg', frame)
   
   label.after(20, show_frames)


# run first time

show_frames()


# Create a Label Widget to display the text or Image

win.mainloop()