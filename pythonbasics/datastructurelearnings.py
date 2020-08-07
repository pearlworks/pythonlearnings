#uname=input("what is the username: ")
#upwd=input("what is the password: ")
#dpwd='x'*len(upwd)
#print (f'{uname}, your password is : {dpwd} , which is {len(upwd)} characters long , last three letters are {upwd[-3::1]}')
mycart=["hdd", "cpu", "power" , "money"]
#print(mycart)
newcart = mycart[:]
newcart[0]="harddrive"

print(mycart)
print(newcart)

mymatrix=[[1,2,4],[3,4,5],[7,8,9]]
mystrmatric=[["apple", "orange", "grapes"],["water", "honey", "salt"]]
print(mymatrix)
print(mystrmatric)
print(len(mystrmatric))
mycart.extend(["fame","wonder"])
print(mystrmatric[0].count("orange"))
print(list(range(0,30)))
print('::'.join(mystrmatric[0]))
mytuple=(1,2,3,4,5,6)
print(mytuple)
print(mytuple[::-1])

# mylist = [1,2,3,4,4,5,6,6,7,8,8]  -- can have duplicate values
# my_dict ={"a":1,"b":2,}  -- collection of datastructure pairs
my_set = {1,2,3,4,5,6,7,8,"orange"} # -> unique list or  values. 
my_secondset = {6,7,8,9,111,123,"apple"}
print(my_set.difference(my_secondset))
print(my_secondset.difference(my_set))
#ternaryoperator
is_friend=False
can_message="message allowed" if is_friend else "message not allowed"
print(can_message)
