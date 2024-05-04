import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

# Path to save images
image_path = '/workspaces/boba-tea-calories-calculator/data/pic/coco'

# URLs of the pages to scrape
urls = [
    'https://cocobubbletea.com/seasonal',
    'https://cocobubbletea.com/milk-tea',
    'https://cocobubbletea.com/fruit-tea',
    'https://cocobubbletea.com/yakult',
    'https://cocobubbletea.com/slush-smoothie',
    'https://cocobubbletea.com/tea-latte',
    'https://cocobubbletea.com/cloud',
    'https://cocobubbletea.com/fresh-tea',
    'https://cocobubbletea.com/tapioca-milk'
]

def download_and_convert_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Load image from bytes
            image = Image.open(BytesIO(response.content))
            image_name = os.path.basename(image_url).split('.')[0] + '.png'
            image.save(os.path.join(save_path, image_name), 'PNG')
            print(f"Image saved as {image_name} with dimensions {image.size}")
        else:
            print(f"Failed to download the image: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_images(url, save_path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img', attrs={'data-src': True})
        count = 0  # Initialize count variable
        for img in images:
            image_url = img['data-src']
            download_and_convert_image(image_url, save_path)
            count += 1  # Increment count for each downloaded image
        print(f"Downloaded {count} pictures")
    else:
        print(f"Failed to retrieve webpage: {response.status_code}")

# Call the scrape_images function for each URL
for url in urls:
    scrape_images(url, image_path)

# Rename the picture files
def capitalize_first_letter(string):
    return ' '.join(word.capitalize() if word != 'QQ' else word for word in string.split())

for filename in os.listdir(image_path):
    new_filename = capitalize_first_letter(filename.replace('+', ' '))
    os.rename(os.path.join(image_path, filename), os.path.join(image_path, new_filename))
    print(f"Renamed {filename} to {new_filename}")

for filename in os.listdir(image_path):
    os.rename(os.path.join(image_path, '2 Guys.png'), os.path.join(image_path, '2 Ladies Milk Tea.png'))
    os.rename(os.path.join(image_path, '3 Guys.png'), os.path.join(image_path, '3 Guys Milk Tea.png'))