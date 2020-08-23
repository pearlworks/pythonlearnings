arr=[1,1,0,-1,-1]
pnumlist=[pnum for pnum in arr if pnum>0]
nnumlist=[nnum for nnum in arr if nnum<0]
zcount=arr.count(0)

print ("pnum list is: ", pnumlist)
print ("negative num list is: ", nnumlist)
print("count of zeros: ",zcount)
print ("count of pnums:", len(pnumlist))
print ("count of negative nums", len(nnumlist))

pratio=len(pnumlist)/len(arr)
nratio=len(nnumlist)/len(arr)
zratio=zcount/len(arr)

print ("Pratio is: ", format(pratio,'.6f'))
print ("Nratio is: ", format(nratio,'.6f'))
print ("zratio is: ", format(zratio,'.6f'))