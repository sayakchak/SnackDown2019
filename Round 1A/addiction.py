import psycho
psycho.full()
T = int(input())
if T<1 or T>1000:
    exit(0)
for t in range(T):
    a,b,c = [int(x) for x in input().split()]
    if a<1 or b<1 or c<1 or a> 10**9 or b>10**9 or c> 10**9 or ((a+b)!=c):
        exit(0)
    count = 1
    c_l = 0
    A = "{0:b}".format(a)
    B = "{0:b}".format(b)
    x_1 = 0
    y_1 = 0
    A_1 = 0
    B_1 = 0
    for a in A:
        if a == '1':
            A_1 += 1
    for a in B:
        if a == '1':
            B_1 += 1
    for i in range (1,c):
        x = ["{0:b}".format(i),"{0:b}".format(c-i)]
        x_1 = 0
        y_1 = 0
        for a in x[0]:
            if a == '1':
                x_1 += 1
        for a in x[1]:
            if a == '1':
                y_1 += 1
        if x_1 == A_1 and y_1 == B_1:
            c_l += 1
    print(c_l)
'''        
if c_l > 0:
    A = A*3
    B = B*3
    for x in C:
        if x[0] in A and x[1] in B:
            count += 1
print(count)
'''