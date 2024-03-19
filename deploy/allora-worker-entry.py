import requests

url = 'http://host.docker.internal:3000/service_output'
payload = {
    "input": ""
}

# Set the Content-Type header
headers = {'Content-Type': 'application/json'}

print("request")

# Make the POST request
response = requests.post(url, json=payload, headers=headers)
