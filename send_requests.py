import requests

url = "http://127.0.0.1:5000/find-recipe"
payload = {
    "ingredients": "cheese, butter, garlic powder",
    "error-threshold": 0.4
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())
