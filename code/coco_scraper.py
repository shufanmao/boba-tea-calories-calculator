import requests
from bs4 import BeautifulSoup
import csv
import re
import operator

# Function to customize the title case of drink names
def custom_title(s):
    words = s.split()
    return ' '.join([word.title() if word.lower() != "qq" else "QQ" for word in words])

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

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
# Prepare to write to a CSV file
csv_file_path = '/workspaces/boba-tea-calories-calculator/data/csv/coco_drinks_calories.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Drink Name', 'Small Size Drink Calories', 'Medium Size Drink Calories', 'Big Size Drink Calories'])

# Now, read the file and sort the data
with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    data = sorted(reader, key=operator.itemgetter(0))  # Sort by the first column

# Finally, write the sorted data back to the file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Drink Name', 'Small Size Drink Calories', 'Medium Size Drink Calories', 'Big Size Drink Calories'])  # Write the header
    writer.writerows(data)  # Write the sorted data

    for url in urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            sub_page_name = url.split('/')[-1]  # Extract sub-page name from URL

            drink_blocks = soup.find_all('div', class_='sqs-block-content')
            for block in drink_blocks:
                drink_name = None
                small_calories = ''
                medium_calories = ''
                big_calories = ''

                paragraphs = block.find_all('p')
                for p in paragraphs:
                    if p.strong:
                        drink_name = custom_title(p.strong.text.replace('&', '').strip())
                    if 'calories' in p.text.lower():
                        calorie_info = p.text.strip()
                        matches = re.findall(r'\d+', calorie_info)
                        if len(matches) == 1:
                            medium_calories = matches[0]  # Assign to medium only if one number is found
                        elif len(matches) == 2:
                            small_calories, big_calories = matches  # Normal assignment if two numbers are found
                        # If no valid matches or more than expected, do not assign any value (already initialized as empty strings)

                if drink_name:
                    writer.writerow([sub_page_name, drink_name, small_calories, medium_calories, big_calories])
        else:
            print(f"Failed to retrieve {url} with status code {response.status_code}")


# Predefined drink entries to add manually
predefined_drinks = [
    ['seasonal', 'Hoji Milk Tea', '368', '502'],
    ['seasonal', 'Hoji Cha', '104', '154'],
    ['seasonal', 'Peach Honey Jello', '460', '640'],
    ['milk tea', '2 Ladies Milk Tea', '254', '460'],
    ['milk tea', '3 Guys Milk Tea', '309', '545']
]

# After scraping and writing the scraped data to the CSV, add the predefined entries
with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for drink in predefined_drinks:
        writer.writerow(drink)
