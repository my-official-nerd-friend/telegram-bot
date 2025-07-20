import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def parse_link(link):
    req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read()
    html = data.decode("utf8")
    
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find("span", id="productTitle").getText(strip=True)
    price = soup.find("span", class_="a-offscreen").getText(strip=True)
    image_url = soup.find("img", id="landingImage")["src"]
        
    print(f"\n{name}\n{price}\n{image_url}")
    return {
        "name": name,
        "price": price,
        "image_url": image_url
    } 
def get_amazon_affiliate_url(link, my_tag):
        parsed = urlparse(link)
        qs = parse_qs(parsed.query)
        qs['tag'] = my_tag
        new_q = urlencode(qs, doseq=True)
        return urlunparse(parsed._replace(query=new_q)).strip()  