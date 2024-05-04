import os
import requests
from bs4 import BeautifulSoup

def find_subpages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    base_url = "https://www.kungfutea.com"
    excluded_urls = {base_url, base_url + '/'}
    links = soup.select('div.elementor-widget-image a')
    sub_urls = [a['href'] for a in links if 'href' in a.attrs and a['href'] not in excluded_urls]
    return sub_urls

def scrape_images(sub_pages, save_dir):
    for sub_page in sub_pages: 
        response = requests.get(sub_page)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img')
        for img in image_tags:
            img_url = img.get('data-src') or img.get('src')
            if img_url and 'CopyofSquircleLogosmaller' not in img_url:
                image_name = img_url.split('/')[-1].split('.')[0]
                image_name = ''.join(e for e in image_name if e.isalnum() or e == ' ')
                image_path = os.path.join(save_dir, f"{image_name}.jpg")
                if not os.path.exists(image_path):  # Avoid re-downloading existing images
                    with open(image_path, 'wb') as f:
                        f.write(requests.get(img_url).content)
                    print(f"Image '{image_name}' saved as '{image_path}'")

def main():
    main_menu_url = 'https://www.kungfutea.com/menu'
    save_directory = "/workspaces/boba-tea-calories-calculator/data/pic/kungfu"  
    # Specify your save directory
    sub_pages = find_subpages(main_menu_url)
    scrape_images(sub_pages, save_directory)

if __name__ == "__main__":
    main()
