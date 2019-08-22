T = int(input())
if T<1 or T>1000:
    exit()
sum_N = 0
for t in range(T):
    N = int(input())
    if N<2 or N>100000:
        exit(0)
    sum_N += N
    if sum_N > 1000000:
        exit(0)
    A = [int(x) for x in input().split()]
    if A[0] < 1 or min(A) < 0 or max(A) > N:
        exit(0) 
    tell = 1 #people telling, initially 1
    day = 0
    sum = 0
    i = 0
    tot_sum = sum
    while tot_sum < N-1:
        for j in range (i,tell):
            sum += A[j] #told this many people today
        i = tell #fresh faces next day
        tell += sum #next day this many people gonna tell 
        tot_sum += sum
        #print(tot_sum)
        day += 1
    print(day)