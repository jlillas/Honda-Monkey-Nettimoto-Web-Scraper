from seleniumbase import Driver
import time
import random

# Define the filename
filename = 'data.txt'

# Open and read the contents of the file
with open(filename, 'r') as file:
    page = int(file.read())

# Print the content (for verification)
print(page)


def scrape_page(base_url, page_number):
    # Initialize the driver
    print("Starting the browser...")
    driver = Driver(browser="chrome")
    
    try:
        # Construct the URL with the current page number
        url = f'{base_url}?page={page_number}'
        
        # Open the page
        print(f"Opening page {page_number}...")
        driver.get(url)
        
        # Add a random delay to simulate human-like behavior
        delay = random.uniform(2, 4)
        print(f"Waiting for {delay} seconds...")
        time.sleep(delay)
        
        # Retrieve the complete HTML code of the page
        html_source = driver.page_source
        
        # Save the HTML code to a file
        file_path = f"nettimoto_page_{page_number}.html"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_source)
            print(f"The HTML code for page {page_number} has been saved to {file_path}")
    
    finally:
        # Quit the browser
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    # Base URL for the pages
    base_url = 'https://www.nettimoto.com/honda/monkey'
    
    # Loop through page numbers (saving pages 1 to 3 in this example)
    for page_number in range(1, (page + 1)):
        scrape_page(base_url, page_number)
