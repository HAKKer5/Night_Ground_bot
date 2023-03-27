from cbrf.models import DailyCurrenciesRates


daily = DailyCurrenciesRates()
daily.date

daily.get_by_id('R01375').name
a = daily.get_by_id('R01375').value
b = a / 10


print(round((b), 2))