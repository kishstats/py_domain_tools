import os

def get_whois(url):
    print('getting whois: ' + url)
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    print('results: {}'.format(results))
    return results
