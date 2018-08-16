hr1,min1=map(int,raw_input().split())
hr2,min2=map(int,raw_input().split())
p1=hr1*60+min1
p2=hr2*60+min2
diff=abs(p1-p2)
time=diff%60
time1=(diff-time)//60
print time1,time
