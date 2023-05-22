import csv
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://shopee.co.id/top_products?catId=ID_BITL0_59%3Atop_sold'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the webpage
title = soup.find('title').text.strip()

# Find the product items on the page
product_items = soup.find_all('div', class_='shopee-item-card')

# Create a CSV file and write the header row
csv_file = open('shopee_top_products.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Product Name', 'Product Price', 'Product Rating', 'Additional Title'])

# Extract information from each product item and write to the CSV file
for item in product_items:
    # Extract the product name
    product_name = item.find('div', class_='shopee-item-card__text-name').text.strip()

    # Extract the product price
    product_price = item.find('span', class_='shopee-item-card__current-price').text.strip()

    # Extract the product rating
    product_rating = item.find('div', class_='shopee-rating-stars__stars').get('style')
    product_rating = product_rating.replace('width:', '').replace('%', '').strip()

    # Extract the additional title (class "L6I7M8")
    additional_title = item.find('div', class_='L6I7M8').text.strip() if item.find('div', class_='L6I7M8') else ''

    # Write the extracted information to the CSV file
    csv_writer.writerow([title, product_name, product_price, product_rating, additional_title])

# Close the CSV file
csv_file.close()

print('Scraping completed. The data has been exported to shopee_top_products.csv.')
