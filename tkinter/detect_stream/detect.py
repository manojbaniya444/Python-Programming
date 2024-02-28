import cv2
import numpy as np
from ultralytics import YOLO
import gc

# Load the YOLOv8 model
model = YOLO('best.pt')

names = model.model.names

class LicensePlateDetector:
    def __init__(self):
        self.model = model
        self.names = model.model.names

        self.annotated_frame = None
        self.cropped_plate = None

    def detect_objects(self, frame):
        # use yolo model here
        self.annotated_frame = frame

        original_frame = frame.copy()

        # Run YOLOv8 inference on the frame
        results = self.model(frame)

        # Visualize the results on the frame
        for result in results:
            boxes = result.boxes.xyxy.cpu()
            clss = result.boxes.cls.cpu().tolist()
            confs = result.boxes.conf.float().cpu().tolist()


            self.annotated_frame = results[0].plot() if any(conf > 0.7 for conf in confs) else self.annotated_frame

            for box, cls, conf in zip(boxes, clss, confs):
                class_name = self.names[int(cls)]

                # Show the frame only when a license plate is detected and when the confidence score is greater than 70 percent
                if class_name == 'license_plate' and conf > 0.7:
                    print(f"Class Name: {class_name}, Confidence Score: {conf}, Bounding Box: {box}")
                    coordinates = box  # License plate coordinates

                    self.cropped_plate = frame[int(coordinates[1]):int(coordinates[3]), int(coordinates[0]):int(coordinates[2])]
                    self.cropped_plate = cv2.resize(self.cropped_plate, (300, 100))

        # Rest of the detection code...

        return (self.annotated_frame, self.cropped_plate)
