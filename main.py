import urllib
import requests
from pprint import pprint

# response = requests.get('https://jsonbin.io/b/59d0f30408be13271f7df29c').json()
# APP_ACCESS_TOKEN = response['access_token']
APP_ACCESS_TOKEN= '1683591102.e76c52f.01bc1307f56044c693d2f4e7d6ae3d88'
# APP_ACCESS_TOKEN is the access token we need to access our api
BASE_URL = 'https://api.instagram.com/v1/'


# BASE_URL is the url which will be the base of the urls and will exist commonly

# pprint (response)

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET REQUEST URL: %s ' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        # code 200 means getting good response
        pprint(user_info['data'])
        if 'data' in user_info:
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['count']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['count']['follows'])
            print 'No of posts: %s' % (user_info['data']['count']['media'])
        else:
            print 'User doesn\'t exist'
    else:
        print 'Mila nahi tera status code....sorry main ni manta koi aur code ko'

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if 'data' in user_info:
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Mila nahi tera status code....sorry main ni manta koi aur code ko'


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Mila nahi tera status code....sorry main ni manta koi aur code ko'
        exit()


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']) > 0:
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your Image has been downloaded'
            return own_media['data'][0]['id']
        else:
            print 'Post to hai hi nahi....sorry pr chiz hogi thi milegi'
    else:
        print 'Mila nahi tera status code....sorry main ni manta koi aur code ko'
        return None


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET REQUEST URL: %s ' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']) > 0:
            return user_media['data'][0]['id']
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
        else:
            print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
        return None

def start_bot():
    print '/n'
    print 'Aao chlao ye instabot '
    print 'Kya krna chahoge ap apne instagram se'
    print '1. Get your own details'
    print "2.Get details of a user by username\n"
    print "3.Get your own recent post\n"
    print "4.Get the recent post of a user by username\n"
    print "5.Exit"

    select= input('Enter your option ')
    if select== 1:
        self_info()
    elif select==2:
        insta_username=raw_input('Apne us dost ka username to bta do ')
        get_user_info(insta_username)
    elif select==3:
        get_own_post()
    elif select==4:
        insta_username = raw_input("Enter the username of the user: ")
        get_user_post(insta_username)
    elif select == 5:
        exit()
    else:
            print "wrong choice"

start_bot()
