import requests
from bs4 import BeautifulSoup

def at_check(words):

    words = words.split(' ')
    for i in words:
        if '@' in i:
            return i


def email_search(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.body
    for string in tag.stripped_strings:
        email = at_check(string)
        if email is not None:
            print(email)


if __name__ == "__main__":
    email_search('https://www.10thstreetboxing.com/')