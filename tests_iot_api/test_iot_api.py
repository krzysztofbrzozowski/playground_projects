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
    from secrets import API_KEY
except ImportError as e:
    API_KEY = os.environ['API_KEY']

ENDPOINT = 'http://iot-api.krzysztofbrzozowski.pl'


class TestIoTAPITempMonitor:
    @pytest.fixture(autouse=True)
    def setup_startup(self):
        pass

    def test_endpoint_is_ok(self):
        response = requests.get(ENDPOINT)
        assert response.status_code == 200

    def test_create_db_record_with_sample_data(self):
        headers = {'Authorization': f'Token {API_KEY}', 'Content-Type': 'application/json'}
        payload = [{'hex_address': 0x01, 'temperature': 10, 'humidity': 20}]

        # POST
        create_db_record_response = requests.post(url=f'{ENDPOINT}/post-pms-data', json=payload, headers=headers)
        assert create_db_record_response.status_code == 201
        create_db_record_response = create_db_record_response.json()[0]

        # GET
        get_db_record_response = requests.get(url=f'{ENDPOINT}/get-pms-data/{0x01}')
        assert get_db_record_response.status_code == 200
        # Currently, overcomplicated because no option in API to get one record
        get_db_record_response = [response
                                  for response in get_db_record_response.json()
                                  for k, v in response.items()
                                  if k == 'title' and v == create_db_record_response['title']][0]

        assert get_db_record_response['title'] == create_db_record_response['title']
        assert get_db_record_response['hex_address'] == create_db_record_response['hex_address']

    def test_create_db_record_requires_token(self):
        headers = {'Authorization': f'Token WRONG_TOKEN', 'Content-Type': 'application/json'}
        payload = [{'hex_address': 0x01, 'temperature': 10, 'humidity': 20}]

        response = requests.post(f'{ENDPOINT}/post-pms-data', json=payload, headers=headers)
        print(response.content)
        assert response.status_code == 401
