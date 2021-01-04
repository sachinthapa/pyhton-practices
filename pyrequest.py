import requests
from getpass import getpass

response = requests.get(
           'https://api.github.com/search/repositories',
           timeout = 5,
           params = {'q':'requests+language:python'},
           headers={'Accept': 'application/vnd.github.v3.text-match+json'},
        )
#requests.get('https://api.github.com', verify=False)

json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

print(f'Post {requests.post("https://httpbin.org/post", data={"key":"value"})}')
print(f'Head {requests.head("https://httpbin.org/get")}')

response = requests.post('https://httpbin.org/post', json={'key':'value'})

print(response.json()['data']) 
print(response.json()['headers']) 

