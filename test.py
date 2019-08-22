#Always needs to start with 2 (the iterations) so lower limit doesn't have any meaning
primes = []
bool_check = [] 
for i in range(int(input())): 
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