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

label =Label(win)


b1 = Button(win, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 

def upload_file():
    global img
    '''
    f_types = [('image Files', '*.jpg'),('image Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    '''
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
    Label(win, image=img1).place(x=750,y=100)
    Label(win, image=img2).place(x=1010,y=100)
    Label(win, image=img3).place(x=750,y=300)
    Label(win, image=img4).place(x=1010,y=300)
    label.after(5000, upload_file)
    
    
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
   cv2.imwrite('record/captured_image.jpg', frame)
   
   label.after(20, show_frames)


# run first time

show_frames()

# Create a Label Widget to display the text or Image

win.mainloop()