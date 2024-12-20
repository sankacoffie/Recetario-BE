import requests
from bs4 import BeautifulSoup

def scrape_recipe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').text
    ingredients = [li.text for li in soup.select('.ingredients li')]
    steps = [p.text for p in soup.select('.steps p')]

    return {
        'title': title,
        'ingredients': ingredients,
        'steps': steps
    }
