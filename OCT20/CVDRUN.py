#https://www.codechef.com/OCT20B/problems/CVDRUN
def solver():
    Y = "YES"
    N = "NO"
    n,k,x,y = map(int,input().split())
    if k == 1 or x == y:
        return Y
    if k == 0:
        return N
    se = set()
    se.add(x)
    x = (x+k)%n
    while x != y:
        if x in se:
            break
        se.add(x)
        x = (x+k)%n
    return Y if x == y else N
        
for _ in range(int(input())):
    print(solver())