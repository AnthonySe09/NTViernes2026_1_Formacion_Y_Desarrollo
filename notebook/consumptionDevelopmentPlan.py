import requests

def consume_development_plans():
    url = "http://localhost:8080/api/development-plans"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

plans = consume_development_plans()
print(plans)