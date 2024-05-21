import re
import csv
from bs4 import BeautifulSoup
import os

# File path to the file you want to delete
file_path = 'prices.csv'

# Check if file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")

# Function to extract numbers from a string and join them without commas
def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    return ''.join(numbers)  # Join the numbers into a single string without commas

# List of HTML files to read
html_files = ['nettimoto_page_1.html', 'nettimoto_page_2.html', 'nettimoto_page_3.html', 'nettimoto_page_4.html']

# Open the CSV file to write the prices
with open('prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Writing header

    # Loop through each HTML file
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        elements = soup.find_all(class_='list-card__info_price__main')

        # Extract numbers, clean them, and write to CSV
        for element in elements:
            price = extract_numbers(element.get_text())
            if price:
                writer.writerow([price])  # Writing the cleaned price to CSV

print('Data has been saved to "prices.csv".')
