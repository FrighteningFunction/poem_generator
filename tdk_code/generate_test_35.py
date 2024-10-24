import argparse
from tdk_code.poem_generator import generate_poem_and_log
from tdk_code.openai_pure_call import openai_pure_call

def generate_poems(count: int):
    for i in range (count):
        generate_poem_and_log("gpt-3.5-turbo-0125", openai_pure_call)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a specified number of poems.")
    parser.add_argument("count", type=int, help="Number of poems to generate")
    args = parser.parse_args()
    
    generate_poems(args.count)