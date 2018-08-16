hr1,min1=map(int,raw_input().split())
hr2,min2=map(int,raw_input().split())
s1=hr1*60+min1
s2=hr2*60+min2
diff=abs(s1-s2)
time=diff%60
time1=(diff-time)//60
print time1,time
