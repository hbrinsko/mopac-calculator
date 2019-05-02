import googlemaps
from datetime import datetime
import numpy as np
import config
import json
import config


def calculate_without_tolls(gmaps, now):
    without_tolls = gmaps.distance_matrix(config.start_point,
                                          config.end_point,
                                          mode="driving",
                                          avoid="tolls",
                                          departure_time=now)

    no_toll_drivetime = without_tolls['rows'][0]['elements'][0]['duration']['text']
    return int(no_toll_drivetime.replace(" mins", ""))


def calculate_with_tolls(gmaps, now):
    with_tolls = gmaps.distance_matrix(config.start_point,
                                       config.end_point,
                                       mode="driving",
                                       departure_time=now)
    toll_drivetime = with_tolls['rows'][0]['elements'][0]['duration']['text']
    return int(toll_drivetime.replace(" mins", ""))


def calc_time_saved():
    gmaps = googlemaps.Client(key=config.google_key)
    now = datetime.now()
    time_without = calculate_without_tolls(gmaps, now)
    time_with = calculate_with_tolls(gmaps, now)
    diff = time_without - time_with
    return diff


if __name__ == '__main__':
    calc_time_saved()
