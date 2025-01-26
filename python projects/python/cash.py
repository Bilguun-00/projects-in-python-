from cs50 import get_float

def calculate(cent):
    quarters = 0
    while cent >= 25:
        quarters = quarters + 1
        cent = cent - 25
    while cent >= 10:
        quarters = quarters + 1
        cent = cent - 10
    while cent >= 5:
        quarters = quarters + 1
        cent = cent - 5
    while cent >= 1:
        quarters = quarters + 1
        cent = cent - 1
    return quarters



while True:
    cent = get_float("cash owed: ")
    if cent > 0:
        break
quarters = calculate(cent * 100)
cent = cent - quarters
print(quarters)





