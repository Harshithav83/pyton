# sample_string = "Hello world"
# print("value of the string at position 0 is", sample_string[0])
# print("value of the string at position 1 is", sample_string[1])
# print("value of the string at position 2 is", sample_string[2])
# print("value of the string at position 3 is", sample_string[3])
# print("value of the string at position 4 is", sample_string[4])
# print("value of the string at positon 5 is", sample_string[5])
# # string index
# print("value of the string at position -1 is", sample_string[-1])
# print("value of the string at position -2 is", sample_string[-2])
# print("value of the string at position -3 is", sample_string[-3])
# print("value of the string at position -4 is", sample_string[-4])
#
# value = "Hello world"
# print(len(value))
# value = "Hello world"
# print(len(value))
# # deleting a string
# value = "Hello world"
# print(value)
# del value
# print(value)
#
# concatenating strings
# value1 = 'hello'
# value2 = 'world'
# print(value1 , end = "")
# print(value2)
#string repetition using
value = "Hello world"
print(value*3)
#check if a substring is present in a string
value = "Hello world"
if "Hello" in value:
    print("Hello is present in the string")
elif "hello" not in value:
    print("hello is not present in the string")
# showing the use of raw strings in python
value = "Are you learning python ? yes\\no"
print(value)
value_modified = r"are you learning python ? yes\no"
print(value_modified)
#count , index , find , lower and upper
value = "Hello world"
print(value.count("H"))
print(value.index("H"))
print(value.find("H"))
print(value.lower())
print(value.upper())
#iterating thourgh a string
value = "hello"
for i in value :
    print(i)
    for i in range(len(value)):
        print(value[i])
# start index string
value = "Hello world"
print(value[0:5])
print(value[6:])
print(value[:5])
print(value[0:5:2])
value = "tinker"
print(value[1:4])
#print the odd index of the string using negative indexing
value = "hello world"
print(value[9:0:-2])

