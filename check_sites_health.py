import requests
import os
import argparse
import whois
from datetime import datetime


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', type=str, help='Path to file with urls for checking')
    args = parser.parse_args()
    return args


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as file_handler:
        urls_for_check = file_handler.read()
        return urls_for_check


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code == 200


def get_domain_expiration_date(domain_name):
    domain = whois.whois(domain_name)
    domain_expiration_timedelta = domain.expiration_date[0] - datetime.now()
    return domain_expiration_timedelta.days >= 30


def get_site_status(url):
    if is_server_respond_with_200(url) and get_domain_expiration_date(url):
        site_status = '{url} - {status_code}; {domain_expiration_date}'.format(
            url=url, status_code='status code is 200', domain_expiration_date='domain expiration date 1 month or more')
        return site_status


if __name__ == '__main__':
    args = get_argparser()
    urls_for_check = load_urls4check(args.path).split()
    for url in urls_for_check:
        print(get_site_status(url))
