currency=float(input())
fromCurr=input()
toCurr=input()

def getRate(argument):
    switcher = {
        "BGN": 1.00,
        "USD": 1.79549,
        "EUR": 1.95583,
        "GBP": 2.53405
    }
    return switcher.get(argument, "nothing")

money=currency*getRate(fromCurr)
fx_money=money / getRate(toCurr)

print("%.2f"%(fx_money))

