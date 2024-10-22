import pandas as pd
import plotly.express as px

# Load the dataset
dataset = pd.read_csv('generated_poems.csv')

# Filter out rows with undefined data
filtered_dataset = dataset.dropna(subset=['model', 'theme', 'form', 'style'])

# Prepare data for the facet grid bar charts
facet_data = filtered_dataset.groupby(['model', 'theme', 'form', 'style']).size().reset_index(name='count')

# Create the facet grid bar charts
fig = px.bar(
    facet_data,
    x='theme',
    y='count',
    color='style',
    facet_col='model',
    facet_col_wrap=2,
    title='Facet Grid Bar Charts of Generated Poems',
    labels={'count': 'Number of Poems', 'theme': 'Genre', 'form': 'Format', 'style': 'Style'}
)

fig.update_layout(barmode='stack', width=1200, height=800)
fig.show()