import math

numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getNum(char):
    return numbers.index(char)

def baseConvert(xBase,yBase,str):
    str=str.upper()
    if xBase == yBase:
        return str
    if (not isinstance(xBase,int)) or (not isinstance(yBase,int)):
        return 'Error: bases must be integers'
    if (xBase < 2) or (yBase < 2):
        return 'Error: bases must be greater than or equal to 2'
    total = 0
    place = len(str)-1
    for char in str:
        if getNum(char) > xBase:
            return 'Error: character outside of starting base range'
        total += getNum(char)*math.pow(xBase,place)
        place -= 1
    if yBase == 10:
        return f'{total}'
    output = ''
    subtotal = total
    n = 0
    r = 0
    while total > math.pow(yBase,n-1):
        r = int(subtotal % yBase) 
        output = numbers[r] + output
        subtotal = (subtotal - r) / yBase
        n+=1
    return output

b1 = 0
while b1 != 49:
    b1 = int(input("Enter the starting base system: "))
    b2 = int(input("Enter the base system to be converted to: "))
    s = input("Enter your number in the starting base system: ")
    print(baseConvert(b1,b2,s))
