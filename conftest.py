import pytest
from utils import random_payload, get_tokens, make_order


@pytest.fixture
def login_data():
    payload = random_payload()
    login_pass = get_tokens(payload)

    return login_pass


@pytest.fixture
def order_number():
    return make_order()
