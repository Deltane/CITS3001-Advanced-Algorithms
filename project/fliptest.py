import subprocess
import os
import random
import time

# MAKE SURE YOU'RE IN THE RIGHT DIRECTORY
filename = "flip.py"
numTests = 1
rows = 7
cols = 7

# =============================
path = os.getcwd()
file_path = os.path.join(path, filename)
beginning = time.time()

while numTests > 0:
    values = [["." if random.random() < 0.6 else "#" for c in range(cols)] for r in range(rows)]
    question = f"{rows} {cols}\n{"\n".join(["".join(values[c]) for c in range(rows)])}"
    answer = "idkbro\n"

    print(question)

    result = subprocess.run(['python3', file_path], input=question, capture_output=True, text=True, check=False)
    stdout = result.stdout

    end = time.time()
    print(f"Input: \n{question}")
    print(f"Expected: \n{answer}")
    print(f"Received: \n{stdout}")
    if result.stderr:
        print(result.stderr)
    print(f"process ended in {end - beginning} time")

    numTests -= 1