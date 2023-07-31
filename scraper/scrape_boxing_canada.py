import requests
from bs4 import BeautifulSoup

def get_google_search_links(query):
    base_url = "https://www.google.com/search?q=boxing+club&oq=boxing&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyDwgCEAAYQxiDARixAxiKBTIMCAMQABhDGLEDGIoFMgYIBBBFGDwyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgxMjg4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
    params = {"q": query}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(base_url, headers=headers)
    return res.text  # Return the HTML content as text, not the full response object

inquire = input("Search: ")
html = get_google_search_links(inquire)
link_list = list()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', href=True)  # Find anchor tags with the 'href' attribute

for link in links:
    #print(link['href'])  # Access the 'href' attribute of each anchor tag
    if link['href'].startswith('https://'):
        link_list.append(link['href'])

for i in link_list:
    print(i)
