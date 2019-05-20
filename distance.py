import googlemaps
from datetime import datetime
import numpy as np
import config
import json
import re


def calculate_without_tolls(gmaps, now, origin, destination):
    without_tolls = gmaps.distance_matrix(origin,
                                          destination,
                                          mode="driving",
                                          avoid="tolls",
                                          departure_time=now)

    no_toll_drivetime = without_tolls['rows'][0]['elements'][0]['duration']['text']
    no_toll_drivetime  = re.findall("\d+", no_toll_drivetime)
    return int(no_toll_drivetime[0])


def calculate_with_tolls(gmaps, now, origin, destination):
    with_tolls = gmaps.distance_matrix(origin,
                                       destination,
                                       mode="driving",
                                       departure_time=now)
    toll_drivetime = with_tolls['rows'][0]['elements'][0]['duration']['text']
    toll_drivetime  = re.findall("\d+", toll_drivetime)
    return int(toll_drivetime[0])


def calc_time_saved(origin, destination):
    gmaps = googlemaps.Client(key=config.GOOGLE_KEY)
    now = datetime.now()
    time_without = calculate_without_tolls(gmaps, now, origin, destination)
    time_with = calculate_with_tolls(gmaps, now, origin, destination)
    diff = time_without - time_with
    return str(diff)


if __name__ == '__main__':
    calc_time_saved(config.WORK_ADDRESS, config.HOME_ADDRESS)
