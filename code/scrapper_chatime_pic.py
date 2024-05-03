import requests
from bs4 import BeautifulSoup
import os

# Function to scrape images from a single page
def scrape_images(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all image elements
        img_tags = soup.find_all('img')
        # Extract image URLs
        image_urls = [img['src'] for img in img_tags if img.has_attr('src')]
        return image_urls
    else:
        print(f"Failed to fetch page: {url}")
        return []

# URLs to scrape
urls = [
    "https://chatime.com/drinks/",
    "https://chatime.com/drinks/page/2/",
    "https://chatime.com/drinks/page/3/",
    "https://chatime.com/drinks/page/4/"
]

# Directory to save images
output_dir = "/workspaces/boba-tea-calories-calculator/data/pic/chatime"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Scrape images from each URL
for url in urls:
    image_urls = scrape_images(url)
    if image_urls:
        # Download images
        for i, image_url in enumerate(image_urls):
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(f"{output_dir}/image_{i}.jpg", "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded image {i}")
                else:
                    print(f"Failed to download image: {image_url}")
            except Exception as e:
                print(f"Error downloading image: {str(e)}")
    else:
        print(f"No images found on page: {url}")
