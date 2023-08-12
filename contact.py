import requests
from bs4 import BeautifulSoup

def at_check(words):

    words = words.split(' ')
    for i in words:
        if '@' in i:
            #print(i)
            return i

def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)

    return de

def email_search(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.body
    try:
        for string in tag.stripped_strings:
            email = at_check(string)
            if email is not None:
                return email
    except AttributeError:
        return "@"
    

def clean_email(email_dict):
    email_keys_list = list(email_dict.keys())
    for i in email_keys_list:
        if i is None or i.startswith("@") or i.endswith("@") or "." not in i:
            del email_dict[i]

    return email_dict



#if __name__ == "__main__":
   # email_search('https://www.accesswire.com/546295/Theramed-Provides-Update-on-New-Sales-Channel-for-Nevada-Facility')