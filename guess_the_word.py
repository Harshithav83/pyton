counter = 0
secret_word = "Python"
while counter <7:
    word = input("Enter the secret word")
    counter = counter+1
    if word == secret_word:
        print("you guessed it right")
        break
else:
        print("better luck next time")