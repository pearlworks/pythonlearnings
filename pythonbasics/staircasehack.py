
###STAIRCASE###
from datetime import datetime
print("STAIRCASEPRINTING")
staircase=7
for i in range(staircase,0,-1):
  #print (i)
  #print(i-1)
  #print(staircase%(i-1))
  print(' '*(i-1)+'#'*((staircase)-(i-1)))

####HighCandlesCount####
print("HighCandlesCount")
candle=[5,6,6,4,7,8,8,8]
highval=max(candle)
print (candle.count(highval))

####MIN-MAX-sums-in-array####
print("MIN-MAX-sums-in-array")
#minval=min(candle)
#print("highest value:",highval)
#print("lowest value:",minval)
#minsum, maxsum = 0,0
minsumarr=candle[:]
maxsumarr=candle[:]
#print(minsumarr)
minsumarr.remove(max(candle))
#print(minsumarr)
#print(maxsumarr)
maxsumarr.remove(min(candle))
#print(maxsumarr)
#for i in range(len(candle)):
#  if (candle[i] != highval):
#    minsum+=candle[i]
#  if (candle[i] != minval):
#    maxsum+=candle[i]
  
#print (minsum," ",maxsum)
print("original array is:", candle)
print("minsumarr is:",minsumarr)
print ("maxsumarr is: ",maxsumarr)
print(sum(minsumarr)," ",sum(maxsumarr))

####TIMECONVERSION#####
print("TIMECONVERSION Exercise")
mystr="04:59:59AM"

print(mystr)

constr=":"
if (mystr[len(mystr)-2]) == 'P' or (mystr[len(mystr)-2]) == 'p' :
  #mystr.remove("M")
  
  print(mystr)
  mystr=mystr[:-2]
  splitstr=mystr.split(":")
  print(splitstr)
  print(int(splitstr[0])+12)
  splitstr[0]=str(int(splitstr[0])+12)
  print(splitstr)
  hrstr=constr.join(splitstr)
  print(hrstr)
else:
  mystr=mystr[:-2]
  print(mystr)


#mytime=datetime.strptime(mystr,'%H:%M:%S')

#print(mytime)