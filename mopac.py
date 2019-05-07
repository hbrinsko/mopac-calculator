import argparse
import datetime
import json
import random
import sys
import time

import pytz
import requests


def get_mopac_data(when):
    url = 'https://mopac-fare.mroms.us/HistoricalFare/ViewHistoricalFare'
    USER_AGENTS = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
                   'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C202 Safari/604.1',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko']
    headers = {
        'Origin': 'https://www.mobilityauthority.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': random.choice(USER_AGENTS),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.mobilityauthority.com/pay-your-toll/current-mopac-rates',
        'Connection': 'keep-alive'
    }
    payload = when.strftime('starttime=%m%%2F%d%%2F%Y+%H%%3A%M')
    r = requests.post(url, headers=headers, data=payload)
    try:
        return r.json()
    except:
        print(r.status_code)
        print(r.headers)
        print(r.text)
        return {}


def parse_mopac_data(data):
    result = {}
    for e in data:
        name = e.get('tollingPointName').replace('LP1X ', '').lower()
        result[name] = e.get('tripRate')
    return result


def get_specific_toll(route):
    now = datetime.datetime.now(pytz.timezone('America/Chicago'))
    raw_data = get_mopac_data(now)
    if not raw_data:
        print("Didn't get json data, quitting...")
        sys.exit(1)

    nice_data = parse_mopac_data(raw_data)
    route = route.lower()
    print('${:,.2f}'.format(nice_data[route]))
    return '${:,.2f}'.format(nice_data[route])


if __name__ == '__main__':
    get_specific_toll('sb: parmer to 5th/cvz')
