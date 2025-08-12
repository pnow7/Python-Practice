leapyear = int(input())

if (leapyear % 4 == 0 and leapyear % 100 != 0) or (leapyear % 400 == 0):
    print("1")
else:
    print("0")