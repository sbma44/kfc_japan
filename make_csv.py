import json
import csv
import os

if __name__ == '__main__':
    with open('out.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for f in os.listdir('./json'):
            with open('./json/{}'.format(f)) as jsonfile:
                j = json.load(jsonfile)                
                
                for shop in j['shop_list']:
                    row = [
                        shop['shop_id'],
                        shop['name'],
                        shop['longitude'],
                        shop['latitude'],
                        shop['prefecture'],
                        shop['city'],
                        shop['address'],
                        shop['zip_code']                    
                    ]
                    map(lambda x: x.strip(), row)

                    writer.writerow(row)