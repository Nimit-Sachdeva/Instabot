import requests
from pprint import pprint

response = requests.get('https://jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN = response['access_token']
BASE_URL = 'https://api.instagram.com/v1/'


def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET REQUEST URL: ' % s % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code']==200:
        #REQUEST SUCCESSFUL
    else :
        print 'Mila nahi tera status code....sorry main ni manta koi aur code ko'