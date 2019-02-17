import urllib.request,json
from .models import Quote
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def configure_request(app):
    global api_key,base_url

def get_quotes():
    """Function to retrieve news quotes list from the News api"""

    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        id = get_quotes_response.get('id')
        author = get_quotes_response.get('author')
        quote = get_quotes_response.get('quote')

        quote_object = Quote(id ,author ,quote)
    return quote_object
    

