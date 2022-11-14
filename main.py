Even numbers
startpoint = int(input("Enter start point: "))
endpoint = int(input("Enter end point: "))
for num in range(startpoint+1, endpoint):
   if(num%2==0):
       print(num)
odd numbers
startpoint = int(input("Enter start point: "))
endpoint = int(input("Enter end point: "))
for num in range(startpoint+1, endpoint):
   if(num%2!==0):
       print(num)
Factorial of numbers
n = int(input("enter the number:"))
result = 1
for i in range (n,0,-1):
    result = result*i
    print("factorial of ", n "is", result)
sum of numbers
list1 = [10,20,60]
sum_list1 = 0
for i in list1:
    sum_list1 = sum_list1 +i
    print("sum of list is:",sum_list1)
    Average of numbers
    num = int(input("How many numbers"))
    totalsum = 0
    for n in range (num):
        numbers = float(input("Enter any number"))
        totalsum += numbers
        avg = totalsum/num

