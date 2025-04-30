# Crowd Density Estimation using YOLOv8
### 📍 Smart Surveillance System – MG Road & Nandi Locations

This project demonstrates real-time crowd density estimation using self-captured videos and a YOLOv8-based deep learning model. It simulates an IoT-based smart city surveillance system capable of detecting and classifying crowd density levels for public safety and monitoring.

---

## ✅ Components Completed

- **Video Capture**: 2 real-world scenes (MG Road and Nandi) recorded using a mobile phone.
- **Frame Extraction**: 50+ frames extracted from each video.
- **Annotation**: Manual annotation of people using bounding boxes in YOLO format (via CVAT).
- **Model Training**: YOLOv8 trained using custom annotated data.
- **Inference**: Model used to detect and count people in videos.
- **Density Analysis**:
  - Counted people per frame
  - Classified density as Low (0–10), Medium (11–25), High (26+)
  - Generated time series and pie charts

---

## 📊 Outputs

Each notebook contains:
- Frame-by-frame detections
- Output video with bounding boxes
- Graphs for:
  - People Count vs Time
  - Density Category Distribution

---

## 🔗 Submission Links

- **📂 Google Drive Folder**: [Add your public Google Drive link here]
- **📁 GitHub Repository**: [Add your GitHub repo link here]

---

## 🛠 Tools Used

- Python 3.119
- YOLOv8 (Ultralytics)
- OpenCV
- CVAT
- Jupyter Notebook


