def smartlights(n, x):
    x = list(x)
    presses = 0

    for i in range(1, n - 1):
        if x[i] == '1':
            presses += 1
            x[i - 1] = '0' if x[i - 1] == '1' else '1'
            x[i] = '0' if x[i] == '1' else '1'
            x[i + 1] = '0' if x[i + 1] == '1' else '1'

    if x[-2] == '1' or x[-3] == '1':
        return -1

    return presses


N = int(input().strip())
X = input().strip()

result = smartlights(N, X)
print(result)

