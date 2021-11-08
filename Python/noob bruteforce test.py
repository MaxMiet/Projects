import requests

url = 'http://localhost/login.php'

data = {
    'username': 'max',
    'password': 'maxpw123',
    #'token': '4adc370f11ad7e5659ebfcea3969257c0b6c64zb'
}

response = requests.post(url, data=data).text

print(response)