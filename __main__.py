import sys
import requests
import json


def main(dict):
    url = 'https://belarusbank.by/api/kursExchange'
    response = requests.get(url).json()[0]
    value = response[f'{dict["currency"]}_out']
    dict["rate"] = value
    return dict
