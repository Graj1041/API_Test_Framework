import requests
import json
from Utilities.customLogger import LogGen
from Utilities.assertions import assert_valid_schema


class Test_API:

    # Additional headers
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    url = 'https://jsonplaceholder.typicode.com/'
    logger = LogGen.log_gen()

    def test_get_when_api_returns_at_least_100_records(self):
        self.logger.info("test_get_when_api_returns_at_least_100_records started")
        # Arrange
        url = self.url + 'posts'
        # Act
        resp = requests.get(url, headers=self.headers)
        json_data = (json.loads(resp.text))
        # Assert
        assert resp.status_code == 200
        assert_valid_schema(json_data[0], 'user.json')
        assert len(json_data) == 100
        self.logger.info("test_get_when_api_returns_at_least_100_records completed")

    def test_verify_user_id(self):
        self.logger.info("test_verify_user_id started")
        # Arrange
        url2 = self.url + 'posts/1'
        # Act
        resp = requests.get(url2, headers=self.headers)
        json_data = (json.loads(resp.text))
        # Assert
        assert resp.status_code == 200
        assert_valid_schema(json_data, 'user.json')
        assert len(json_data)/4 == 1
        assert json_data['id'] == 1
        self.logger.info("test_verify_user_id completed")

    def test_verify_invalid_posts(self):
        self.logger.info("test_verify_invalid_posts started")
        # Arrange
        url3 = self.url + 'invalidposts'
        # Act
        resp = requests.get(url3, headers=self.headers)
        # Assert
        assert resp.status_code == 404

        self.logger.info(json.loads(resp.text))
        self.logger.info("test_verify_invalid_posts completed")

    def test_verify_when_record_is_created(self):
        self.logger.info("test_verify_when_record_is_created started")
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
        self.logger.info("test_verify_when_record_is_created completed")

    def test_verify_when_record_is_updated(self):
        self.logger.info("test_verify_when_record_is_updated started")
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
        self.logger.info("test_verify_when_record_is_updated completed")

    def test_verify_delete_posts(self):
        self.logger.info("test_verify_delete_posts started")
        # Arrange
        url6 = self.url + 'posts/1'
        # Act
        resp = requests.delete(url6, headers=self.headers)
        # Assert
        assert resp.status_code == 200
        self.logger.info("test_verify_delete_posts completed")
