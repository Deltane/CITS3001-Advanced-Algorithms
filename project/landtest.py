import sys
from collections import deque
from io import StringIO

def readProperties():
    input_line = sys.stdin.readline().split()
    numProperties, sizeLimit = map(int, input_line)
    properties = []
    for index in range(numProperties):
        line = sys.stdin.readline().strip()
        value, size = map(int, line.split())
        properties.append({'value': value, 'size': size})
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

def test_with_input(input_string):
    """Helper function to redirect stdin for testing purposes."""
    old_stdin = sys.stdin
    try:
        sys.stdin = StringIO(input_string)
        numProperties, sizeLimit, properties = readProperties()
        result = calculateMinTax(numProperties, sizeLimit, properties)
        return result
    finally:
        sys.stdin = old_stdin

def main():
    # Test Case 1
    input1 = "3 3\n1 1\n2 2\n3 3\n"
    expected1 = 5
    output1 = test_with_input(input1)
    print(f"Test 1 Passed: {output1 == expected1} - Output: {output1}, Expected: {expected1}")

    # Test Case 2
    input2 = "4 5\n2 4\n2 4\n1 2\n3 3\n"
    expected2 = 7
    output2 = test_with_input(input2)
    print(f"Test 2 Passed: {output2 == expected2} - Output: {output2}, Expected: {expected2}")

if __name__ == "__main__":
    main()