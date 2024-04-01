N = int(input())
h = int(N/3600)
m = int(N/60) - 60*h
s = N - 3600*h - 60*m
print(str(h)+":"+str(m)+":"+str(s))