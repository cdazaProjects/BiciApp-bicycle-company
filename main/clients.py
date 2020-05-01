import requests


class UserApi(object):
    url = 'https://ms-spring.herokuapp.com/'

    def register_user(self, payload):
        self.url += 'api/user/enterprise-user'
        response = requests.post(self.url, payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception


class BicycleApi(object):
    url = 'https://rent-bicycle.herokuapp.com/'

    def register_bicycle(self, payload):
        self.url += 'api/bicycle/'
        response = requests.post(self.url, payload)
        if response.status_code == 201:
            return response.json()