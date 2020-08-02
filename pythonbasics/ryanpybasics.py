#https://github.com/aneagoie/ztm-python-cheat-sheet
statement="Shan narayan learns python"
print(statement)
print(statement[::-1])
#saidstatement=input("what do you want to say?")
#print("what was said is:" + saidstatement)
teststring = 'abcdefghijklmnopqrstuvwxyz123456789'
print("teststring is: " + teststring)
reversestring=teststring[::-1]
print("reversestring is: " + reversestring)
#print (teststring[0:5])
skippedstring=teststring[::2]
print ("skipped and reversed original::" + skippedstring[::-1])
print ("skippedstring::" + skippedstring)
reverseskipped=reversestring[::2]
print("reverseskipped ::" + reverseskipped)

#Datatypes are: 
#test='extra'
#int(test)
#float(myfloat)
#bool(mybool)
#str(mystr)
#list(mylist)
#tuple(mytuple)
#set(myset)
#dict(mydict)
#complex()
#bin() - binary of the number or variable or value
print ("Data Types are as below")
print (type(4+10))
print (type(2/3))
print (type(True))
#print (type{1,2,3,4,5,6,7})

print (4 ** 4)
print (type(2//3))
print (4 % 3) # prints the reminder of the divisionc
#types of classes

#basic math functions: 
print ("Basic math functions")

print (round(4.93))

long_string='''
#Operator precedence
# ()
# **
# * /
# + - 
'''
print((5 + 4) * 10 / 2)

print(((5 + 4) * 10) / 2)

print((5 + 4) * (10 / 2))

print(5 + (4 * 10) / 2)

print(5 + 4 * 10 // 2)

print (bin(10))

#specialized Datatypes
None # - special datatype which gives nothing.  
#print (teststring[::-1])

#Constants are defined by UPPERCASE variable declaration as a practice.
#variables should not be started with two __ as it is not a good practice.  
a,b,c=1,2,3
print(a)
print(b)
print(c)
some_value=5
some_value=some_value+2
some_value/=2
print(some_value)
print(long_string)

print(f'{long_string}')

#immutabililty: 

testimmute='01234567'
testimmute=testimmute+'8'
print(testimmute)
print(long_string.upper())

print(bool(0))