import re
import csv
from bs4 import BeautifulSoup
import os

# Function to read the number of files to process from data.txt
def get_number_from_file(filename='data.txt'):
    try:
        with open(filename, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return 0
    except ValueError:
        print("Error: The file does not contain a valid integer.")
        return 0

# Function to extract numbers from a string and join them without commas
def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    return ''.join(numbers)  # Join the numbers into a single string without commas

# Read the number from data.txt
num_files = get_number_from_file()

# Generate the list of HTML files to read
html_files = [f'nettimoto_page_{i}.html' for i in range(1, num_files + 1)]

# File path to the file you want to delete
file_path = 'prices.csv'

# Check if file exists and delete if it does
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")

# Open the CSV file to write the prices
with open('prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Writing header

    # Loop through each HTML file
    for html_file in html_files:
        if os.path.exists(html_file):
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            elements = soup.find_all(class_='list-card__info_price__main')

            # Extract numbers, clean them, and write to CSV
            for element in elements:
                price = extract_numbers(element.get_text())
                if price:
                    writer.writerow([price])  # Writing the cleaned price to CSV
        else:
            print(f"Warning: The file {html_file} does not exist.")

print('Data has been saved to "prices.csv".')
