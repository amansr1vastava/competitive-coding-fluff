t = int(input())
while t>0:
    t = t-1
    n = int(input())
    n = n//4

    string = list(map(int, str(input()))) 

    output = str()
    for i in range(n):
        if string[4*i + 0]==0:
            out = ['a','b','c','d','e','f','g','h']
        else:
            out = ['i','j','k','l','m','n','o','p']

        if string[4*i + 1]==0:
            out= out[:4]

        else:
            out= out[4:]

        if string[4*i + 2]==0:
            out= out[:2]

        else:
            out= out[2:]

        if string[4*i + 3]==0:
            out= out[0]

        else:
            out= out[1]

        output = output+str(out)
    print(output)
