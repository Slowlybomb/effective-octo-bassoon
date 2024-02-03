# CHALLENGE
from flask import Flask, request, render_template
# from currency_exchange import get_currency_rate



import requests

def get_currency_rate(euro, currency):
    url = 'https://api. currencybeacon.com/v1/convert'
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


app = Flask(__name__)

@app.route("/xchange", methods=['GET', 'POST'])
def xchange():
    euro = ""
    conversion_result = None
    currency = ""
    currency_rate = None 

    if request.method == "POST":
        try:
            euro = request.form.get("euro", type=float)
            currency = request.form.get("currency")
            currency_rate = get_currency_rate(euro, currency)
            if currency_rate:
                conversion_result = round(currency_rate * euro, 2)
            else:
                conversion_result = "Conversion failed. Please try again."
        except (ValueError, TypeError) as e:
            conversion_result = "Invalid input."
            print(f"Error: {e}")

    return render_template("xchange_form.html", 
                           euro=euro, currency_rate=currency_rate, currency=currency, conversion_result=conversion_result)
