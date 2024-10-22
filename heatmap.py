import os
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

# Load the dataset
dataset = pd.read_csv('generated_poems.csv')

# Check for the data type of the 'style' column
print(dataset['style'].apply(type).unique())

# Convert non-string types to string if necessary
dataset['style'] = dataset['style'].astype(str)

# Now, try to create the heatmap as before
filtered_dataset = dataset.dropna(subset=['theme', 'form', 'style'])

# Create a pivot table for the heatmap
pivot_table = filtered_dataset.pivot_table(index='theme', columns='form', values='style', aggfunc='count', fill_value=0)

# Proceed with heatmap generation


output_dir = 'diagram_output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

dataset = pd.read_csv('generated_poems.csv')

filtered_dataset = dataset.dropna(subset=['theme', 'form', 'style'])

types = ['theme', 'form', 'style']

for i in range(len(types)):
    for j in range(i + 1, len(types)):
        # Define the two types to compare
        x_type = types[i]
        y_type = types[j]

        # Create a pivot table for the heatmap
        pivot_table = filtered_dataset.pivot_table(index=y_type, columns=x_type, values='style', aggfunc='count', fill_value=0)

        # Create the heatmap
        plt.figure(figsize=(16, 10))
        heatmap = sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", annot_kws={"size": 10}, cbar_kws={'label': 'Count'})

        # Customize x-axis and y-axis labels
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.yticks(fontsize=12)

        # Add axis titles and plot title
        plt.xlabel(f'{x_type.capitalize()}', fontsize=14, labelpad=20)
        plt.ylabel(f'{y_type.capitalize()}', fontsize=14, labelpad=20)
        plt.title(f'Heatmap of {y_type.capitalize()} vs {x_type.capitalize()}', fontsize=16, fontweight='bold', pad=20)

        # Adjust layout
        plt.tight_layout()

        # Save the plot to the diagram_output folder
        output_path = os.path.join(output_dir, f'heatmap_{y_type}_vs_{x_type}.png')
        plt.savefig(output_path)

        # Close the plot to free memory for the next one
        plt.close()

print(f"Heatmaps saved in {output_dir}/")
