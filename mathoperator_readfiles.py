def math(value1, value2):
    print(value1, value2)
    print('Addition: ', value1+value2)
    print('Subtraction: ', value1-value2)
    print('Multiplication: ', value1*value2)
    print('Division: ', value1/value2)
    print('Modulus: ', value1%value2)
    print('Exponent: ', value1**value2)
    print('FloorDivision:', value1//value2)

filePath= 'S:\\INFO8005_PY\\'
firstfiletoread= '8685825_Value1.txt'
secondfiletoread= '8685825_Value2.txt'
#print(firstfiletoread)
readfirstfile = open(filePath+ firstfiletoread, "r")
readsecondfile = open(filePath+ secondfiletoread, "r")
firstfiledata= int(readfirstfile.read())
print(type(firstfiledata))
secondfiledata= int(readsecondfile.read())
print(type(secondfiledata))

 
math(firstfiledata, secondfiledata)