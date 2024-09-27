import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# models: "meta-llama-3-8b-instruct", "meta-llama-3.1-405b-instruct"

endpoint = "https://models.inference.ai.azure.com"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def meta_api_call(model, temperature, userprompt, systemprompt):
    response = client.complete(
    messages=[
        SystemMessage(content=systemprompt),
        UserMessage(content=userprompt),
    ],
    temperature=temperature,
    top_p=1.0,
    max_tokens=1000,
    model=model
)

    return response

#print(response.choices[0].message.content)