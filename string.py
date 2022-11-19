number = 0
endpoint = int(input("enter the end point"))
while number < endpoint:
    number = number + 1
    if number % 5 == 0:
        print(number)
    else:
        continue
