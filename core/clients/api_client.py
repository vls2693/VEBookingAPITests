import os

import requests
from dotenv import load_dotenv

from core.settings.environments import Environment

load_dotenv()  # читаем .env один раз - при импорте модуля


class APIClient:
    def __init__(self):
        # 1. Узнаём, на какой среде запускаемся
        environment_str = os.getenv("ENVIRONMENT")
        try:
            # 2. Ищем элемент enum по имени: "PROD" -> Environment.PROD
            environment = Environment[environment_str]
        except KeyError:
            raise ValueError(f"Unsupported environment value: {environment_str}")

        # 3. По среде получаем базовый адрес
        self.base_url = self.get_base_url(environment)
        # 4. Заголовки, которые уйдут с каждым запросом
        self.headers = {
            "Content-Type": "application/json",
        }

    def get_base_url(self, environment: Environment) -> str:
        if environment == Environment.TEST:
            return os.getenv("TEST_BASE_URL")
        elif environment == Environment.PROD:
            return os.getenv("PROD_BASE_URL")
        else:
            raise ValueError(f"Unsupported environment: {environment}")

    def get(self, endpoint, params=None, status_code=200):
        url = self.base_url + endpoint  # базовый адрес + "/booking/1"
        response = requests.get(url, headers=self.headers, params=params)
        if status_code:
            assert response.status_code == status_code
        return response.json()

    def post(self, endpoint, data=None, status_code=200):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers, json=data)
        if status_code:
            assert response.status_code == status_code
        return response.json()