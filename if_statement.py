num = int(input("Please enter any whole number between 0 and 10: "))

if isinstance(num, int):
    if num <= 10:
        if num >=0:
            print("You have entered %d number" % num)
    elif num > 10:
        print("You have entered invalid number")
else:
    print("You have entered non-integer value")