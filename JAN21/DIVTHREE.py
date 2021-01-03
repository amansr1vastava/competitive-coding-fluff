t = int(input())
while t>0:
    n,k,d = map(int, input().split())
    a = map(int, input().split())
    Sum = sum(a)
    quotient = Sum//k
    if quotient<=d:
        print(quotient)
    else:
        print(d)
    t = t-1