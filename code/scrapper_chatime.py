import requests
from bs4 import BeautifulSoup
import csv
import json
import logging
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Specific URL for Matcha Latte Milk Tea
matcha_url = "https://chatime.com/drinks/match-latte-milk-tea"

# Base URL for other drinks, if needed
base_url = "https://chatime.com/drinks/"

# Path for CSV file
csv_file_path ='/workspaces/boba-tea-calories-calculator/data/csv/chatime_drinks_calories.csv'

# Function to fetch and parse drink data
def fetch_drink_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script_content = soup.find('script', string=lambda t: t and 'window.__remixContext' in t)
        if script_content:
            json_text = script_content.string.split('=', 1)[1].strip()
            json_text = json_text.rsplit(';', 1)[0].strip()  # Remove trailing JS code
            json_data = json.loads(json_text)
            nutrition_info = json_data['state']['loaderData']['routes/drinks_.$slug'].get('nutrition', {})
            return {
                "small": nutrition_info.get('regularCalories', "Not Available"),
                "medium": nutrition_info.get('mediumCalories', "Not Available"),
                "large": nutrition_info.get('largeCalories', "Not Available")
            }
    else:
        logging.error(f"Failed to retrieve {url} with status code {response.status_code}")
    return None

# Fetch data for Matcha Latte Milk Tea
matcha_data = fetch_drink_data(matcha_url)

# Load the CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Find the row for Matcha Latte Milk Tea (assuming the name is exact) and update it
if matcha_data:
    df.loc[df['Drink Name'].str.lower() == 'matcha latte milk tea', ['Small Size Calories', 'Medium Size Calories', 'Big Size Calories']] = matcha_data['small'], matcha_data['medium'], matcha_data['large']

# Save the updated DataFrame back to the CSV
df.to_csv(csv_file_path, index=False)
logging.info("CSV file updated successfully.")
