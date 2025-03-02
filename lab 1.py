x=1
n=1
f=0
k=1
m=-1
while k<=2*n-1:
    m=-1*m
    h=m*((x**k)/k)
    f=f+h
    k=k+1
    print(h)