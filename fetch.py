import re
import csv
import json
import time
import requests

def main():  
    for kencode in range(1, 48):
        url = 'http://www.kfc.co.jp/api/?p=shop.search&kencode=01&t=attr_con&keyword_type=attr_con&pref={kencode:02d}&limit=9999&_={time:d}'.format(kencode=kencode, time=int(time.time()))        
        print(url)
        resp = requests.get(url)
        with open('json/{}.json'.format(kencode), 'w') as f:
            f.write(resp.text)

if __name__ == '__main__':
    main()
