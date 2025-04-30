import os
import pandas as pd
import matplotlib.pyplot as plt

predict_path = r"C:\Users\Manoj\Downloads\Crowd_Detection_Project\runs\detect\predict2\labels"

frame_data = []

for file in sorted(os.listdir(predict_path)):
    if file.endswith(".txt"):
        frame_name = file.replace(".txt", "")
        with open(os.path.join(predict_path, file), "r") as f:
            lines = f.readlines()
            person_count = len(lines)  

            
            if person_count <= 10:
                density = "Low"
            elif person_count <= 25:
                density = "Medium"
            else:
                density = "High"

            frame_data.append({
                "frame": frame_name,
                "count": person_count,
                "density": density
            })

df = pd.DataFrame(frame_data)
print(df.head()) 
df.to_csv("crowd_density_results.csv", index=False)
print("✅ Results saved to crowd_density_results.csv")


plt.figure(figsize=(12, 5))
plt.plot(df["frame"], df["count"], marker='o')
plt.xticks(rotation=45)
plt.title("People Count per Frame")
plt.xlabel("Frame")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("count_per_frame.png")
plt.show()


plt.figure(figsize=(6, 5))
df["density"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["green", "orange", "red"])
plt.title("Crowd Density Distribution")
plt.ylabel("")
plt.savefig("density_distribution.png")
plt.show()
