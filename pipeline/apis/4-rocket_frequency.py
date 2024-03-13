#!/usr/bin/env python3

import requests

def get_launch_data():
    response = requests.get("https://api.spacexdata.com/v4/launches")
    data = response.json()
    return data

def count_launches_per_rocket(launches):
    rocket_count = {}
    for launch in launches:
        rocket_name = launch['rocket']
        if rocket_name in rocket_count:
            rocket_count[rocket_name] += 1
        else:
            rocket_count[rocket_name] = 1
    return rocket_count

def main():
    launches = get_launch_data()
    rocket_count = count_launches_per_rocket(launches)
    sorted_rocket_count = sorted(rocket_count.items(), key=lambda x: (-x[1], x[0]))
    for rocket, count in sorted_rocket_count:
        print("{}: {}".format(rocket, count))

if __name__ == '__main__':
    main()

