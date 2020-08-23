import pytest
import requests
import json
from Utilities.customLogger import LogGen
from Utilities.utility import assert_valid_schema

logger = LogGen.log_gen()


class Test_API:

    # Additional headers
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    url = 'https://jsonplaceholder.typicode.com/'

    def test_get_when_api_returns_at_least_100_records(self):
        logger.info("test_get_when_api_returns_at_least_100_records started")
        # Arrange
        url = self.url + 'posts'
        # Act
        resp = requests.get(url, headers=self.headers)
        json_data = (json.loads(resp.text))
        # Assert
        assert resp.status_code == 200
        assert_valid_schema(json_data)
        assert len(json_data) == 100
        logger.info("test_get_when_api_returns_at_least_100_records completed")

    def test_verify_id(self):
        logger.info("test_verify_id started")
        # Arrange
        url2 = self.url + 'posts/1'
        # Act
        resp = requests.get(url2, headers=self.headers)
        json_data = (json.loads(resp.text))
        # Assert
        assert resp.status_code == 200
        assert_valid_schema(json_data)
        assert len(json_data)/4 == 1
        assert json_data['id'] == 1
        logger.info("test_verify_id completed")

    def test_verify_invalid_posts(self):
        logger.info("test_verify_invalid_posts started")
        # Arrange
        url3 = self.url + 'invalidposts'
        # Act
        resp = requests.get(url3, headers=self.headers)
        # Assert
        assert resp.status_code == 404

        logger.info(json.loads(resp.text))
        logger.info("test_verify_invalid_posts completed")

    def test_verify_when_record_is_created(self):
        logger.info("test_verify_when_record_is_created started")
        # Arrange
        url4 = self.url + 'posts'
        payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
        # Act
        resp = requests.post(url4, data=json.dumps(payload), headers=self.headers)
        json_data = json.loads(resp.text)
        # Assert
        assert resp.status_code == 201
        assert json_data['title'] == 'foo'
        assert json_data['body'] == 'bar'
        assert json_data['userId'] == 1
        logger.info("test_verify_when_record_is_created completed")

    def test_verify_when_record_is_updated(self):
        logger.info("test_verify_when_record_is_updated started")
        # Arrange
        url5 = self.url + 'posts/1'
        payload = {'id': 1, 'title': 'abc', 'body': 'xyz', 'userId': 1}
        # Act
        resp = requests.put(url5, data=json.dumps(payload), headers=self.headers)
        json_data = json.loads(resp.text)
        # Assert
        assert resp.status_code == 200
        assert json_data['title'] == 'abc'
        assert json_data['body'] == 'xyz'
        assert json_data['userId'] == 1
        logger.info("test_verify_when_record_is_updated completed")

    def test_verify_delete_posts(self):
        logger.info("test_verify_delete_posts started")
        # Arrange
        url6 = self.url + 'posts/1'
        # Act
        resp = requests.delete(url6, headers=self.headers)
        # Assert
        assert resp.status_code == 200
        logger.info("test_verify_delete_posts completed")
