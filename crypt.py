def prime(n):
    primes = [False for x in range(n+1)]
    for i in range(2,n+1):
        if primes[i]==False:
            j = 2*i
            while(j<=n):
                primes[j] = True
                j+=i
    return primes
def prime_fact(n,sieve):
    for i in range(3,int(n**5)):
        if sieve[i]==False and n%i == 0:
            return [i,int(n/i)]
    
    
if __name__ == "__main__":
    N = [x for x in range(100)]
    L = [x for x in range(100)]
    prime_factor = [[0,0] for i in range(100)]
    T = int(input())
    ll = []
    max = 0
    alphabets = {}
    output = ""
    for test in range(T):
        N[test],L[test] = map(int,input().split())
        if N[test]>max: max = N[test]
        ll.append(input())
    sieve = prime(max)
    for test in range(T):
        l = [int(x) for x in ll[test].split(" ")]
        for i in range (L[test]): prime_factor[i] = prime_fact(l[i],sieve)
        for i in range (L[test]-1):
            if prime_factor[i][0]==prime_factor[i+1][0]:
                prime_factor[i][0],prime_factor[i][1] = prime_factor[i][1],prime_factor[i][0]
            elif prime_factor[i][0]==prime_factor[i+1][1]:
                (prime_factor[i][0],prime_factor[i][1]) = (prime_factor[i][1],prime_factor[i][0])
                (prime_factor[i+1][0],prime_factor[i+1][1]) = (prime_factor[i+1][1],prime_factor[i+1][0])
            elif prime_factor[i][1]==prime_factor[i+1][1]:
                (prime_factor[i+1][0],prime_factor[i+1][1]) = (prime_factor[i+1][1],prime_factor[i+1][0])
        #print(prime_factor)
        temp = []
        for i in range(L[test]):
            temp.append(prime_factor[i][0])
            temp.append(prime_factor[i][1])
        s = set(temp)
        temp = []
        for S in s: temp.append(S)
        print(temp)
        temp.sort()
        count = 0
        for S in temp:
            alphabets[S] = chr(count+65)
            count+=1
        #print(alphabets)
        output+="\nCase #"+str(test)+": "
        for i in range (L[test]):
            #print(alphabets[prime_factor[i][0]])
            output+=alphabets[prime_factor[i][0]]
        output+=alphabets[prime_factor[L[test]-1][1]]
    print(output)        
    
    


