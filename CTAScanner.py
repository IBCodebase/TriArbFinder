import requests

class CTAScanner:
    def printCurrencies(self):
        endpoint = 'https://api.exchange.coinbase.com/currencies'
        response = requests.get(endpoint)
        data = {}
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
        for item in data:
            print(f"ID: {item['id']}, Name: {item['name']}")

    def getCurrenciesIdList(self):
        currenciesList = []
        endpoint = 'https://api.exchange.coinbase.com/currencies'
        response = requests.get(endpoint)
        data = {}
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
        for item in data:
            currenciesList.append(item['id'])
        return currenciesList

    def updateCurrenciesList(self):
        with open("currentCurrenciesList", "w") as file:
            currenciesList = CTAScanner.getCurrenciesIdList(self)
            for item in currenciesList:
                file.write(str(item + '\n'))

