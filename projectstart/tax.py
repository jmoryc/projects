income = int(input("Proszę o wprowadzenia dochodu bazowego:"))

if income < 25000:
    income = income * 0.95

if income > 25000 and income < 50000:
    income = income * 0.90

if income > 50000 and < 60000:
    income = income * 0.85


print("Ostateczny dochód po odjęciu podatku wynosi:", income)