import ganji_url, page_parsing
from multiprocessing import pool
import requests

print ganji_url.link_list

if __name__ == '__main__':

    for i in ganji_url.link_list:
        print i