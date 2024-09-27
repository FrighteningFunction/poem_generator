from tdk_code.poem_generator import generate_poem_and_log
from tdk_code.meta_api_call import meta_api_call

# Function to test single poem generation
def test_single_generation():
    # Specify parameters for testing
    # model = "gpt-4o-mini"
    model= "meta-llama-3-8b-instruct"
    api_call = meta_api_call

    # Run the async function using asyncio
    generate_poem_and_log(model, api_call)

# Run the test function
test_single_generation()