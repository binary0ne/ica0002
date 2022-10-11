import requests

SOURCE_LINK = 'http://193.40.156.67/students/binary0ne.html'

response = requests.get(SOURCE_LINK)
print(response.content)