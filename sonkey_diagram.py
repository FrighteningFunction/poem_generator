import pandas as pd
import plotly.graph_objects as go

# Load the dataset
dataset = pd.read_csv('generated_poems.csv')

# Filter out rows with undefined data
filtered_dataset = dataset.dropna(subset=['model', 'theme', 'form', 'style'])

# Prepare data for the Sankey diagram
labels = list(pd.concat([filtered_dataset['model'], filtered_dataset['theme'], filtered_dataset['form'], filtered_dataset['style']]).unique())
label_indices = {label: i for i, label in enumerate(labels)}

# Create source and target indices
source_indices = []
target_indices = []
values = []

# Add flows from model to theme
for model, theme in filtered_dataset[['model', 'theme']].values:
    source_indices.append(label_indices[model])
    target_indices.append(label_indices[theme])
    values.append(1)

# Add flows from theme to form
for theme, form in filtered_dataset[['theme', 'form']].values:
    source_indices.append(label_indices[theme])
    target_indices.append(label_indices[form])
    values.append(1)

# Add flows from form to style
for form, style in filtered_dataset[['form', 'style']].values:
    source_indices.append(label_indices[form])
    target_indices.append(label_indices[style])
    values.append(1)

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values
    )
)])

fig.update_layout(title_text="Sankey Diagram of Generated Poems", font_size=10)
fig.show()