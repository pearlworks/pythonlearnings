#!/bin/python3

alice = [[-117, 28, 30,45,66],[99, 16, 8,65,77],[-1,-2,3,-67,-165],[34,56,77,88,11],[1,2,3,4,5]]

arr=[[11,2,4],[4,5,6],[10,8,-12]]
arlen=len(alice)
print('alice array lenghth is ', arlen)

#list = [1, 3, 5, 7, 9] 
  
# Using for loop 
#for i in list: 
#    print(i) 
#print("alice array lenght:"  %arlen)
#result=[0,0]
#k=0

#while k <= arlen:
  #print("\n value:",alice[k])

#for row in range(arlen):
#  for column in range(arlen):
#    if row==column:
#      print ("regular diagonal value is ", alice[row][column])
    #print ("reverse diagonal value is ", alice[row][rc])

fslash=len(arr)-1
bslash=0
for rar in arr:
  print (rar)

fslashsum=0
bslashsum=0
for rar in arr:
  #print (rar)
  print ("fslash line value :",rar[fslash])
  fslashsum=fslashsum+rar[fslash]
  fslash=fslash-1
  print ("bslash line value :",rar[bslash])
  bslashsum=bslashsum+rar[bslash]
  bslash=bslash+1
print("sum of fslash is: ", fslashsum)
print("sum of bslash is: ", bslashsum)
diffval=abs(abs(fslashsum)-abs(bslashsum))
print("difference is: ", diffval)

  #print ("alice ", alice[k])
  #print ("bob",bob[k])
  #if alice[k] <= bob[k]:
    #print("bob gets a point")
    #result[1]=result[1]+1
  #else:
    #print("alice gets a point")
    #result[0]=result[0]+1

#print("comparison of alice and bob is:", result)

 # print ("bob" + bob[i])
 # if (alice[i]  <= bob[i]):
 #   print("bob is bigger")
 # else:
 #   print("alice scores")
