import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os
import threading
import gc
import numpy as np

from detect import LicensePlateDetector

class WebCamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam app")

        self.detector = LicensePlateDetector()

        rtsp_url = 'rtsp://192.168.1.69:8080/h264_ulaw.sdp'
        self.video = cv2.VideoCapture(rtsp_url)

        self.detected_frame = None
        self.detected_license_plate = None

        self.frame_skip = 20
        self.frame_counter = 0

        self.canvas = tk.Canvas(window, width=640, height=640)
        self.canvas.pack()

        self.canvas2 = tk.Canvas(window, width=300, height=100)
        self.canvas2.pack()

        self.download_button = tk.Button(window, text="Capture", command=self.download_image)
        self.download_button.pack()

        self.is_running = True
        self.update_webcam()

    def update_webcam(self):
        ret, frame = self.video.read()

        if ret:
            frame = cv2.resize(frame, (640, 640))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            if self.detected_frame is not None:
                self.detected_frame.close()
                self.detected_frame = None
                gc.collect()

            if self.detected_license_plate is not None:
                self.detected_license_plate.close()
                self.detected_license_plate = None
                gc.collect()

            self.frame_counter += 1
            if self.frame_counter % self.frame_skip == 0:
                # Perform image processing and object detection
                detected_frame, detected_license_plate = self.detector.detect_objects(frame)

                # Convert to ImageTk format
                self.detected_frame = Image.fromarray(detected_frame)
                self.photo = ImageTk.PhotoImage(image=self.detected_frame)
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

                if detected_license_plate is not None:
                    self.detected_license_plate = Image.fromarray(detected_license_plate)
                    self.photo2 = ImageTk.PhotoImage(image=self.detected_license_plate)
                    self.canvas2.create_image(0, 0, image=self.photo2, anchor=tk.NW)
                else:
                    self.canvas2.create_text(150, 50, text="No License Plate Detected", font=("Helvetica", 20), fill="blue")

        if self.is_running:
            self.window.after(1, self.update_webcam)

    def download_image(self):
        if self.detected_frame is not None:
            file_path = os.path.expanduser("~/Desktop/webcam_capture.png")
            self.detected_frame.save(file_path)
            os.startfile(file_path)

    def close(self):
        self.is_running = False
        self.video.release()

root = tk.Tk()
app = WebCamApp(root)

# Bind the closing event to the close method
root.protocol("WM_DELETE_WINDOW", app.close)

root.mainloop()
