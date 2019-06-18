# flightaware-cli

Flight updates from FlightAware using commandline.

# Required Modules

* tabulate
* requests (default)
* sys (default)
* datetime (default)
* json (default)

## How To Run

```bash
python3 flightaware.py MH103 # Will redirect to MAS103 (Malaysian Airlines 103)
python3 flightaware.py AXM714 # AirAsia 714
```

## Preview

```
Time                   Latitude    Longitude    Altitude (ft/100)    Ground Speed (mph)
-------------------  ----------  -----------  -------------------  --------------------
2019-06-17 17:21:08     100.2         8.1438                  370                   468
2019-06-17 17:21:38     100.213       8.0803                  370                   468
2019-06-17 17:22:09     100.225       8.0167                  370                   468
2019-06-17 17:22:39     100.238       7.9515                  370                   469
2019-06-17 17:23:09     100.251       7.8877                  370                   470
2019-06-17 17:23:39     100.263       7.8229                  370                   472
2019-06-17 17:24:09     100.276       7.7583                  370                   474
2019-06-17 17:24:39     100.289       7.694                   370                   474
2019-06-17 17:25:09     100.302       7.6274                  370                   474
2019-06-17 17:25:39     100.314       7.5625                  370                   475
```
