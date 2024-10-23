import json
import random

# Read the dataset
with open('joint_poem_dataset.jsonl', 'r') as file:
    poems = [json.loads(line) for line in file]

# Rename the keys
for poem in poems:
    poem['text'] = poem.pop('Poem')
    poem['label'] = poem.pop('Label')

# Separate poems by label
human_poems = [poem for poem in poems if poem['label'] == 'human']
machine_poems = [poem for poem in poems if poem['label'] == 'machine']

# Calculate the number of poems for each set
total_poems = len(poems)
test_set_size = total_poems // 5
validation_set_size = total_poems // 10
finetune_set_size = total_poems - test_set_size - validation_set_size

# Ensure each set has an equal ratio of human and machine-labeled poems
test_set_size_per_label = test_set_size // 2
validation_set_size_per_label = validation_set_size // 2
finetune_set_size_per_label = (finetune_set_size // 2)

# Randomly shuffle the poems
random.shuffle(human_poems)
random.shuffle(machine_poems)

# Create the test set
test_set = human_poems[:test_set_size_per_label] + machine_poems[:test_set_size_per_label]

# Create the validation set
validation_set = human_poems[test_set_size_per_label:test_set_size_per_label + validation_set_size_per_label] + \
                 machine_poems[test_set_size_per_label:test_set_size_per_label + validation_set_size_per_label]

# Create the finetune set
finetune_set = human_poems[test_set_size_per_label + validation_set_size_per_label:] + \
               machine_poems[test_set_size_per_label + validation_set_size_per_label:]

# Write the test set to test_poem_dataset.jsonl
with open('test_poem_dataset.jsonl', 'w') as file:
    for poem in test_set:
        file.write(json.dumps(poem) + '\n')

# Write the validation set to validation_poem_dataset.jsonl
with open('validation_poem_dataset.jsonl', 'w') as file:
    for poem in validation_set:
        file.write(json.dumps(poem) + '\n')

# Write the finetune set to finetune_poem_dataset.jsonl
with open('finetune_poem_dataset.jsonl', 'w') as file:
    for poem in finetune_set:
        file.write(json.dumps(poem) + '\n')