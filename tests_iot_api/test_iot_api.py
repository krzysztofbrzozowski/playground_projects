"""
@author:    Krzysztof Brzozowski
@file:      test_iot_api
@time:      22/01/2023
@desc:      
"""
import pytest
import requests

ENDPOINT = 'http://iot-api.krzysztofbrzozowski.pl'


class TestIoTAPI:
    @pytest.fixture(autouse=True)
    def setup_startup(self):
        pass

    def test_endpoint_is_ok(self):
        response = requests.get(ENDPOINT)
        assert response.status_code == 200
