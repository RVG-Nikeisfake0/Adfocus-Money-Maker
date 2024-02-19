import requests

def validate(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return 'https://' + url

def create(api_key, a_url):
    key = str(api_key)
    b_url = str(a_url)
    url = validate(b_url)
    return requests.post(f'http://adfoc.us/api/?key={key}&url={url}')