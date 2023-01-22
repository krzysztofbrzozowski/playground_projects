"""
@author:    Krzysztof Brzozowski
@file:      test_iot_api
@time:      22/01/2023
@desc:      
"""
import os
import pytest
import requests

# Hidden values, in GitHub workflows it is accessible via os.
try:
    from secrets import API_TOKEN
except ImportError as e:
    API_TOKEN = os.environ['API_TOKEN']

ENDPOINT = 'http://iot-api.krzysztofbrzozowski.pl'


class TestIoTAPITempMonitor:
    @pytest.fixture(autouse=True)
    def setup_startup(self):
        pass

    def test_endpoint_is_ok(self):
        response = requests.get(ENDPOINT)
        assert response.status_code == 200

    def test_create_db_record_with_sample_data(self):
        headers = {'Authorization': f'Token {API_TOKEN}', 'Content-Type': 'application/json'}
        payload = [{'hex_address': 31, 'temperature': 10, 'humidity': 20}]

        response = requests.post(f'{ENDPOINT}/post-pms-data', json=payload, headers=headers)
        print(response.content)
        assert response.status_code == 201

    def test_create_db_record_requires_token(self):
        headers = {'Authorization': f'Token WRONG_TOKEN', 'Content-Type': 'application/json'}
        payload = [{'hex_address': 31, 'temperature': 10, 'humidity': 20}]

        response = requests.post(f'{ENDPOINT}/post-pms-data', json=payload, headers=headers)
        print(response.content)
        assert response.status_code == 401
