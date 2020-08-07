#!/bin/python3
def diffdiagonal(arr):
  
  bslash=0
  fslash=len(arr)-1
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
  return diffval

alice = [[-117, 28, 30,45,66],[99, 16, 8,65,77],[-1,-2,3,-67,-165],[34,56,77,88,11],[1,2,3,4,5]]

arr=[[11,2,4],[4,5,6],[10,8,-12]]

longarr=[
  [6, 6, 7, -10, 9, -3, 8, 9, -1],
[9, 7, -10, 6, 4, 1, 6, 1, 1],
[-1, -2, 4, -6, 1, -4, -6, 3, 9],
[-8, 7, 6, -1, -6, -6, 6, -7, 2],
[-10, -4, 9, 1, -7, 8, -5, 3, -5],
[-8, -3, -4, 2, -3, 7, -5, 1, -5],
[-2, -7, -4, 8, 3, -1, 8, 2, 3],
[-3, 4, 6, -7, -7, -8, -3, 9, -6],
[-2, 0, 5, 4, 4, 4, -3, 3, 0]
]
#arlen=len(alice)
#print('alice array lenghth is ', arlen)

result=diffdiagonal(longarr)


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
