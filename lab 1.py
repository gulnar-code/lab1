x=0.7
n=1
p=0
eps=0.01
while x**n/n>eps:
    p=p-x**n/n
    n=n+1
print(p)
