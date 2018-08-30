p,q=map(int,raw_input().split())
p= p ^ q
q= p ^ q
p= p ^ q
print p,q
