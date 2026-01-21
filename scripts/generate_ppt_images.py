import os
import requests
import time
from openai import OpenAI

# --------------------------------------------------------------------------
# CONFIGURATION
# --------------------------------------------------------------------------
# Get your API key from: https://www.volcengine.com/product/ark
# Set it as an environment variable or fill it in below (not recommended for public repos)
API_KEY = os.environ.get("ARK_API_KEY")

if not API_KEY:
    print("Error: ARK_API_KEY is not set.")
    print("Please set the ARK_API_KEY environment variable.")
    print("You can obtain a key from: https://www.volcengine.com/product/ark")
    exit(1)

# Base URL for Volcengine Ark
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

# Initialize OpenAI Client
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

# --------------------------------------------------------------------------
# PPT PAGES DATA (Populated by the Agent)
# --------------------------------------------------------------------------
# This list will be populated by the ppt-planning-generator skill
# Example format:
# PPT_PAGES = [
#     {
#         "filename": "MySlide_Page01.png",
#         "prompt": "Create a professional PPT slide..."
#     }
# ]
PPT_PAGES = [] 

def generate_ppt_images():
    if not PPT_PAGES:
        print("No pages to generate. Please ensure PPT_PAGES is populated.")
        return

    print(f"Starting generation for {len(PPT_PAGES)} slides...")
    
    for index, page in enumerate(PPT_PAGES):
        filename = page["filename"]
        prompt = page["prompt"]
        
        print(f"\n[{index+1}/{len(PPT_PAGES)}] Generating: {filename}")

        try:
            start_time = time.time()
            # Call the image generation model
            # Model name might need adjustment based on your specific deployment
            imagesResponse = client.images.generate(
                model="doubao-seedream-4-5-251128", 
                prompt=prompt,
                size="2K",
                response_format="url"
            )
            
            if imagesResponse.data:
                image_url = imagesResponse.data[0].url
                print(f"Downloading image from {image_url[:50]}...")
                
                # Save image to file
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(filename, "wb") as f:
                        f.write(response.content)
                    print(f"✅ Saved to: {os.path.abspath(filename)}")
                else:
                    print(f"❌ Failed to download. Status: {response.status_code}")
            else:
                print("❌ No image data returned.")
                
            elapsed = time.time() - start_time
            print(f"Time taken: {elapsed:.2f}s")
            
        except Exception as e:
            print(f"❌ Error generating {filename}: {e}")

if __name__ == "__main__":
    generate_ppt_images()
