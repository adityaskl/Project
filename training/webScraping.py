# This is a template for web scraping using Python and not the actual code for the project.

import requests
from bs4 import BeautifulSoup

def scrape_flood_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the relevant HTML elements that contain the data
        articles = soup.find_all('article', class_='page-article')

        for article in articles:
            # Extract information like date and location
            title_element = article.find('h2', class_='entry-title')
            date_element = article.find('time', class_='entry-date')
            
            if title_element and date_element:
                title = title_element.a.text.strip()
                date = date_element.span.text.strip()
                
                # Extracting location from the title (assuming it's in the format "India – Location - Description")
                parts = title.split('–')
                if len(parts) > 1:
                    location = parts[1].strip()
                else:
                    location = "Unknown"

                # Print or process the extracted data as needed
                print(f"Date: {date}\nLocation: {location}\n{'='*50}\n")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    # URL of the website
    url = "https://floodlist.com/tag/india"
    scrape_flood_data(url)
