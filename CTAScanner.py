import random
import time

from isArbatrageCoinbase import IsArbitrageCoinbase
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

    def getCodeFromList(self, lineNum):
        with open("currentCurrenciesList", "r") as file:
            content = file.readlines()
            return content[lineNum].replace("\n","")

    def getListLength(self):
        with open("currentCurrenciesList", "r") as file:
            content = file.readlines()
            return len(content)

    def randomCheck(self, secondsToRun):
        timeLimit = time.time() + secondsToRun
        listLength = self.getListLength()
        while True:
            currency1 = self.getCodeFromList(random.randint(0, listLength - 1))
            currency2 = self.getCodeFromList(random.randint(0, listLength - 1))
            currency3 = self.getCodeFromList(random.randint(0, listLength - 1))
            print(currency1 + " " + currency2 + " " + currency3)
            arbInstance = IsArbitrageCoinbase.isTriangularArbitrage(currency1, currency2, currency3)


            if arbInstance > 1:
                print(currency1 + ":" + currency2 + ":" + currency3 + "-" + str(arbInstance))

            if timeLimit <= time.time():
                break
            time.sleep(1)
