import pandas as pd
import plotly.express as px

# Load the dataset
dataset = pd.read_csv('generated_poems.csv')

# Filter out rows with undefined data
filtered_dataset = dataset.dropna(subset=['model', 'theme', 'form', 'style'])

# Prepare data for the bubble chart matrix
bubble_data = filtered_dataset.groupby(['model', 'theme', 'form', 'style']).size().reset_index(name='count')

# Create the bubble chart matrix
fig = px.scatter_matrix(
    bubble_data,
    dimensions=['model', 'theme', 'form', 'style'],
    size='count',
    color='model',
    title='Bubble Chart Matrix of Generated Poems',
    labels={'count': 'Number of Poems'}
)

fig.update_traces(marker=dict(opacity=0.6, sizemode='area', line=dict(width=2, color='DarkSlateGrey')))
fig.update_layout(width=1000, height=800)
fig.show()