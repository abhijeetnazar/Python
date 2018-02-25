#!/usr/bin/env python
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
import urllib.request
import json


def getMovieTitles(substr):
    # parse strings: 'ip_prefix' and 'region'
    # for i in range(len(j['prefixes'])):
    #	print("{0}\t{1}".format(j['prefixes'][i]['ip_prefix'], j['prefixes'][i]['region']))
    res = urllib.request.urlopen('https://jsonmock.hackerrank.com/api/movies/search/?Title='+substr)
    res_body = res.read()
    j = json.loads(res_body.decode("utf-8"))
    counter = 0
    count = j['total_pages']+1
    array = []
    for i in range(count):
        res = urllib.request.urlopen(
            'https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page='+str(i))
        res_body = res.read()
        k = json.loads(res_body.decode("utf-8"))
        for item in k['data']:
            array.append(item['Title'])
    return sorted(array)


res = getMovieTitles('spiderman')
for res_cur in res:
    print(str(res_cur) + "\n")
