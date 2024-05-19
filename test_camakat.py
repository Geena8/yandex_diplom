# Георгина Адайи, 16-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_request
import requests
import configuration

def get_order(track_num):
    return requests.get(
        configuration.URL_SERVICE 
        + configuration.GET_ORDER_PATH 
        + str(track_num)
    )
# test to check all is working
def test_get_order():
    track = sender_request.get_track()
    assert get_order(track).status_code == 200
