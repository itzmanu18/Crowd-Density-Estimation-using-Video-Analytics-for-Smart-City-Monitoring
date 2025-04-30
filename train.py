from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",                    
    epochs=50,
    imgsz=640,
    batch=8,
    project="crowd_detection_yolov8", 
    name="nandi_model",                  
    verbose=True
)
