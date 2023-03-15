import cv2
class VideoCamera (object):
    

        # Create a VideoCapture object to capture images from the default camera
        
   

        
        # Create a window to show real-time video capture

        # Create a variable to keep track of whether the user wants to record an image or not
    def get_frame(self):
        self.cap = cv2.VideoCapture(0)
        ret, frame =self.cap.read()
        ret, jpeg = cv2.imencode('.jpg',frame)
        # Loop through frames from the video capture
        return jpeg.tobytes()

        # Release the VideoCapture object and destroy all windows
        
