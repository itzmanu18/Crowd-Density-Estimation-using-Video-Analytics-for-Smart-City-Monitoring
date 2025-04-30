from ultralytics import YOLO

model = YOLO("crowd_detection_yolov8/nandi_model6/weights/best.pt")  


model.predict(
    source="Nandi.mp4",          
    save=True,
    save_txt=True,
    save_conf=True,
    show=True,
    conf=0.4
)
