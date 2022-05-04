from bs4 import BeautifulSoup

def extract(html,extract_all=False):
    soup = BeautifulSoup(html,'html.parser')

    links = []
    for a in soup.find_all('a',href=True):
        links.append(a['href'])

    action_links = []
    for form in soup.find_all('form'):
        if form['action']:
            action_links.append(form['action'])

    assets = []
    scripts = []

    if extract_all:
        for link in soup.find_all('link',href=True):
            assets.append(link['href'])
        for script in soup.find_all('script',src=True):
            scripts.append(script['src'])
    
    return links, action_links ,assets, scripts