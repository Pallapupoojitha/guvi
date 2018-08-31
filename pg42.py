m1,m2=map(str,raw_input().split())
n1=len(m1)
n2=len(m2)
if n1==n2:
         if m1==m2:
                  print m1
         elif m1>m2:
                  print m1
         else:
                  print m2
elif n1>n2:
       print m1
else:
       print m2
        
