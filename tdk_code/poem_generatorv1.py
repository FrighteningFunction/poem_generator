# A script to generate poems of various models from template api calls.
# The script varies theme (genre), style, format, and temperature for creativity randomly.
# The script logs the generated poems to a CSV file keeping track of the model, temperature, genre, format, and style and timestamp.

import csv
import time
from azure.core.exceptions import HttpResponseError

from tdk_code.openai_api_call import openai_api_call
from tdk_code.meta_api_call import meta_api_call

from datetime import datetime
import random

# List of models
models = [
    "meta-llama-3-8b-instruct", "meta-llama-3.1-405b-instruct",
    "Phi-3-small-128k-instruct", "Phi-3.5-mini-instruct",
    "gpt-4o-mini", "gpt-4o"
]

temperatures = [0.7, 0.8, 1.0]  # Vary temperature for creativity
daily_limit = 150
requests_per_minute = 15

# Lists for genres, styles, and formats
genres = [
    "horror", "adventure", "romantic", "mysterious", "happy", "sad", "fantasy", "sci-fi", "historical", "thriller", 
    "drama", "comedy", "tragedy", "mythological", "folklore", "gothic", "detective", "dystopian", "satire", "epic", 
    "paranormal", "western", "post-apocalyptic", "cyberpunk", "fairytale", "magical realism", "steampunk", 
    "coming-of-age", "slice-of-life", "crime"
]

formats = [
    # Shorter forms (3-4 lines or fewer)
    "haiku",              # 3-line poem (5-7-5 syllables)
    "tanka",              # 5-line poem (5-7-5-7-7 syllables)
    "limerick",           # 5-line humorous poem (AABBA rhyme scheme)
    "couplet",            # 2 rhyming lines
    "quatrain",           # 4-line stanza with various rhyme schemes
    "epigram",            # Short, witty, usually a few lines
    "triolet",            # 8-line poem with repetition of lines
    "clerihew",           # Humorous 4-line poem about a person
    "cinquain",           # 5-line poem with a set syllable or word pattern
    "renga",              # Linked-verse poetry, but 3-5 lines can be used (hokku)
    "epitaph",            # Short poem, often 2-4 lines, written on a tombstone
    "visual poetry",      # Poem where arrangement on the page is part of its meaning
    "monostich",          # Single-line poem
    "tetrastich",         # A stanza or poem consisting of 4 lines
    "dodoitsu",           # 4-line Japanese poem (7-7-7-5 syllables)
    "senryu",             # Similar to Haiku but focuses on human nature (3 lines)
    "proverb",            # Short, stylized saying, often 1-2 lines

    # Moderately longer forms (5+ lines)
    "sonnet",             # 14-line poem (e.g., Shakespearean or Petrarchan)
    "villanelle",         # 19-line poem with repeating lines (e.g., "Do not go gentle into that good night")
    "sestina",            # 39-line complex, structured poem
    "ode",                # Lyrical poem, often in praise of something
    "ballad",             # Narrative poem, usually in quatrains
    "blank verse",        # Unrhymed iambic pentameter
    "free verse",         # Poem without a fixed form or rhyme scheme
    "terza rima",         # A poem composed of tercets, often rhymed ABA, BCB, etc.
    "pantoum",            # A poem with repeating lines in a specific pattern
    "ghazal",             # Series of couplets that often convey themes of love and loss
    "narrative poem",     # Poem that tells a story, length can vary
    "rondeau",            # A 15-line poem with a refrain (e.g., "In Flanders Fields")
    "prose poetry"       # Prose written with the qualities of poetry (rhythmic, evocative language)
]


styles = [
    "classical", "modern", "abstract", "narrative", "confessional", "lyrical", "symbolist", "imagist", 
    "surrealist", "expressionist", "formal", "experimental", "minimalist", "stream-of-consciousness", 
    "beat", "postmodern", "romanticist", "metaphysical", "transcendental", "avant-garde", "free verse", 
    "realist", "gothic", "pastoral", "baroque", "satirical", "existentialist", "epistolary", "allegorical", "absurdist"
]

# CSV log file
csv_file = "generated_poems.csv"

def try_api_call(api_call, model, temperature, prompt, systemprompt) -> str:
    while True:
        try:
            return api_call(model, temperature, prompt, systemprompt)
        except HttpResponseError as e:
                retry_after = int(e.message.split("Please wait ")[1].split(" ")[0])
                if retry_after < 100:
                    print(f"Rate limit reached. Waiting for {retry_after} seconds.")
                    time.sleep(retry_after)
                else:
                    raise e


# Original synchronous function to generate a poem and log it to CSV
def generate_poem_and_log(model, api_call):
    # Randomly select genre, format, style and temperature
    genre = random.choice(genres)
    format = random.choice(formats)
    style = random.choice(styles)
    temperature = random.choice(temperatures)

    # Construct the prompt
    prompt = f"Write a {genre}, {style} poem in the form of a {format}."

    systemprompt = "You are a creative poet. You don't use any Markdown formatting, including asterisks, underscores, or any symbols related to formatting. You respond only with the poem, no extra instructions or commentary."

    response = try_api_call(api_call, model, temperature, prompt, systemprompt)

    poem_text = response
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the poem to CSV with proper quoting
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow([poem_text, model, temperature, genre, format, style, timestamp])

    print(f"Poem from {model} logged successfully.")


# Function to generate a customizable amount of poems with rate-limiting
# example: generate_custom_poems("gpt-4o-mini", 80, openai_api_call)
def generate_custom_poems(chosenmodel, num_poems, api_call):
    if num_poems > daily_limit:
        print(f"Exceeds daily limit of {daily_limit}. Generating only {daily_limit} poems.")
        num_poems = daily_limit

    # Determine how many full batches of poems can be made (due to the API limit)
    full_batches = num_poems // requests_per_minute
    remaining_poems = num_poems % requests_per_minute

    # Generate poems in batches to respect the rate limit
    for batch in range(full_batches):
        for _ in range(requests_per_minute):
           
            generate_poem_and_log(chosenmodel, api_call)
        print(f"Waiting 60 sec to respect the API rate limit...")
        time.sleep(60) 

    if remaining_poems > 0:
        for _ in range(remaining_poems):
            generate_poem_and_log(chosenmodel, api_call)

    print(f"Successfully generated {num_poems} poems.")

def generate_evenly_distributed_poems(num_poems):
    num_models = len(models)
    poems_per_model = num_poems // num_models
    remaining_poems = num_poems % num_models

    for model in models:
        for _ in range(poems_per_model):
            try:
                if "gpt" in model:
                    generate_poem_and_log(model, openai_api_call)
                else:
                    generate_poem_and_log(model, meta_api_call)
            except HttpResponseError as e:
                print(f"Error with model {model}: {e.message}")
                break

    for i in range(remaining_poems):
        model = models[i]
        try:
            if "gpt" in model:
                generate_poem_and_log(model, openai_api_call)
            else:
                generate_poem_and_log(model, meta_api_call)
        except HttpResponseError as e:
            print(f"Error with model {model}: {e.message}")
            continue

if __name__ == "__main__":
    generate_evenly_distributed_poems(300)  # Customize the number of poems you want to generate