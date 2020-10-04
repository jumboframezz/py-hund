def getRate(argument):
    rates = {
        "BGN": 1.00,
        "USD": 1.79549,
        "EUR": 1.95583,
        "GBP": 2.53405
    }
    return rates.get(argument, "zero")


print(getRate("JPY"))
print(getRate("USD"))
