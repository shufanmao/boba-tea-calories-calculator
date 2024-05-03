import os
import pandas as pd
from fuzzywuzzy import process
import numpy as np

# Path to coco_drinks_calories.csv file
csv_file_path = '/workspaces/boba-tea-calories-calculator/data/csv/coco_drinks_calories.csv'

# Path to the folder containing images
image_folder_path = '/workspaces/boba-tea-calories-calculator/data/pic/coco'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Get the list of files in the image folder
image_files = os.listdir(image_folder_path)

# Initialize an empty list to store the match results
match_results = []

# Function to find matching image file for a given drink name using fuzzy matching
def find_matching_image_file(drink_name, image_files):
    # Try to find an exact match
    for file_name in image_files:
        if drink_name.lower() in file_name.lower():
            match_results.append(f"Exact match found for {drink_name}: {file_name}")
            return file_name
    # If no exact match, use fuzzy matching
    best_match, score = process.extractOne(drink_name, image_files)
    if score >= 80:
        match_results.append(f"Fuzzy match found for {drink_name}: {best_match} with a score of {score}")
        return best_match
    return None

# Apply the function to each drink name in the DataFrame
df['Matching File'] = df['Drink Name'].apply(lambda x: find_matching_image_file(x, image_files))

# Sort the match results
match_results.sort()

# Print the match results in order
for result in match_results:
    print(result)

# Create a set of all image files
all_image_files = set(image_files)

# Remove the matched image files from the set
for file_name in df['Matching File']:
    if pd.notnull(file_name):
        all_image_files.discard(file_name)

# Print the image files that have not been matched
for file_name in all_image_files:
    print(file_name)
# Apply the function to each drink name in the DataFrame
df['Matching File'] = df['Drink Name'].apply(lambda x: find_matching_image_file(x, image_files))

# Add matching image path to a new column
df['Path'] = df['Matching File'].apply(lambda x: os.path.join(image_folder_path, x) if pd.notnull(x) else np.nan)


# Save the DataFrame to a new CSV file with the header
df.to_csv('/workspaces/boba-tea-calories-calculator/data/csv/coco_output.csv', index=False)


# Upon checking based on print results, finish manual edits
df.loc[9, 'Matching File'] = 'Thai Tea.png'
df.loc[35, 'Matching File'] = 'Lemon Wintermelon.png'
df.loc[40, 'Matching File'] = 'Mango Slush.png'
df.loc[41, 'Matching File'] = 'Toro Slush.png'
df.loc[47, 'Matching File'] = 'Matcha Latte.png'
df.loc[53, 'Matching File'] = 'Green Tea.png'
df.loc[54, 'Matching File'] = 'Black Tea.png'
df.loc[55, 'Matching File'] = 'Wintermelon Tea.png'
df.loc[56, 'Matching File'] = 'Tapioca Milk.png'

# Update the 'Path' column
df['Path'] = df['Matching File'].apply(lambda x: os.path.join(image_folder_path, x) if pd.notnull(x) else np.nan)

# Save the DataFrame to a new CSV file with the header
df.to_csv('/workspaces/boba-tea-calories-calculator/data/csv/coco_output.csv', index=False)

## Create a set of all image files to double check if they are all included
all_image_files = set(image_files)

# Check if each file in 'Matching File' is in the set of all image files
df['File Exists'] = df['Matching File'].apply(lambda x: x in all_image_files if pd.notnull(x) else False)

# Print the rows where 'File Exists' is False
print(df[df['File Exists'] == False])