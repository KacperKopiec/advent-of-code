T=[]
while(True):
    a=input()
    print(a)
    if not a:
        break
    T.append(a)

result=0
for k in range(len(T)):
    suma=0
    l=len(T[k])+1
    N=[[0 for i in range(10)] for j in range(l)]
    for i in range(l):
        if(i==0):
            continue
        for j in range(10):
            N[i][j]=N[i-1][j]
        N[i][ord(T[k][i-1])-ord('0')]+=1
    j=12
    start=1
    while(j>0):
        i=9
        while(i>=0):
            assert l-j >= 0 and i < 10 and i >= 0 and start - 1 >= 0 and start - 1 < l
            if(N[l-j][i]-N[start-1][i]>0):
                while(ord(T[k][start-1])-ord('0')!=i):
                    start+=1
                suma=suma*10+i
                start+=1
                break
            else:
                i=i-1     
        j=j-1
    result+=suma
print(result)