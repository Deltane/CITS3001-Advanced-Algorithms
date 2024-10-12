import sys
from collections import deque

def readProperties():
    input_line = sys.stdin.readline().split()
    while len(input_line) < 2:
        input_line += sys.stdin.readline().split()
    numProperties, sizeLimit = map(int, input_line)
    properties = []
    for index in range(numProperties):
        while True:
            line = sys.stdin.readline().strip()
            if line:
                value, size = map(int, line.split())
                properties.append({'value': value, 'size': size})
                break
    return numProperties, sizeLimit, properties

def calculateMinTax(numProperties, sizeLimit, properties):
    minTax = [0] * (numProperties + 1)
    totalSize = 0
    start = 0
    maxValues = deque()

    for end in range(numProperties):
        totalSize += properties[end]['size']
        while totalSize > sizeLimit:
            totalSize -= properties[start]['size']
            if maxValues and maxValues[0]['index'] == start:
                maxValues.popleft()
            start += 1
        while maxValues and maxValues[-1]['value'] <= properties[end]['value']:
            maxValues.pop()
        maxValues.append({'value': properties[end]['value'], 'index': end})
        minTax[end + 1] = minTax[start] + maxValues[0]['value']
    return minTax[numProperties]

def main():
    numProperties, sizeLimit, properties = readProperties()
    minTax = calculateMinTax(numProperties, sizeLimit, properties)
    print(minTax)

if __name__ == "__main__":
    main()