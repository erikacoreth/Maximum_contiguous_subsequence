#Erika Coreth

import random

def MCSS(v):
    largest, acc = float('-inf'), 0
    start = end = temp_start = 0 #track indices

    for i, num in enumerate(v):
        if num > acc + num:
            acc = num
            temp_start = i #start new subsequence
        else:
            acc += num #add to current subsequence

        if acc > largest:
            largest = acc
            start = temp_start #update best start index
            end = i #update best end index
    return largest, start, end #return sum and indices


vector = [random.randint(-100, 100) for _ in range(1000)]

max_sum, start_index, end_index = MCSS(vector)

print(f"Maximum Contiguous Subsequence Sum: {max_sum}")
print(f"Starting Index: {start_index}")
print(f"Ending Index: {end_index}")