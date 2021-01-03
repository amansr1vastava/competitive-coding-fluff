t = int(input())
while t>0:
    n,k,x,y = map(int, input().split())
    if(x==y):
        print(str(n)+' '+ str(n))
    else:
        k = k%4
        a= [[0,0],[0,0],[0,0],[0,0]]
        while(x!=n and y!=n):
            x= x+1
            y=y+1
            a[1][0]=x
            a[1][1]=y
        if(x==n):
            x =x - (n-y)
            y =y + (n-y)
            a[2][0]=x
            a[2][1]=y
            
            y=y-(x-0)
            x=x-(x-0)
            a[3][0]=x
            a[3][1]=y
            
            x=x+(y-0)
            y=y-(y-0)
            a[0][0]=x
            a[0][1]=y
        else:
            y =y- (n-x)
            x =x + (n-x)
            a[2][0]=x
            a[2][1]=y
            
            x=x-(y-0)
            y=y-(y-0)
            a[3][0]=x
            a[3][1]=y
            
            y=y+(x-0)
            x=x-(x-0)
            a[0][0]=x
            a[0][1]=y
        print(str(a[k][0])+' '+str(a[k][1]))
    t = t -1