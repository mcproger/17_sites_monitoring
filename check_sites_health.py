import requests
import os


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as file_handler:
        urls_for_check = file_handler.read()
        return urls_for_check


def is_server_respond_with_200(url):
    pass


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    pass
