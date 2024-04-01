T = int(input())
a = int(T/365)
f = T/365
c = round((f - a)*365)
m = int(c/30)
b = c/30
d = round((b - m)*30)
print(str(a)+" ano(s)")
print(str(m)+" mes(es)")
print(str(d)+" dia(s)")