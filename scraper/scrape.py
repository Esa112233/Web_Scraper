import requests
from bs4 import BeautifulSoup

def get_google_search_links(query):
    base_url = "https://www.google.com/search"
    params = {"q": query}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(base_url, params=params, headers=headers)
    return res

inquire = input("Search: ")
html = get_google_search_links(inquire)

soup = BeautifulSoup(html.text, 'html.parser')
link = soup.find_all('a', href=True)
for i in link:
    print(i['href'])


