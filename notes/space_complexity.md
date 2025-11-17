# Space Complexity Guide

## What is Space Complexity?

Space complexity measures the total amount of memory an algorithm needs relative to the input size.

## Components of Space Complexity

1. **Auxiliary Space**: Extra space used by the algorithm (excluding input)
2. **Input Space**: Space used to store the input

Usually, when we talk about space complexity, we mean **auxiliary space**.

## Common Space Complexities

| Notation | Description | Example |
|----------|-------------|---------|
| O(1) | Constant | Only using fixed variables |
| O(log n) | Logarithmic | Recursive call stack for binary search |
| O(n) | Linear | Creating a copy of the array |
| O(n²) | Quadratic | 2D matrix of size n×n |

## Analysis Tips

### What Counts Towards Space?
✅ Variables created
✅ Data structures (arrays, hash maps, etc.)
✅ Call stack (for recursion)
✅ Dynamic memory allocation

❌ Input space (usually excluded)
❌ Reusing input space

## Common Patterns

### O(1) Space - Constant
```python
def find_max(arr):
    max_val = arr[0]  # Single variable
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
# Space: O(1) - only using one variable
```

### O(n) Space - Linear
```python
def create_frequency_map(arr):
    freq = {}  # Hash map can grow to size n
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
# Space: O(n) - hash map with n unique elements
```

### O(log n) Space - Logarithmic (Recursion)
```python
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
# Space: O(log n) - call stack depth is log n
```

### O(n) Space - Recursive Call Stack
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# Space: O(n) - n recursive calls on stack
```

## In-Place Algorithms

**In-place** means the algorithm uses O(1) extra space (not counting input).

### Example: Reverse Array In-Place
```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
# Space: O(1) - modifying input array
```

### Example: Not In-Place
```python
def reverse_copy(arr):
    return arr[::-1]  # Creates new array
# Space: O(n) - new array created
```

## Recursion vs Iteration

### Recursive (Uses Call Stack)
```python
def sum_recursive(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + sum_recursive(arr, index + 1)
# Space: O(n) due to call stack
```

### Iterative (Usually More Space Efficient)
```python
def sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Space: O(1)
```

## Common Data Structures Space

### Hash Map / Set
```python
seen = set()  # O(n) in worst case
for num in arr:
    seen.add(num)
```

### Queue / Stack
```python
from collections import deque
queue = deque()  # O(k) where k is max size
```

### 2D Matrix
```python
matrix = [[0] * n for _ in range(n)]  # O(n²)
```

## Optimization Techniques

1. **Reuse Variables**: Don't create unnecessary copies
2. **In-place Modifications**: Modify input when allowed
3. **Iterative vs Recursive**: Iteration often uses less space
4. **Sliding Window**: Instead of storing all subarrays
5. **Two Pointers**: Instead of creating new arrays

## Practice Checklist

- [ ] Identify constant space solutions
- [ ] Count variables and data structures
- [ ] Analyze recursive call stack depth
- [ ] Convert recursive to iterative solutions
- [ ] Implement in-place algorithms

