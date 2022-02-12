"""
Salesman's Travel
https://www.codewars.com/kata/56af1a20509ce5b9b000001e
"""


def travel(r, zipcode):
    results = ''
    streets = []
    ad_nums = []
    r = r.split(',')
    for ad in r:
        ad = ad.split(' ')
        if ' '.join(ad[-2:]) == zipcode:
            if streets:
                streets += ','
                streets += ad[1:-2]
                ad_nums += f',{ad[0]}'
            else:
                streets += ad[1:-2]
                ad_nums += ad[0]
    results += f'{zipcode}:{" ".join(streets)}/{"".join(ad_nums)}'
    return results.replace(' , ', ',')
