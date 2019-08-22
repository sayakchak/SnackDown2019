T= int(input())
if T<1 or T>1000:
    exit(0)
s=0
while T>0 :
    n,m,k,l=[int(x) for x in input().split()]
    s += n
    if n<1 or m<1 or l<1 or k<2 or n>10**5 or m>10**5 or l>10**4 or k>10**9 or s>10**6:
        exit(0)
    a=[int(x) for x in input().split()]
    a.sort()
    if a[0]<1 or a[-1]> (k-1):
        exit(0)
    for i in range(1,n):
        if a[i]==a[i-1]:
            exit(0)
    B = []
    C = m*l
    M = max(0,(C + (n+1)*l - k))
    #print(M)
    i = 0
    while i<n and a[i]<=k:
        M = min((C+ (i+1)*l - a[i]),M)
        i += 1
    print(M)
    T -= 1
    
