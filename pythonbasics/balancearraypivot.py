arr=[1,2,3,4,6]

arlength=len(arr)



for i in range(arlength): 
  leftsum = 0
  rightsum = 0
  # get left sum 
  lefarray=arr[:i]
  print("left array :", lefarray)
  rightarray=arr[(i+1):(arlength)]
  print("right array :", rightarray)
  leftsum=sum(lefarray)
  rightsum=sum(rightarray)
  print("iterate value is:", i)
  print("sum values are ",leftsum, rightsum)
  if (leftsum==rightsum):
    print("pivot index is:",i)