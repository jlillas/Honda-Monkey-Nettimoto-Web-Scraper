import re
from bs4 import BeautifulSoup
import os

# File path to the file you want to delete
file_path = 'data.txt'

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
html_files = ['nettimoto_page_1.html']

# Check if the HTML file exists
if not os.path.exists('nettimoto_page_1.html'):
    with open('data.txt', mode='w', newline='') as file:
        file.write('1\n')
    print('The HTML file "nettimoto_page_1.html" does not exist. Wrote "1" to "data.txt".')
else:
    # Open the text file to write the pages
    with open('data.txt', mode='w', newline='') as file:
        # Loop through each HTML file
        for html_file in html_files:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            elements = soup.find_all(class_='totalPage')

            # Extract numbers, clean them, and write to the text file
            for element in elements:
                page = extract_numbers(element.get_text())
                if page:
                    file.write(f'{page}\n')  # Writing the cleaned page to text file

    print('Data has been saved to "data.txt".')
