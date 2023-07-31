import requests
from bs4 import BeautifulSoup


def email_search(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.body
    for strings in tag.stripped_strings:
        print(strings)


if __name__ == "__main__":
    email_search('http://www.trailcourts.ca/boxing-club.html')