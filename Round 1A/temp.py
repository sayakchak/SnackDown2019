T = int(input())
if T<1 or T>100:
    exit(0)
L = ['d', 'f']
R = ['j','k']
for t in range(T):
    N = int(input())
    if N<1 or N>100:
        exit(0)
    S = {}
    #time = 0
    time = N*0.2
    for i in range(N):
        w = input()
        for p_ in w:
            if p_!='d' and p_!='f' and p_ != 'j' and p_ != 'k':
                exit(0)
        l = len(w)
        if l>20:
            exit(0)
        if w in S:
            time += S[w]/2
        else:
            i = 1
            t = 'L' if w[0] in L else 'R'
            lop = 'L' if w[0] in L else 'R'
            #t_time = 0.2
            t_time = 0
            while i<l:
                lop = 'L' if w[i] in L else 'R'
                if lop == t:
                    t_time += 0.4
                else:
                    t_time += 0.2
                    t = lop
                i += 1
            S[w] = t_time
            time += t_time
    '''
    x = time*10
    if (x - int(x) == 0.0):
        print(int(x))
    else:
        print(x)
    '''
    #print(S)
    print(int(time*10))