T = int(input())
if T<1 or T>100:
    exit(0)
for t in range(T):
    N,M = [int(x) for x in input().split()]
    if N<1 or M<1 or N>100 or M>100:
        exit(0)
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    if min(A)<0 or min(B)<0 or max(A)>10**9 or max(B)>10**9:
        exit(0)
    sum_A = 0
    sum_B = 0
    for i in range(N):
        sum_A += A[i]
    for i in range(M):
        sum_B += B[i]
    if sum_A>sum_B:
        print("Alice")
    if (sum_A == 0 or (sum_A==1 and sum_B!=0)):
        print("Bob")
    else:
        print("Alice")