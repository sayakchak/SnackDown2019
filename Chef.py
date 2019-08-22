T=int(input())
if T<1 or T>1000:
    exit(0)
sum = 0
for test in range (T):
    k=int(input())
    sum += k
    if k<1 or k>100000 or sum > 500000:
        exit(0)
    ni=[int(x) for x in input().split()]
    mi=[int(x) for x in input().split()]
    if min(mi) < 0 or min(ni) < 0 or max(mi) > 10**8 or max(ni) > 10**8:
        exit(0)
    i=0
    while (i+3)<=k and str(mi)!=str(ni):
        if mi[i]!=ni[i]:
            if mi[i] < ni[i]:
                break
            else:
                h=1
                for j in range(i,i+3):
                    ni[j] += h
                    h+=1
        i+=1
    if str(mi)==str(ni):
        print("TAK")
    else:
        print("NIE")
