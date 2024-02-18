import requests

url = 'https://api.github.com/some/endpoint'

headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

# print(r)
# print(r.text)
# print(r.encoding)
# print(r.content)
# print(r.headers)

print(r.json())

