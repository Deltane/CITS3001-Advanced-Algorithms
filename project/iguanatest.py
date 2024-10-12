def run_test_case(input_data, expected_output):
    import subprocess

    # Create a subprocess to run your Python script, pipe input and capture output
    process = subprocess.Popen(['python', 'iguana.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)

    # Send input data and get the output
    output, errors = process.communicate(input=input_data)
    if process.returncode != 0:
        print(f"Error running test case:\n{errors}")
        return False

    # Compare program output with expected output
    if output.strip() == expected_output.strip():
        return True
    else:
        print(f"Test failed!\nExpected: {expected_output.strip()}\nGot: {output.strip()}")
        return False

def main():
    test_cases = [
        ("2\n..\n..", "0"),  # Example input and expected output
        ("2\n.#\n#.", "-1"),
        ("3\n...\n...\n...", "1"),
        # Add more test cases here
    ]

    # Run all test cases
    for i, (input_data, expected) in enumerate(test_cases, 1):
        print(f"Running test case {i}...", end=" ")
        if run_test_case(input_data, expected):
            print("Passed!")
        else:
            print("Failed!")

if __name__ == '__main__':
    main()
