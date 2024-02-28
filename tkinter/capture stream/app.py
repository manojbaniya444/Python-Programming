import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os

class WebCamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam app")

        # Replace the following line with the RTSP URL of your stream
        rtsp_url = 'rtsp://192.168.1.69:8080/h264_ulaw.sdp'
        self.video = cv2.VideoCapture(rtsp_url)

        self.current_image = None

        self.frame_skip = 2
        self.frame_counter = 0
        
        self.canvas = tk.Canvas(window, width=640, height=640)
        self.canvas.pack()

        self.download_button = tk.Button(window, text="Capture", command=self.download_image)
        self.download_button.pack()

        self.update_webcam()

    def update_webcam(self):
        ret, frame = self.video.read()
        frame = cv2.resize(frame, (640, 640))

        if ret:
            self.frame_counter += 1
            if self.frame_counter % self.frame_skip == 0:
                self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                self.photo = ImageTk.PhotoImage(image=self.current_image)

                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            self.window.after(1, self.update_webcam)

    def download_image(self):
        if self.current_image is not None:
            file_path = os.path.expanduser("~/Desktop/webcam_capture.png")
            self.current_image.save(file_path)
            os.startfile(file_path)


root = tk.Tk()
app = WebCamApp(root)
root.mainloop()
