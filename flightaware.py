#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__version__ = "0.2.0"
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
import requests
from tabulate import tabulate

BASE = "https://flightaware.com/live/flight"
HEADERS = ["Time", "Latitude", "Longitude", "Altitude (ft/100)", "Ground Speed (mph)"]

if __name__ == "__main__":
    flight = sys.argv[1].strip()
    content = requests.get(BASE + "/" + flight, allow_redirects=True).text
    head = "<script>var trackpollBootstrap = "
    tail = ";</script>"
    
    for line in content.split("\n"):
        if head in line:
            data = line.replace(head, "").replace(tail, "")
    
    tab = []
    data = json.loads(data)
    for key in data['flights']:
        flight_id = key
        break
    
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
        
    print(tabulate(tab[-10:], headers=HEADERS))
