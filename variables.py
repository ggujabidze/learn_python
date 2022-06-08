import string


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if myfloat == 10.0 and isinstance(myfloat, float):
    print("Float: %f" % myfloat)
if myint == 20 and isinstance(myint, int):
    print (f"Integer: {myfloat}")