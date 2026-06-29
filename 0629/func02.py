def addMany(*args):
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result

print(addMany(1,2))
print(addMany(1,2,3,4,5))
print(addMany(1,2,3,4,5,6,7,8,9,10))
