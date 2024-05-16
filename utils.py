import random
import string

import requests
from faker import Faker

from data import REGISTER_URL, MAKE_ORDER_URL, INGREDIENTS_LIST_SAMPLE


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def random_payload():
    email = Faker().email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


def get_tokens(payload):
    login_pass = {}

    response = requests.post(REGISTER_URL, data=payload)
    data = response.json()
    if response.status_code == 200:
        login_pass['accessToken'] = data['accessToken']
        login_pass['refreshToken'] = data['refreshToken']

    return login_pass


def get_ingredients_payload():
    return INGREDIENTS_LIST_SAMPLE


def make_order():
    payload = random_payload()
    login_pass = get_tokens(payload)
    ingredients_payload = get_ingredients_payload()
    order_request = requests.post(MAKE_ORDER_URL, headers={'authorization': login_pass['accessToken']}, data=ingredients_payload)
    if order_request.status_code == 200:
        return order_request.json()['order']['number']
