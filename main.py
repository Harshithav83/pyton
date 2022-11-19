endpoint = int(input("Enter the value of endpoint"))
sumofnumbers = 0
i = 0
while i <= endpoint:
    sumofnumbers = sumofnumbers + i
    i = i + 1
    print("The sum of first {} whole numbers is {}".format(endpoint, sumofnumbers))