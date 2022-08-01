
def g1(x):
    x = list(x)
    x.sort(reverse=True)
    return int(''.join(x))

def g2(x):
    x = list(x)
    x.sort()
    return int(''.join(x))

def f(x):
    return g1(x) - g2(x)

N, K = input().split()

tmp = N

for i in range(int(K)):
    tmp = f(str(tmp))

print(tmp)