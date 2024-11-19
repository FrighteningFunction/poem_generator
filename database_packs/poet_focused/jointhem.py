import json
import random

def merge_files(human_file, machine_file, output_file):
    poems = []
    
    with open(human_file, 'r') as hf, open(machine_file, 'r') as mf:
        for line in hf:
            poem = json.loads(line)
            poem['label'] = 'human'
            poems.append(poem)
        
        for line in mf:
            poem = json.loads(line)
            poem['label'] = 'machine'
            poems.append(poem)
    
    random.shuffle(poems)
    
    with open(output_file, 'w') as of:
        for poem in poems:
            of.write(json.dumps(poem) + '\n')

if __name__ == "__main__":
    human_file = 'c:/Users/szoko/Documents/VSproj/poem_generator/human_dataset/poet_focused/shakespeare100sonnets.jsonl'
    machine_file = 'c:/Users/szoko/Documents/VSproj/poem_generator/tdk_code/poem_generator_v2/generated_sonnets.jsonl'
    output_file = 'c:/Users/szoko/Documents/VSproj/poem_generator/database_packs/poet_focused/shakespeare_test.jsonl'
    
    merge_files(human_file, machine_file, output_file)
