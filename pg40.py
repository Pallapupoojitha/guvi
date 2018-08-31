qterms = int(raw_input())
q1 = 1
q2 = 1
count = 0
if nerms == 1:
    print(n1) 
else:
    while count < qterms:
        print q1,
        qth = q1 + q2
        q1 = q2
        q2 = qth
        count = 1
