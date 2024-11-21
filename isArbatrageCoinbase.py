import requests
import json

class IsArbitrageCoinbase:

    def fetchApiData(baseCurrency, quoteCurrency):
        # both inputs are strings
        endpoint = 'https://api.coinbase.com/v2/prices/' + baseCurrency + '-' + quoteCurrency + '/spot'
        response = requests.get(endpoint)
        data = {}
        if response.status_code == 200:
            data = response.json()

            #print('amount: ' + data['data']['amount'])
        else:
            print(f"Error: {response.status_code}, {response.text}")
            print('--------------fetch api data-----------------------------')
            print(data)
            print('---------------------------------------------------------')
        return float(data['data']['amount'])

    def isTriangularArbitrage(currency1, currency2, currency3):
        # all inputs are strings
        value1 = IsArbitrageCoinbase.fetchApiData(currency1, currency2)
        value2 = IsArbitrageCoinbase.fetchApiData(currency2, currency3)
        value3 = IsArbitrageCoinbase.fetchApiData(currency3, currency1)

        #print('-------------------isTriangularArbitrageCompare-----------------')
        #print("c1: " + currency1 + " c2: " + currency2 + " c3: " + currency3)
        #print(value1)
        #print(value2)
        #print(value3)
        #print('----------------------------------------------------------------')

        return IsArbitrageCoinbase.isTriangularArbitrageCompare(value1, value2, value3)

    def isTriangularArbitrageCompare(value1, value2, value3):
        # all inputs are floats
        value1 = IsArbitrageCoinbase.normalize(value1)
        value2 = IsArbitrageCoinbase.normalize(value2)
        value3 = IsArbitrageCoinbase.normalize(value3)
        #print('----------- isTriangularArbitrage Compare ----------------')
        #print(value1)
        #print(value2)
        #print(value3)
        #print('-----------------------------------------------------------')

        return value1 * value2 * value3

    def normalize(value):
        # input is a float
        if value == 0:
            raise ValueError("Cannot divide by zero")
        return 1 / value


