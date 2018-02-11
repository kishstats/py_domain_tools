import os
from datetime import datetime
import argparse
from domain_name import get_domain_name
from ip_address import get_ip_address
from nmap import get_nmap
from robots_txt import get_robots_txt
from whois import get_whois

DIR = 'files'
CURRENT_DATE = datetime.now()


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def save_report(name, url, domain_name, ip_address, nmap, robots_txt, whois):
    project_dir = DIR + '/' + name + '_' + CURRENT_DATE.strftime('%Y-%m-%d')
    create_dir_if_not_exists(project_dir)
    write_file(project_dir + '/full_url.txt', url + "\n" + ip_address)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


def gather_info(url, name=None):
    domain_name = get_domain_name(url)

    replace_chars = ['.', '-']
    if not name:
        name = domain_name
        for ch in replace_chars:
            name = name.replace(ch, '_')

    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)

    save_report(name, url, domain_name, ip_address, nmap, robots_txt, whois)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get lookup URL')
    parser.add_argument('-u', '--url', help='URL', required=True)
    parser.add_argument('-n', '--name', help='Name')
    args = parser.parse_args()

    create_dir_if_not_exists(DIR)

    gather_info(args.url, args.name)
