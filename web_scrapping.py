from bs4 import BeautifulSoup
import requests

sites = [
    {'site': 'Le Parisien', 'url': 'https://www.leparisien.fr/', 'class': 'lp-card-article__link lp-f-subtitle-04'},
    {'site': 'Le Figaro', 'url': 'https://www.lefigaro.fr/', 'class': 'fig-ranking-profile-headline'}
]

for site_info in sites:
    url = site_info['url']
    class_name = site_info['class']

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all(class_=class_name):
        print(f"{site_info['site']} | {link.text}")
