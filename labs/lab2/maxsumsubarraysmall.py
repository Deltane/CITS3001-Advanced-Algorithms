def maxsumsubarraysmall(nums):
    max_sum = 0  # Initialize the maximum sum as 0
    current_sum = 0  # Initialize the current sum as 0

    for num in nums:
        current_sum = max(num, current_sum + num)  # Update current sum
        max_sum = max(max_sum, current_sum)  # Update max sum if current sum is larger

    return max_sum

def main():
    N = int(input())  # First line input, total number of elements
    nums = list(map(int, input().split()))  # Second line input, the array elements

    result = maxsumsubarraysmall(nums)
    print(result)

main()