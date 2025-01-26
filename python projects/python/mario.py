from cs50 import get_int
while True:
    heights = get_int("height: ")
    if heights >= 1 and heights <= 8:
        break
for colum in range(1, heights +1):
    for i in range(heights - colum):
        print(" ", end="")
    for i in range(colum):
         print("#", end="")
    print("  ", end="")
    for i in range(colum):
         print("#", end="")
    print()






