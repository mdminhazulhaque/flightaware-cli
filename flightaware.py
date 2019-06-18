#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__version__ = "0.1.0"
__license__ = "GPLv3"

"""
Copyright (c) 2018 Md. Minhazul Haque
This file is part of mdminhazulhaque/bd-mrp-api
(see https://github.com/mdminhazulhaque/banglalionwimaxapi).
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import json
from datetime import datetime
import sys
import os
import requests
from tabulate import tabulate

BASE = "https://flightaware.com/live/flight/"
HEADERS = ["time", "lat", "long", "alt", "gs"]
LIMIT = int(os.environ['LIMIT']) if 'LIMIT' in os.environ else 10

if __name__ == "__main__":
    try:
        flight = sys.argv[1].strip()
    except:
        exit("Flight number required")
    
    try:
        response = requests.get(BASE + flight)
    except:
        exit("Request cannot be fetched")
    
    # If 301, then get redirected flight name
    if response.status_code == 301:
        newurl = response.headers['Location']
        flight = newurl.split("/")[-1]
        response = requests.get(BASE + flight)
    
    # extract data from script tag in html
    head = "<script>var trackpollBootstrap = "
    tail = ";</script>"
    
    for line in response.text.split("\n"):
        if head in line:
            data = line.replace(head, "").replace(tail, "")
            break
    
    tab = []
    try:
        data = json.loads(data)
    except:
        exit("Flight data not found")
                
    for key in data['flights']:
        flight_id = key
        break
    
    if "INVALID" in flight_id:
        exit("Invalid flight number")
    
    for track in data['flights'][flight_id]['track']:
        ts = int(track['timestamp'])
        timestamp = datetime.fromtimestamp(ts)\
            .strftime('%Y-%m-%d %H:%M:%S')
        row = [
            timestamp,
            track['coord'][0],
            track['coord'][1],
            track['alt'],
            track['gs']
        ]
        tab.append(row)
    
    if len(tab) < LIMIT:
        print(tabulate(tab, headers=HEADERS))
    else:
        print(tabulate(tab[-LIMIT:], headers=HEADERS))
