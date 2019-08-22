T = int(input())
if T<1 or T>100:
    exit(0)
sum = 0
for j in range (T):
    N = int(input())
    sum += N
    if N<2 or N> (10**5) or sum > (10**6):
        exit(0)
    A = [int(x) for x in input().split()]
    if min(A) <1 or max(A)> (10**9):
        exit(0)
    B = []
    m = min(A)
    s = A.index(m)
    for i in range (N-1,0, -1): #finding index of smallest when there's a division
        if (A[i] == m and A[i-1]!= A[i]):
            s = i
            break
    if s>0:
        for i in range (s,N):
            B.append(A[i])
        for i in range(s):
            B.append(A[i])
    else:
        B = A
    flag = 1
    for i in range(N-1):
        if B[i] - B[i+1] > 0:
            flag = 0 
            break
    #print(B)
    x = "YES" if flag == 1 else "NO"
    print(x)
   




















'''T = int(input())
if T<1 or T>100:
    exit(0)
sum = 0
for j in range (T):
    N = int(input())
    sum += N
    if N<2 or N> (10**5) or sum > (10**6):
        exit(0)
    A = [int(x) for x in input().split()]
    if min(A) <1 or max(A)> (10**9):
        exit(0)
    flag = 1
    B = []
    s = A.index(min(A))
    if s>0:
        for i in range (s,N):
            B.append(A[i])
        for i in range(s):
            B.append(A[i])
    else:
        B = A
    for i in range(N-1):
        if B[i] - B[i+1] > 0:
            flag = 0 
            break
    print(B)
    x = "YES" if flag == 1 else "NO"
    print(x)
   '''