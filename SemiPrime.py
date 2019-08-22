'''
def sieve_of_eras(upper):
    primes = []
    #Always needs to start with 2 (the iterations) so lower limit doesn't have any meaning
    bool_check = [] 
    for i in range(upper): 
        bool_check.append(0) #for ex if say upper = 3 it will be [0,0,0] 0, 1, 2 not 3 cuz BETWEEN 1 AND UPPER 
    for i in range(2,len(bool_check)):
        if bool_check[i] == 0:
            p = i
            n = 2*p
            while (n < upper):
                if bool_check[n] == 0:
                    bool_check[n] = 1
                n+=p                
    for i in range (2,len(bool_check)):
        if bool_check[i] == 0:
            primes.append(i)
    print (primes)
sieve_of_eras(200)
#prints all primes
'''
'''
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
T = int(input())
for t in range(T):
    num = int(input())
    semi = []
    for N in range (3,num + 1):
        temp = 0
        i = 0
        while i < 45 and prime[i] <= N:
            j = i+1
            while j <46 and prime[j] <= N:
                if (prime[i]*prime[j]) > N:
                    break
                if (prime[i]*prime[j]) == N:
                    temp = 1
                    break
                j += 1
            if temp == 1 :
                semi.append(N)
                break
            i += 1
    print(semi)
    #finds semi primes
'''             
semi = [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94,95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155, 158, 159, 161, 166, 177, 178, 183, 185, 187, 194]
#len(semi) = 56
T = int(input())
if T<1 or T>200:
    exit(0)
for t in range(T):
    N = int(input())
    if N<1 or N>200:
        exit(0)
    i = 0
    temp = 0
    while i<56 and semi[i] < N:
        j = 0
        while j<56 and semi[j] < N:
            if (semi[i]+semi[j]) == N:
                temp = 1
                break
            j += 1
        if temp == 1:
            break
        i += 1
    print("YES") if temp == 1 else print("NO")




