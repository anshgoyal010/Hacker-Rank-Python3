m=int(input())
am=set(map(int,input().split()))
n=int(input())
an=set(map(int,input().split()))
c=an.difference(am)
d=am.difference(an)
c.update(d)
#c=int(list(c))
c=sorted(c)
for i in (c):
    print(i)
