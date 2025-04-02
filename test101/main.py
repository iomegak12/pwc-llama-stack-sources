import os

from art import tprint
from dotenv import load_dotenv


if __name__ == "__main__":
    tprint("Llama Stack at PwC")

    load_dotenv()
    
    print(f"Together API Key: {os.getenv("TOGETHER_API_KEY")}")    
    