import sys
def read_properties():
    data = sys.stdin.read().strip().split()
    index = 0
    results = []

    while index < len(data):
        num_properties = int(data[index])
        index += 1
        max_size_limit = int(data[index])
        index += 1
        properties = []
        for i in range(num_properties):
            value = int(data[index])
            index += 1
            size = int(data[index])
            index += 1
            properties.append((value, size))
        min_tax = calculate_min_tax(properties, max_size_limit)
        results.append(min_tax)
    return results

def calculate_min_tax(properties, max_size_limit):
    num_properties = len(properties)
    min_tax_payable = [float('inf')] * (num_properties + 1)
    min_tax_payable[0] = 0

    for end_index in range(1, num_properties + 1):
        max_property_value = 0
        cumulative_size = 0
        current_index = end_index
        while current_index > 0 and cumulative_size + properties[current_index - 1][1] <= max_size_limit:
            cumulative_size += properties[current_index - 1][1]
            max_property_value = max(max_property_value, properties[current_index - 1][0])
            min_tax_payable[end_index] = min(min_tax_payable[end_index],
                                             min_tax_payable[current_index - 1] + max_property_value)
            current_index -= 1
    return min_tax_payable[num_properties]
def main():
    results = read_properties()
    for result in results:
        print(result)

if __name__ == "__main__":
    main()