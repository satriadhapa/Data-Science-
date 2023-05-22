import csv
import requests
from bs4 import BeautifulSoup

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
page_count = 10  # Set the total number of pages to scrape

# Create and open a CSV file in write mode
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write header row
    writer.writerow(['Title', 'Price', 'Rating', 'Genre', 'Link'])

    # Iterate over each page
    for page in range(1, page_count + 1):
        url = base_url.format(page)
        response = requests.get(url)
        html_content = response.content.decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')

        books = soup.find_all('article', class_='product_pod')

        # Write data rows
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip('£')
            rating = book.find('p', class_='star-rating')['class'][1]
            genre = book.find('p', class_='genre').text.strip()
            link = url.replace('/catalogue/page-{}.html', '') + book.h3.a['href']
            writer.writerow([title, price, rating, genre, link])
