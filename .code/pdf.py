import PyPDF2

# Open the PDF file
with open('data/downloaded data/2024 Kung Fu Tea Product Ingredient Information - Website.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)  # Updated to use PdfReader instead of PdfFileReader
    
    # If the PDF is encrypted, attempt to decrypt it
    if reader.is_encrypted:
        reader.decrypt('password')  # Replace 'password' with the actual password if needed

    # Get text from each page
    text = ""
    for page in reader.pages:
        text += page.extract_text()

print(text)


print(text)

import csv

# Sample data extracted from the PDF
data = [
    {
        "Category": "Classic",
        "Drink Name": "Kung Fu Black Tea",
        "Base": "Black Tea – Black Tea, Bergamot Flavor",
        "Additives": "Cane Sugar Syrup – Fructose, Glucose, Sucrose, Water"
    }
    # You can add more drink entries here in the same format
]

# Specify the filename to save the CSV
filename = 'data/csv/kungfu_drink_additives.csv'

# Writing to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Category", "Drink Name", "Base", "Additives"])
    writer.writeheader()  # Writing the headers
    writer.writerows(data)  # Writing the data

print(f'Data successfully saved to {filename}')
