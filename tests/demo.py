# demo.py - временный файл для проверки
from core.clients.api_client import APIClient

client = APIClient()
print(client.base_url)
# Вывод: https://restful-booker.herokuapp.com

print(client.get("/booking/1"))
# Вывод (данные на стенде меняются, у тебя будут свои):
# {'firstname': 'Mary', 'lastname': 'Jackson', 'totalprice': 628, 'depositpaid': True,
#  'bookingdates': {'checkin': '2018-12-26', 'checkout': '2020-12-20'}, 'additionalneeds': 'Breakfast'}

print(client.get("/booking", params={"firstname": "Jim"})[:2])
# Вывод: [{'bookingid': 3}, {'bookingid': 8}]

print(client.post("/auth", data={"username": "admin", "password": "password123"}))
# Вывод: {'token': 'e572ff863253251'}