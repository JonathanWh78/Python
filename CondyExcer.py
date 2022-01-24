usermark = int(input ("Please enter your mark: "))

if usermark > 85:
   print ("Distinction")
elif usermark <= 85 and usermark >=65:
   print ("Pass")
else:
   print ("Fail")

usermark2 = int(input ("Please enter your mark: "))

if usermark2 > 65:
    if usermark2 >=65 and usermark2 <=85:
        print ("Pass")
    else:
        print ("Distinction")
else:
    print ("fail")