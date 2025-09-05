#Your current code has O(n) time complexity and O(k) space complexity 
# where k is the number of unique elements. Here are several optimized approaches 
# depending on your specific needs:

# find the unique numbers in the array
numbers = [1,1,1,1,2,3,1,2,6]

# Answer 







from collections import Counter, defaultdict

# Method 0: Optimize solution using dict
def find_unique_number(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    return [key for key, value in count.items() if value == 1] # O(n) time, O(k) space




# Method 1: Using Counter
def find_unique_counter(arr):
    count = Counter(arr)
    return [num for num, freq in count.items() if freq == 1]

# Method 2: Two-pass approach
def find_unique_two_pass(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Second pass: collect unique numbers in order of first appearance
    unique = []
    seen = set()
    for num in arr:
        if count[num] == 1 and num not in seen:
            unique.append(num)
            seen.add(num)
    
    return unique

# Method 3: Single pass with set tracking
def find_unique_single_pass(arr):
    seen_once = set()
    seen_multiple = set()
    
    for num in arr:
        if num in seen_once:
            seen_once.remove(num)
            seen_multiple.add(num)
        elif num not in seen_multiple:
            seen_once.add(num)
    
    return [num for num in arr if num in seen_once]

# Method 4: For sorted arrays or when order doesn't matter
def find_unique_sorted(arr):
    if not arr:
        return []
    
    arr_sorted = sorted(arr)
    unique = []
    
    i = 0
    while i < len(arr_sorted):
        if i == len(arr_sorted) - 1 or arr_sorted[i] != arr_sorted[i + 1]:
            if i == 0 or arr_sorted[i] != arr_sorted[i - 1]:
                unique.append(arr_sorted[i])
        i += 1
    
    return unique

# Method 5: XOR approach variations for multiple unique elements
def find_single_unique_xor(arr):
    """Only works when there's exactly one number that appears once"""
    result = 0
    for num in arr:
        result ^= num
    return result

def find_two_unique_xor(arr):
    """Works when there are exactly TWO numbers that appear once"""
    # XOR all elements - result will be XOR of the two unique numbers
    xor_all = 0
    for num in arr:
        xor_all ^= num
    
    # Find rightmost set bit to distinguish the two numbers
    rightmost_bit = xor_all & -xor_all
    
    # Divide numbers into two groups and XOR each group
    first_unique = 0
    second_unique = 0
    
    for num in arr:
        if num & rightmost_bit:
            first_unique ^= num
        else:
            second_unique ^= num
    
    return [first_unique, second_unique]

# Method 6: Early termination optimization
def find_unique_early_stop(arr, max_unique=None):
    """Stops early if we find the desired number of unique elements"""
    count = {}
    unique_found = []
    
    # First pass: count all elements
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Second pass: collect unique elements (with early stop option)
    for num in arr:
        if count[num] == 1 and num not in unique_found:
            unique_found.append(num)
            if max_unique and len(unique_found) >= max_unique:
                break
    
    return unique_found

# Method 7: Memory-optimized streaming approach (for very large datasets)
def find_unique_streaming(arr):
    """Most memory efficient - processes elements as they come"""
    from collections import defaultdict
    
    # Use defaultdict to avoid .get() calls
    count = defaultdict(int)
    for num in arr:
        count[num] += 1
    
    # Generator expression for memory efficiency
    return [num for num in arr if count[num] == 1 and arr.index(num) == arr.index(num)]

# Actually, let's fix method 7 to avoid the index issue:
def find_unique_streaming_fixed(arr):
    """Memory efficient with proper order preservation"""
    from collections import defaultdict
    
    count = defaultdict(int)
    for num in arr:
        count[num] += 1
    
    seen = set()
    result = []
    for num in arr:
        if count[num] == 1 and num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test all methods
print("Original array:", numbers)
print("Method 0 (Dict):", find_unique_number(numbers))
print("Method 1 (Counter):", find_unique_counter(numbers))
print("Method 2 (Two-pass):", find_unique_two_pass(numbers))
print("Method 3 (Single-pass):", find_unique_single_pass(numbers))
print("Method 4 (Sorted):", find_unique_sorted(numbers))

# Test all methods including multiple unique elements
print("Original array:", numbers)
print("Method 0 (Dict):", find_unique_number(numbers))
print("Method 1 (Counter):", find_unique_counter(numbers))
print("Method 2 (Two-pass):", find_unique_two_pass(numbers))
print("Method 3 (Single-pass):", find_unique_single_pass(numbers))
print("Method 4 (Sorted):", find_unique_sorted(numbers))
print("Method 7 (Streaming):", find_unique_streaming_fixed(numbers))

# Test with exactly one unique number
xor_test_one = [1,1,2,2,3]
print(f"Single unique XOR with {xor_test_one}:", find_single_unique_xor(xor_test_one))

# Test with exactly two unique numbers
xor_test_two = [1,1,2,2,3,4]
print(f"Two unique XOR with {xor_test_two}:", find_two_unique_xor(xor_test_two))

# Test early termination
print(f"Early stop (max 2) with {numbers}:", find_unique_early_stop(numbers, max_unique=2))

# Test with more unique elements
multiple_unique = [1,1,2,2,3,4,5,6,7,7,8,8]
print(f"Multiple unique elements {multiple_unique}:")
print("  Standard approach:", find_unique_counter(multiple_unique))
print("  Early stop (max 3):", find_unique_early_stop(multiple_unique, max_unique=3))

# Performance comparison
import time

def benchmark_methods(arr, iterations=10000):
    methods = [
        ("Dict", find_unique_number),
        ("Counter", find_unique_counter),
        ("Two-pass", find_unique_two_pass), 
        ("Single-pass", find_unique_single_pass),
        ("Sorted", find_unique_sorted),
        ("Streaming", find_unique_streaming_fixed)
    ]
    
    print(f"\nBenchmarking with {len(arr)} elements, {iterations} iterations:")
    
    for name, func in methods:
        start = time.time()
        for _ in range(iterations):
            func(arr)
        end = time.time()
        print(f"{name}: {(end - start) * 1000:.2f} ms")

# Test with larger array
large_array = [1,1,1,1,2,3,1,2,6] * 1000
benchmark_methods(large_array)