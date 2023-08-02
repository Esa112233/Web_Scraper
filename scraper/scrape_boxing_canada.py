import requests
from bs4 import BeautifulSoup
import contact

def get_google_search_links(query):
    base_url = "https://www.google.com/search?q=motor+bike+leather+jackets&sxsrf=AB5stBijF4Tz0CHyEa1U1YyUnplWET0Wcw%3A1690940453998&ei=JbTJZNavPJKr0PEPnpyosA8&ved=0ahUKEwiW1uKI7LyAAxWSFTQIHR4OCvYQ4dUDCBA&uact=5&oq=motor+bike+leather+jackets&gs_lp=Egxnd3Mtd2l6LXNlcnAiGm1vdG9yIGJpa2UgbGVhdGhlciBqYWNrZXRzMgUQABiABDIIEAAYFhgeGAoyCxAAGBYYHhjxBBgKMggQABiKBRiGAzIIEAAYigUYhgMyCBAAGIoFGIYDSINVUJwYWMpScAp4AZABAZgB3QGgAfoUqgEGMjMuNS4xuAEDyAEA-AEBqAIUwgIHECMY6gIYJ8ICDRAuGMcBGNEDGOoCGCfCAhAQABiKBRjqAhi0AhhD2AEBwgIEECMYJ8ICBxAjGIoFGCfCAgcQABiKBRhDwgILEAAYgAQYsQMYgwHCAgsQLhiABBixAxiDAcICCxAAGIoFGLEDGIMBwgIKEC4YigUYsQMYQ8ICChAAGIoFGLEDGEPCAgUQLhiABMICDhAuGIAEGLEDGIMBGOUEwgIIEAAYgAQYsQPCAggQABiABBjJA8ICCBAAGIoFGJIDwgIIEAAYigUYsQPCAgcQABiABBgKwgIGEAAYFhgewgIIEAAYFhgeGA_CAgoQABgWGB4YDxgK4gMEGAAgQYgGAboGBggBEAEYAQ&sclient=gws-wiz-serp"
    params = {"q": query}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(base_url, headers=headers)
    return res.text  # Return the HTML content as text, not the full response object

def link_process(link):

    
    return []

inquire = input("Search: ")
html = get_google_search_links(inquire)
link_list = list()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', href=True)  # Find anchor tags with the 'href' attribute

for link in links:
    #print(link['href'])  # Access the 'href' attribute of each anchor tag
    if link['href'].startswith('https://'):
        link_list.append(link['href'])
        
        contact.email_search(link['href'])



print(link_list)
