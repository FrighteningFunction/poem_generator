import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv('generated_poems.csv')

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

# Function to generate and save heatmap
def generate_heatmap(pivot_table, title, xlabel, ylabel, filename):
    plt.figure(figsize=(14, 12))
    heatmap = sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(fontsize=12, rotation=90)
    plt.yticks(fontsize=12, rotation=0)
    plt.tight_layout()  # Adjust layout to ensure everything fits without being cropped
    
    heatmap_file = os.path.join(output_dir, filename)
    plt.savefig(heatmap_file)
    plt.close()

# Generate and save heatmaps
generate_heatmap(pivot_table_theme_form, 'Heatmap of Themes vs Forms', 'Form', 'Theme', 'heatmap_theme_form.png')
generate_heatmap(pivot_table_theme_style, 'Heatmap of Themes vs Styles', 'Style', 'Theme', 'heatmap_theme_style.png')
generate_heatmap(pivot_table_form_style, 'Heatmap of Forms vs Styles', 'Style', 'Form', 'heatmap_form_style.png')

print("Heatmaps generated and saved to the output directory.")