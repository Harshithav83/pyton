startpoint = int(input("Enter the start point"))
endpoint = int(input("Enter the end point"))
for i in range (startpoint, endpoint + 1):
    if i % 10 == 0:
        break
    else:
        print(i)
