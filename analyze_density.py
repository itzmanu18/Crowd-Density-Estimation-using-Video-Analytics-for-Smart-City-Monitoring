import os
import re
import pandas as pd
import matplotlib.pyplot as plt

labels_dir = "runs/detect/predict/labels"

def extract_frame_number(filename):
    match = re.search(r"_(\d+)\.txt", filename)
    return int(match.group(1)) if match else -1

frames = []
counts = []

for file in sorted(os.listdir(labels_dir), key=extract_frame_number):
    if file.endswith(".txt"):
        path = os.path.join(labels_dir, file)
        with open(path) as f:
            count = len(f.readlines())
        frame = extract_frame_number(file)
        frames.append(frame)
        counts.append(count)

df = pd.DataFrame({"frame": frames, "count": counts})
df.to_csv("crowd_density_results.csv", index=False)

plt.figure(figsize=(10, 5))
plt.plot(df["frame"], df["count"], marker='o', color='blue')
plt.title("Crowd Density Over Time")
plt.xlabel("Frame Number")
plt.ylabel("People Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("time_vs_people_count.png")
plt.show()
