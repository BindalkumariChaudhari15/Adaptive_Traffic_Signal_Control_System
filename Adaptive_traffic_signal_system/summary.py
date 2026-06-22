import csv
import os

#Output folder
output_folder = "results"
os.makedirs(output_folder, exist_ok=True)

#Report summary
data = [
    ["Metric", "Fixed-Time", "Adaptive"],
    ["Pedestrian Wait (s)", 42, 25],
    ["Vehicle Delay (s)", 55, 40],
    ["Throughput", 120, 145],
    ["Queue Length", 30, 18],
    ["Fairness Index", 0.62, 0.81]
]

#Save file
output_path = os.path.join(output_folder, "summary_table.csv")

with open(output_path, "w", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Summary table saved at:", output_path)