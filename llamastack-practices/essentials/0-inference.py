import os
import sys

from dotenv import load_dotenv

load_dotenv()

def create_http_client():
    from llama_stack_client import LlamaStackClient

    host = os.environ["LLAMA_STACK_SERVER_HOST"]
    port = os.environ["LLAMA_STACK_SERVER_PORT"]

    return LlamaStackClient(
        base_url=f"http://{host}:{port}"
    )

client = (
    create_http_client()
)  


models = client.models.list()

print("--- Available models: ---")

for m in models:
    print(f"- {m.identifier}")
    
print()

response = client.inference.chat_completion(
    model_id=os.environ["INFERENCE_MODEL"],
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about coding"},
    ],
)

print(response.completion_message.content)