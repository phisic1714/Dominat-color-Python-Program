# Import required Libraries
import subprocess
from tkinter import *
from tkinter import filedialog
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
win.configure(bg='#616161')

win.option_add('*Font', 'times 30')
win.title('Dominant Color image Program (โปรแกรมระบุสีที่มีในภาพ)')

label =Label(win)




def upload_file():
    global img,img1,img2,img3
    f_types = [('image Files', '*.jpg'),('image Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    pixels_x=280
    pixels_y=210
    img_resized=Image.open(filename).resize((pixels_x, pixels_y))
    color_detect.dominant_color(filename)
    img1=Image.open('record/output.png')
    img2=Image.open('record/my_plot.png')
    img3=Image.open('record/my_plot1.png')
    img = ImageTk.PhotoImage(img_resized)
    img1 = ImageTk.PhotoImage(img1.resize((pixels_x, pixels_y)))
    img2 = ImageTk.PhotoImage(img2.resize((pixels_x, pixels_y)))
    img3 = ImageTk.PhotoImage(img3.resize((pixels_x, pixels_y)))
    imgf=Label(win, image=img)
    imgf.place(x=750,y=100)
    img1f=Label(win, image=img1)
    img1f.place(x=1010,y=100)
    img2f=Label(win, image=img2)
    img2f.place(x=1010,y=300)
    img3f=Label(win, image=img3)
    img3f.place(x=750,y=300)
b1 = Button(win, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1)     
    



def rec():
    global img1,img2,img3,img4
    pixels_x=280
    pixels_y=210
    ret, frame = cap.read()
    cv2.imwrite('record/captured_image.jpg', frame)
    color_detect.dominant_color('record/captured_image.jpg')
    img1=Image.open('record/captured_image.jpg')
    img2=Image.open('record/output.png')
    img3=Image.open('record/my_plot1.png')
    img4=Image.open('record/my_plot.png')
    img1 = ImageTk.PhotoImage(img1.resize((pixels_x, pixels_y)))
    img2 = ImageTk.PhotoImage(img2.resize((pixels_x, pixels_y)))
    img3 = ImageTk.PhotoImage(img3.resize((pixels_x, pixels_y)))
    img4 = ImageTk.PhotoImage(img4.resize((pixels_x, pixels_y)))
    imgf=Label(win, image=img1)
    imgf.place(x=750,y=100)
    img1f=Label(win, image=img2)
    img1f.place(x=1010,y=100)
    img2f=Label(win, image=img3)
    img2f.place(x=750,y=300)
    img3f=Label(win, image=img4)
    img3f.place(x=1010,y=300)
b3 = Button(win, text='Capture', 
   width=20,command = lambda:rec())
b3.grid(row=4,column=1)

cap= cv2.VideoCapture(0)
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
   label.after(20, show_frames)
show_frames()
win.mainloop()