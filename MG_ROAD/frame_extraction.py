import cv2
import os

videos = ['MG Road.mp4']  
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

frame_rate = 5  

for video in videos:
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    count = 0
    saved = 0
    while success:
        if count % int(vidcap.get(cv2.CAP_PROP_FPS)) // frame_rate == 0:
            cv2.imwrite(f"{output_dir}/{video}_{saved}.jpg", image)
            saved += 1
        success, image = vidcap.read()
        count += 1
    vidcap.release()
