import os

def get_nmap(options, ip):
    print('getting nmap: ' + options + " " + ip)
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    print('results: ' + results)
    return results
