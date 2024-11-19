import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv('database_packs/training_v1/generated_poems_OLD.csv')

# Convert non-string types to string if necessary
dataset['style'] = dataset['style'].astype(str)

# Filter the dataset to remove rows with NaN values in 'theme', 'form', or 'style'
filtered_dataset = dataset.dropna(subset=['theme', 'form', 'style'])

# Ensure the output directory exists
output_dir = 'diagram_output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create pivot tables for each combination of 'theme', 'form', and 'style'
pivot_table_theme_form = filtered_dataset.pivot_table(index='theme', columns='form', values='style', aggfunc='count', fill_value=0)
pivot_table_theme_style = filtered_dataset.pivot_table(index='theme', columns='style', values='form', aggfunc='count', fill_value=0)
pivot_table_form_style = filtered_dataset.pivot_table(index='form', columns='style', values='theme', aggfunc='count', fill_value=0)

# Function to generate and show heatmap
def generate_heatmap(pivot_table, xlabel, ylabel):
    plt.figure(figsize=(10, 8))  # Adjust figure size to fit the screen better
    heatmap = sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
    # plt.title(title, fontsize=16)  # Remove title
    plt.xlabel(xlabel, fontsize=28)  # Increase font size by 3
    plt.ylabel(ylabel, fontsize=28)  # Increase font size by 3
    plt.xticks(fontsize=10, rotation=90)
    plt.yticks(fontsize=10, rotation=0)
    plt.tight_layout()  # Adjust layout to ensure everything fits without being cropped
    plt.show()  # Show the heatmap instead of saving it
    plt.close()

# Generate and show heatmap for 'form' and 'style'
generate_heatmap(pivot_table_form_style, 'Style', 'Form')

print("Heatmap generated and displayed.")