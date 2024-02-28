import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os
import gc

from detect import LicensePlateDetector

class WebCamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam app")

        # yolo model
        self.detector = LicensePlateDetector()

        # Replace the following line with the RTSP URL of your stream
        rtsp_url = 'rtsp://192.168.1.69:8080/h264_ulaw.sdp'
        self.video = cv2.VideoCapture(rtsp_url)

        self.detected_frame = None
        self.detected_licensePlate = None

        self.frame_skip = 20
        self.frame_counter = 0
        
        self.canvas = tk.Canvas(window, width=640, height=640)
        self.canvas.pack()

        self.canvas2 = tk.Canvas(window, width=300, height=100)
        self.canvas2.pack()

        self.download_button = tk.Button(window, text="Capture", command=self.download_image)
        self.download_button.pack()

        self.update_webcam()

    # def detect_license_plate(self, frame):
    #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     return frame

    def update_webcam(self):
        ret, frame = self.video.read()
        frame = cv2.resize(frame, (640, 640))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if self.detected_frame is not None:
            self.detected_frame.close()
            self.detected_frame = None
            gc.collect()

        if self.detected_licensePlate is not None:
            self.detected_licensePlate.close()
            self.detected_licensePlate = None
            gc.collect()

        if ret:
            self.frame_counter += 1
            if self.frame_counter % self.frame_skip == 0:
                # processing to the yolo model
                # detected_frame = self.detector.detect_objects(frame)
                detected_frame, detected_license_plate = self.detector.detect_objects(frame)


                self.detected_frame = Image.fromarray(detected_frame)
                self.photo = ImageTk.PhotoImage(image=self.detected_frame)
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

                if detected_license_plate is not None:
                    self.detected_licensePlate = Image.fromarray(detected_license_plate)
                    self.photo2 = ImageTk.PhotoImage(image=self.detected_licensePlate)
                    self.canvas2.create_image(0, 0, image=self.photo2, anchor=tk.NW)
                else:
                    self.canvas2.create_text(150, 50, text="No License Plate Detected", font=("Helvetica", 20), fill="blue")
            self.window.after(1, self.update_webcam)

    def download_image(self):
        if self.current_image is not None:
            file_path = os.path.expanduser("~/Desktop/webcam_capture.png")
            self.current_image.save(file_path)
            os.startfile(file_path)

root = tk.Tk()
app = WebCamApp(root)
root.mainloop()
