#https://www.codechef.com/NOV20B/problems/ADADISH

def solve(n,dishes):
    sorted_dishes = dishes.sort()
    even_i = sorted_dishes[::2]
    odd_i = sorted_dishes[1::2]
    even,odd = sum(even_i),sum(odd_i)
    diffrence = even-odd
    if diffrence>0:
        key = 1
    else:
        diffrence = diffrence*(-1)
        key = 0
    while diffrence > sorted_dishes[-1]:
        if key == 1:
            diffrence -= sorted_dishes[-1]
            odd += sorted.pop()
            key = 0
        else:
            diffrence -= sorted_dishes[-1]
            even += sorted.pop()
            key = 1
    return max(even,odd)

n = int(input())
dishes = list (map (int, input().strip().split()))
print(dishes)
print(solve(n,dishes))