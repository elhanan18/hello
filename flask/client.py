import requests

url = 'http://localhost:5000/hello'
signup = 'http://localhost:5000/signup'
status = 'http://localhost:5000/status'
data = "Elhanan"

r = requests.post(url, data=data, allow_redirects=True)
print(r.content)

r = requests.get(url)
print(r.content)

r = requests.post(signup)
print(r.content)

r = requests.get(status)
print(r.content)

