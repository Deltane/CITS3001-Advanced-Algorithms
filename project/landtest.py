def run_test():
    import subprocess

    # Running the main script and capturing the output
    output = subprocess.run(['python', 'land.py'], input=open('test_input.txt', 'r').read(), text=True, capture_output=True).stdout

    # Reading expected output
    with open('expected_output.txt', 'r') as file:
        expected_output = file.read().strip()

    # Comparing expected output with actual output
    if output.strip() == expected_output:
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(output.strip())

run_test()