from converter import fromDecimal, toDecimal

print("Choose conversio: \n1. Decimal -> U2 \n2. Decimal <- U2")

choice = int(input())

number = None

if (choice == 1):
    number = int(input("Type decimal number: "))
    print(fromDecimal(number))
elif (choice == 2):
    number = input("Type number in U2 system: ")
    print(toDecimal(number))
