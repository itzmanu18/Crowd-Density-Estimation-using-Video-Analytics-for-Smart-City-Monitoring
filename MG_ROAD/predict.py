from ultralytics import YOLO

model = YOLO("crowd_detection_yolov8/mg_road_model3/weights/best.pt")

model.predict(
    source="MG Road.mp4",
    save=True,
    save_txt=True,   
    conf=0.4,
    show=True
)
