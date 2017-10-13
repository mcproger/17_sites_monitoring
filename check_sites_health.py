import requests
import os
import argparse
import whois
from datetime import datetime


def get_console_arguments():
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
    return response.ok


def is_domain_expiration_date_valid(domain_name, days_in_month):
    domain = whois.whois(domain_name)
    if isinstance(domain.expiration_date, list):
        domain_expiration_date = domain.expiration_date[0]
    else:
        domain_expiration_date = domain.expiration_date
    domain_expiration_timedelta = domain_expiration_date - datetime.now()
    return domain_expiration_timedelta.days >= days_in_month


def format_site_status_output(url):
    site_status_output = '{0} - {1}, {2}'.format(
        url,
        'status code is 200',
        'domain expiration date 1 month or more',
    )
    return site_status_output


if __name__ == '__main__':
    args = get_console_arguments()
    urls_for_check = load_urls4check(args.path).split()
    days_in_month = 30
    for url in urls_for_check:
        if is_server_respond_with_200(url) and is_domain_expiration_date_valid(url, days_in_month):
            print(format_site_status_output(url))
