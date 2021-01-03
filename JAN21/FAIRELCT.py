t = int(input())
while t>0:
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = sum(a)
    sum_b = sum(b)
    count = 0
    if sum_a>sum_b:
        print('0')
    else:
        a.sort()
        b.sort()
        for i in range(min(m,n)):
            sum_a = sum_a - a[i] + b[-(i+1)]
            sum_b = sum_b - b[-(i+1)] +a[i]
            if sum_a>=sum_b:
                count = count+1
                break
            else:
                count = count+1
        if sum_a>=sum_b:
            print(count)
        else:
            print('-1')
    t = t -1
        
        
