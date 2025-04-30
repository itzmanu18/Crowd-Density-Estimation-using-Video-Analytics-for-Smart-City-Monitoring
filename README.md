# 🧠 Crowd-Density-Estimation-using-Video-Analytics-for-Smart-City-Monitoring Using YOLOv8
### 📍 Smart City Surveillance – MG Road & Nandi

This project implements an intelligent crowd monitoring system using YOLOv8 for real-time people detection and density estimation in public spaces. The system was tested on two self-recorded videos: **MG Road** and **Nandi**.

---

## 🎯 Objective

- Simulate an IoT-based smart city surveillance system.
- Detect and count people in real-world videos.
- Estimate crowd density over time.
- Generate visual insights using detection results.

---

## 📁 Project Structure

Crowd_Density_Estimation/ ├── MG_ROAD/ │ ├── MG Road.ipynb │ ├── MG Road.mp4 │ ├── Output Graphs (PNG) │ ├── crowd_density_results.csv │ ├── images/ (extracted frames) │ └── labels/ (YOLO format) │ ├── NANDI/ │ ├── Nandi.ipynb │ ├── Nandi.mp4 │ ├── Output Graphs (PNG) │ ├── crowd_density_results.csv │ ├── images/ │ └── labels/ │ ├── train.py ├── predict.py ├── requirements.txt └── README.md

---

## 🚶‍♂️ Model Details

- **Model Used**: YOLOv8 (Ultralytics)
- **Training**: Performed on self-annotated datasets
- **Inference**: Applied on full video files to generate detections
- **Density Classification**:
  - **Low**: 0–10 people
  - **Medium**: 11–25 people
  - **High**: 26+ people

---

## 📊 Visual Output

Each notebook includes:

- 📽️ Inference video with bounding boxes
- 📈 Graph: People Count vs Time
- 🧮 Pie Chart: Density Category Distribution

---

## 🛠️ Technologies Used

- Python 3.119
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- CVAT
- Jupyter Notebook
- Matplotlib / Pandas

---

