import requests

BASE_URL = 'http://127.0.0.1:8000'

response = requests.get(BASE_URL + '/api/v1/health')
print(response.status_code)
print(response.json())

resp = requests.post(
    url=BASE_URL + '/api/v1/predict',
    json={"text": "what are you nice  doing ?!!!"}
    )
print(resp.status_code)
print(resp.json())