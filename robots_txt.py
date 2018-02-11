import requests

def get_robots_txt(url):
    if not url.endswith('/'):
        url += '/'

    robots_txt_info = ''
    try:
        response = requests.get(url + "robots.txt")
        robots_txt_info = response.text
    except Exception as e:
        print('Error fetching robots.txt')

    return robots_txt_info
