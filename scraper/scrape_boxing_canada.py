import requests
from bs4 import BeautifulSoup
import contact
import sel

def get_google_search_query(query):
    base_url = "https://www.google.com/search?q="
    params = {"q": query}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(base_url, headers=headers, params=params)
    return res.text  # Return the HTML content as text, not the full response object


def get_google_search_url(url):
    base_url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = requests.get(base_url, headers=headers)
    return res.text  # Return the HTML content as text, not the full response object


def soup_process(html, current_url, recursive, email_track):
    #email_track = dict()
    if recursive is False:
        return email_track.update({})
    soup = BeautifulSoup(html, 'html.parser')
    #links = soup.find_all('a', href=True)  # Find anchor tags with the 'href' attribute
    links = soup.find_all('a', href=True)

    for link in links:
        #print(link['href'])  # Access the 'href' attribute of each anchor tag
        if link['href'].startswith('https://'):
            #link_list.append(link['href'])
            email = contact.email_search(link['href'])
            if email_track.get(email) is None:
                email_track[email] = link['href']
    next_url = sel.next_page(current_url)
    if next_url is None:
        return email_track.update({})
    if current_url == next_url:
        return email_track.update(soup_process(get_google_search_url(next_url), next_url, False, email_track))
    else:
        return email_track.update(soup_process(get_google_search_url(next_url), next_url, True, email_track))

    
            


def user_input_query(inquire):
    html = get_google_search_query(inquire)
    email_track = dict()
    email_dict = soup_process(html, inquire, True, email_track)
    print(email_dict)

def user_input_url(url):
    html = get_google_search_query(url)
    email_track = dict()
    email_dict = soup_process(html, url, True, email_track)
    print(email_dict)




if __name__ == "__main__":
    
    user_input_url("https://www.google.com/search?q=boxing+clothes&sca_esv=555852541&sxsrf=AB5stBgb8S4iiDOWZs-78WGKMa5PQycIsQ:1691749677871&ei=LQ3WZJ3tNKjf0PEP2JqUwAY&start=120&sa=N&ved=2ahUKEwjdt-TUstSAAxWoLzQIHVgNBWg4tAEQ8tMDegQIIxAG&biw=1920&bih=923&dpr=1")
