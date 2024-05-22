import configuration
import requests
import data

import logging


def make_order(body1):
    print(configuration.URL_SERVICE+configuration.CREATE_ORDER_PATH)
    return requests.post(configuration.URL_SERVICE +configuration.CREATE_ORDER_PATH,
                         json= body1,
                         headers = data.headers)

def get_track():
    order = make_order(data.user_body)
    logging.error("ORDER:"+str(order))
    track = order.json()
    return track

