# 基準値
s = 753

array = list(input())

# 1234567890

arrays = []
for i in range(len(array) -2 ):
    arrays.append(array[i:i+3])

points = []
for arr in arrays:
    tmp = abs(s - int(''.join(arr)))
    points.append(tmp)

print(min(points))
