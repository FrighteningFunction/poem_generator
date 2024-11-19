import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv('database_packs/training_v1/generated_poems_OLD.csv')

# Count the number of poems for each model type
model_counts = dataset['model'].value_counts()

# Calculate the percentage of poems for each model type
model_percentages = (model_counts / model_counts.sum()) * 100

# Print the results to the console
print("Number of poems for each model type:")
print(model_counts)
print("\nPercentage of poems for each model type:")
print(model_percentages)

# Data for the pie chart
labels = model_counts.index
sizes = model_counts.values
colors = plt.cm.Paired(range(len(labels)))
explode = [0.1 if i == model_counts.idxmax() else 0 for i in labels]  # explode the largest slice

# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140, textprops={'fontsize': 18})
# plt.title('Distribution of LLM-s in dataset', fontsize=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()