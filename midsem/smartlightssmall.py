def smartlights(n, x):
    x = list(x)
    presses = 0

    for i in range(1, n - 1):
        if x[i] == '1':
            presses += 1
            x[i - 1] = '0' if x[i - 1] == '1' else '1'
            x[i] = '0' if x[i] == '1' else '1'
            if i + 1 < n:
                x[i + 1] = '0' if x[i + 1] == '1' else '1'

    # Check the last two lights which we can influence
    if x[-1] == '1' or x[-2] == '1':
        return -1

    return presses

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    X = data[1]

    result = smartlights(N, X)
    print(result)

if __name__ == "__main__":
    main()