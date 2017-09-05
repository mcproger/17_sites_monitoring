import requests
import os
import argparse


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
    pass


if __name__ == '__main__':
    args = get_argparser()
    urls_for_check = load_urls4check(args.path).split()
    for url in urls_for_check:
        print(is_server_respond_with_200(url))