import json
import matplotlib.pyplot as plt

# Initialize counters
human_count = 0
machine_count = 0

# Open and read the JSONL file
with open('joint_poem_dataset.jsonl', 'r') as jsonl_file:
    for line in jsonl_file:
        poem = json.loads(line)
        if poem['Label'] == 'human':
            human_count += 1
        elif poem['Label'] == 'machine':
            machine_count += 1

# Print counts to console
print(f"Number of human-generated poems: {human_count}")
print(f"Number of machine-generated poems: {machine_count}")

# Data for the pie chart
labels = ['Human', 'Machine']
sizes = [human_count, machine_count]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # explode the 1st slice (Human)

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('Distribution of Human and Machine Generated Poems')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()