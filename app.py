import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict
import time

class SimplePeopleTracker:
    def __init__(self):
    
        self.model = YOLO('yolov8n.pt')
        self.track_history = defaultdict(lambda: [])
        
    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        results = self.model.track(frame, persist=True, classes=[0])  # class 0 = person
        

        annotated_frame = results[0].plot()
        
       
        current_people_count = 0
        if results[0].boxes is not None:
            current_people_count = len(results[0].boxes)
        
        
        cv2.putText(annotated_frame, f'Anlik Kisi Sayisi: {current_people_count}', 
                   (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        
        return annotated_frame

def main():
    tracker = SimplePeopleTracker()
    
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Kamera açılamadı!")
        return
    
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    print("Basit insan takip uygulaması başlatıldı...")
    print("Çıkmak için 'q' tuşuna basın")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        processed_frame = tracker.process_frame(frame)
        
        
        cv2.imshow('Stand Insan Takip - Basit', processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Uygulama kapatıldı.")

if __name__ == "__main__":
    main()