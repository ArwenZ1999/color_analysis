import os
from dotenv import load_dotenv
load_dotenv() 
#api_key=input("Please enter your API key: ")
api_key=os.getenv("OPENAI_API_KEY")
