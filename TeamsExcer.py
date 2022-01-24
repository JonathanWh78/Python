usernum = int(input("Enter a number: "))

if (usernum % 2) == 0:
    print ("Number is even")
else:
    print("Number is odd")

userlett = input("Enter a letter: ")

if userlett == "a" or userlett == "e" or userlett == "i" or userlett == "o" or userlett == "u":
    print ("It was a vowel")
elif userlett == "y" or userlett == "Y":
    print ("sometimes y is a vowel, and sometimes y is a consonant")
else:
    print ("It is a consonant")