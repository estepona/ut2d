import requests

from bs4 import BeautifulSoup as BS

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

# TODO: more
TZ_INFO = {
    'EST': 'GMT-5'
}

def scrap_google(city: str) -> str:
    city_fmt = city.lstrip().rstrip().replace(' ', '+')

    base_url = 'https://www.google.com/search?q='
    full_url = base_url + city_fmt + '+time'

    r = requests.get(full_url, headers={'User-Agent': USER_AGENT})
    # TODO: return the status_code to determine if using another search engine or website?
    # print(r.status_code)
    
    # TODO: if error, use another engine
    soup = BS(r.content, 'html.parser')
    tz = soup.select('span[class="KfQeJ"]')[1].text
    tz_fmt = tz.lstrip().rstrip()[1:-1]
    
    return TZ_INFO[tz_fmt]
