# Maximum Contiguous Subsequence Sum (MCSS)

This Python script finds the **Maximum Contiguous Subsequence Sum (MCSS)** within a randomly generated list of integers using an optimized approach similar to **Kadane's Algorithm**.

## How It Works

1. A list (`vector`) of 1000 random integers between -100 and 100 is generated.
2. The `MCSS` function iterates through the list to determine the contiguous subarray with the highest sum.
3. The function returns:
   - The maximum sum.
   - The starting index of the subarray.
   - The ending index of the subarray.
4. The results are printed to the console.

## Code Explanation

```python
import random

def MCSS(v):
    largest, acc = float('-inf'), 0
    start = end = temp_start = 0  # Track indices

    for i, num in enumerate(v):
        if num > acc + num:
            acc = num
            temp_start = i  # Start new subsequence
        else:
            acc += num  # Add to current subsequence

        if acc > largest:
            largest = acc
            start = temp_start  # Update best start index
            end = i  # Update best end index
    return largest, start, end  # Return sum and indices

# Generate a random list of integers
vector = [random.randint(-100, 100) for _ in range(1000)]

# Find the maximum contiguous subsequence sum
max_sum, start_index, end_index = MCSS(vector)

# Output results
print(f"Maximum Contiguous Subsequence Sum: {max_sum}")
print(f"Starting Index: {start_index}")
print(f"Ending Index: {end_index}")
