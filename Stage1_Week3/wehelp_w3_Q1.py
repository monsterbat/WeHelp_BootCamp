"""
WeHelp BootCamp Assignemt - Week 3  Task 1
Purpose: Analysis json data than choose the data we want
Release date: 2022/10/05
Update: 2022/10/08: remove before xpostDate 2015 data
Authored by SC Siao
"""

import ssl
ssl._create_default_https_context=ssl._create_unverified_context
import urllib.request as request
import json
import csv
import pandas as pd

# read urlsource code
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(url) as response:
    data=json.load(response)

attraction_list=data["result"]["results"]
# print(attraction_list)


# find first picture : Use .jpg str as breakpoint to find first url
# option to upgrade : filter world
def firstPic_filter(data):
    firstPic_url=""
    filter_word_1=".jpg"
    filter_word_2=".JPG"
    for firstPic_url_bit in data:
        firstPic_url=firstPic_url+firstPic_url_bit
        if filter_word_1 in firstPic_url:
            break
        if filter_word_2 in firstPic_url:
            break
    return firstPic_url

def remove_TPC(data):
    data=data.replace("臺北市  ","")
    address=""
    word_count=0
    for data_bit in data:
        word_count=word_count+1
        # what if the third little isn't “區”？
        if word_count<4:
            address=address+data_bit
    return address
def xpostDate_filter(data):
    xpostDate_year=int(data[0:4])
    return xpostDate_year

with open("data.csv", mode="w",encoding="utf-8") as dataFrame:
    writer = csv.writer(dataFrame)  
    writer.writerow(["景點名稱","區域","經度","緯度","第一張圖檔網址"])          
    for attraction in attraction_list:
        if xpostDate_filter(attraction["xpostDate"])>=2015:
            dataFrame=[
            attraction["stitle"],
            remove_TPC(attraction["address"]),
            attraction["longitude"],
            attraction["latitude"],
            firstPic_filter(attraction["file"])
            ]
            # print(xpostDate_filter(attraction["xpostDate"]))
            writer.writerow(dataFrame)