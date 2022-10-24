import numpy as np
l=[5,2,3,4,8,5,6,7,9,10]
lis=sorted(l)
print("list=",l)
a=np.mean(l)
b=np.median(lis)
sd=np.std(lis)
import statistics as st
c=st.mode(lis)
print("Mean=",a)
print("Median=",b)
print("Mode=",c)
print("standard deviation=",sd)
print("100th percentile of arr : ",np.percentile(li, 100))
