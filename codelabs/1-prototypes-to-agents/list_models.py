import google.generativeai as genai
import os

if "GOOGLE_API_KEY" not in os.environ:
    print("Please set GOOGLE_API_KEY")
    exit(1)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Listing available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

