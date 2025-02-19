year = 2000

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This is a Leap Year")
else:
    print("This is not a Leap Year")
