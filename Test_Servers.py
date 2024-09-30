import requests

print(requests.get('http://127.0.0.1:8000').json())

print(requests.get('http://127.0.0.1:8000/items/0').json())

print(requests.get('http://127.0.0.1:8000/items?name=Mouse').json())

print(requests.get('http://127.0.0.1:8000/items/?category=hardware').json())

print(requests.get('http://127.0.0.1:8000/items/?category=peripherals').json())