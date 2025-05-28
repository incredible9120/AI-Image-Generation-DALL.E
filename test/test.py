import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
import uuid

# Create output directory if it doesn't exist
output_path = os.path.join(os.path.dirname(__file__), "generated_images")
os.makedirs(output_path, exist_ok=True)

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=OPEN_API_KEY)

# Get prompt from user
prompt = input("Enter your image generation prompt: ")

response = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    n=1,
    size="512x512",
)

image_url = response.data[0].url

# Download and save image
image_data = requests.get(image_url).content
image_name = f"{uuid.uuid4()}.png"
image_path = os.path.join(output_path, image_name)

with open(image_path, "wb") as f:
    f.write(image_data)
