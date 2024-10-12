import pandas as pd

# Load both CSV datasets
human_poems = pd.read_csv('PoemDataset.csv')
ai_poems = pd.read_csv('generated_poems.csv')

# Concatenate Title and Poem in the human dataset
human_poems['Poem'] = human_poems['Title'] + ' ' + human_poems['Poem']

# Create the AI label (1 for AI-generated)
ai_poems['Label'] = 1

# Create the Human label (0 for human-written)
human_poems['Label'] = 0

# Select only 'Poem' and 'Label' columns from both datasets
human_poems = human_poems[['Poem', 'Label']]
ai_poems = ai_poems[['Poem', 'Label']]

# Ensure equal amounts from both categories by truncating the longer dataset
min_length = min(len(human_poems), len(ai_poems))
human_poems = human_poems[:min_length]
ai_poems = ai_poems[:min_length]

# Concatenate both datasets into a joint dataset
joint_dataset = pd.concat([human_poems, ai_poems], ignore_index=True)

# Shuffle the dataset to mix AI and human poems
joint_dataset = joint_dataset.sample(frac=1).reset_index(drop=True)

# Save the joint dataset to a new CSV file
joint_dataset.to_csv('joint_poem_dataset.csv', index=False)

# Confirm completion
print("Joint dataset created and saved as 'joint_poem_dataset.csv'.")