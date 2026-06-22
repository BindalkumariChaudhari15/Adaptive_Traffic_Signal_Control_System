import matplotlib.pyplot as plt
import os

#Create output folder
output_folder = "results"
os.makedirs(output_folder, exist_ok=True)

metrics = ["Wait Time", "Vehicle Delay", "Throughput", "Queue Length", "Fairness"]

fixed_time = [42, 55, 120, 30, 0.62]
adaptive = [25, 40, 145, 18, 0.81]

x = range(len(metrics))

#Plot
plt.figure(figsize=(10, 5))

plt.plot(x, fixed_time, marker="o", label="Fixed_Time")
plt.plot(x, adaptive, marker="o", label="Adaptive")

plt.xticks(x, metrics)

plt.title("Overall Performance Dashboard")
plt.ylabel("Value (Mixed Scales)")
plt.legend()

#Save image inside results folder
output_path = os.path.join(output_folder, "summary.png")
plt.savefig(output_path)

#Display chart
plt.show()

print("Saved at:", output_path)