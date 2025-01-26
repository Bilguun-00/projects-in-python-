from cs50 import get_int

card = get_int("card number: ")
number = card
i = 0
while number > 0:
    number = number / 10
    i += i
if i != 13 and i != 15 and i != 16:
    print("invalid")





