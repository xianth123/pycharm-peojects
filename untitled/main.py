from multiprocessing import Pool
import requests
from channel import channel_list2
from page_persing import get_link_from

def get_all_links_from(channel):
    for num in range(1, 101):
        get_link_from(channel, num)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from, channel_list2)
    requests.adapters.DEFAULT_RETRIES = 5
    print  'jieshula!!!'


