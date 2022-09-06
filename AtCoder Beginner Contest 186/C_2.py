N = int(input())

count = 0

for i in range(1, N+1):
    str_10n = str(i)
    if '7' in str_10n:
        continue

    int_8n = oct(i)
    str_8n = str(int_8n)
    if '7' in str_8n:
        continue

    count += 1

print(count)