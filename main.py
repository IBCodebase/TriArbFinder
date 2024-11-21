from isArbatrageCoinbase import IsArbitrageCoinbase
from CTAScanner import CTAScanner
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Scanner = CTAScanner()
    Scanner.updateCurrenciesList()
    #print(IsArbitrageCoinbase.isTriangularArbitrage('EIGEN', 'ETH', 'BTC'))
    Scanner.randomCheck(100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
