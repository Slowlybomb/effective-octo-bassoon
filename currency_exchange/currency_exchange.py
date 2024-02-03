import requests

def get_currency_rate(euro, currency):
    url = 'https://api.currencybeacon.com/v1/convert'
    api_key = 'stVMycnI81B37nUGXdrNEsdeQLOzYtQX'
    source_currency = "EUR"
    target_currency = currency
    amount = euro

    params = {
        'from': source_currency,
        'to': target_currency,
        'amount': 1
    }

    headers = {
        'Authorization': 'Bearer ' + api_key
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        currency_rate = json_data["value"]
        return currency_rate
    else:
        print(f"Failed to convert currency. Status code: {response.status_code}, Error: {response.text}")
        return None
