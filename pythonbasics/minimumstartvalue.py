#Start with a given array of integers and an arbitrary initial value x. Calculate the running sum of x plus each array element, from left to right . The running sum must never get below 1. Determine the minimum value of x. 

# example arr = -[-2,3,1,-5]
# if x=4 

def minmaxxval(arr, fxval):
  myarr=arr
  myx = fxval
  myxsum=myx
  print (myarr)
  print(myx)
  #print("min val is: ", min(myarr))
  #print("max val is:", max(myarr))
  #print("sum of arr : ", sum(myarr))
  #print ("sum of arr - myx is :" , sum(myarr)-myx)
  #print ("myx - sum of arr is :" , myx-sum(myarr))
  for arrvals in arr:
    myxsum=myxsum+arrvals
    print("myxsum iteration value is:", myxsum)
  if (myxsum>1):
    print ("valid min x value:", myx)
  #if ((sum(myarr)-myx)>=1):
  #  print ("my x is valid min value: ", myx)
  #else:
  #  print ("my x is not valid min value :", myx)
  #print("diffvalue min - sum is : ", min(myarr)-sum(myarr))
  #print("diffval max - min is : ", max(myarr)-min(myarr))
  #print("diffval max + min is : ", max(myarr)+min(myarr))
  #print("diffval sum - min is : ", sum(myarr)-min(myarr))


arr=[-2,3,1,-5] # min val is 4
arr2=[-5, 4, -2, 3, 1] # min val is 6
arr3=[-5, 4, -2, 3, 1, -1, -6, -1, 0, -5] # min val 8

arrmax=[arr, arr2, arr3]
xval=[4,6,8,2,1]

for x  in xval:
  for arrval in arrmax:
    minmaxxval(arrval, x)

#print(arrmax)
#print("array min val is: ", min(arr))
#print ("sum of arr : ", sum(arr))
#print("max val of array is:", max(arr))
#print("array min val is: ", min(arr2))
#print ("sum of arr : ", sum(arr2))
#print("max val of array is:", max(arr2))
#print("array min val is: ", min(arr3))
#print ("sum of arr : ", sum(arr3))
#print("max val of array is:", max(arr3))
#print("diffvale is:" , sum)
