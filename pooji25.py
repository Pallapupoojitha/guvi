def median(1,n):
       l.sort()
       if n%2==0:
                     return l[n/2]
        else:
                     return(l[n/2-1]+l[n/2])/2
n=int(raw_input())
i=[int(x) for  in raw_input().split()]
print(median(1,n-1))
