from collections import Counter
T= int(input())
if T<1 and T>1000:
    exit(0)
s=0
while T>0 :
    n,m,k,l=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    a.sort()
    bt=[]
    q=m
    c=0
    for i in range(1,k+1):
        if (i)%l==0:
            q-=1
        bt.append(((q)*l)+(l-i%l))
        if n!=0:
            if a[c]==i:
                q+=1
                n-=1
            if a[c]==i and c!= len(a)-1:
                c+=1

    print(min(bt))

    T=T-1
exit(0)
