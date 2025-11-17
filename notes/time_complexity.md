# Time Complexity Guide

## Big O Notation

Big O notation describes the upper bound of the growth rate of an algorithm's time or space requirements.

### Common Time Complexities (from best to worst)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access, hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search, array traversal |
| O(n log n) | Linearithmic | Merge sort, quick sort (average) |
| O(n²) | Quadratic | Bubble sort, nested loops |
| O(n³) | Cubic | Triple nested loops |
| O(2ⁿ) | Exponential | Recursive fibonacci, subsets |
| O(n!) | Factorial | Permutations |

## Complexity Comparison

For n = 100:
- O(1) = 1 operation
- O(log n) ≈ 7 operations
- O(n) = 100 operations
- O(n log n) ≈ 700 operations
- O(n²) = 10,000 operations
- O(2ⁿ) = 1.27 × 10³⁰ operations

## Common Data Structure Operations

### Arrays
- Access: O(1)
- Search: O(n)
- Insert: O(n) - worst case (at beginning)
- Delete: O(n) - worst case
- Append: O(1) - amortized

### Linked Lists
- Access: O(n)
- Search: O(n)
- Insert: O(1) - if you have the reference
- Delete: O(1) - if you have the reference

### Hash Tables
- Average Case:
  - Access: N/A
  - Search: O(1)
  - Insert: O(1)
  - Delete: O(1)
- Worst Case: O(n) for all operations

### Binary Search Tree (Balanced)
- Access: O(log n)
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

### Heaps
- Find Min/Max: O(1)
- Insert: O(log n)
- Delete Min/Max: O(log n)
- Build Heap: O(n)

## Tips for Analysis

1. **Drop Constants**: O(2n) → O(n)
2. **Drop Non-Dominant Terms**: O(n² + n) → O(n²)
3. **Different Inputs**: Use different variables (e.g., O(a + b))
4. **Amortized Time**: Consider average case over sequence of operations
5. **Recursive Relations**: Use recursion tree or Master theorem

## Common Patterns

### Two Pointers
```python
# O(n) - single pass through array
left, right = 0, len(arr) - 1
while left < right:
    # process
    left += 1
    right -= 1
```

### Sliding Window
```python
# O(n) - each element visited at most twice
left = 0
for right in range(len(arr)):
    # expand window
    while condition:
        # shrink window
        left += 1
```

### Binary Search
```python
# O(log n) - halving search space each iteration
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Nested Loops
```python
# O(n²) - two nested loops through n elements
for i in range(n):
    for j in range(n):
        # process
```

## Practice Problems

Track your understanding:
- [ ] Identify O(1) operations
- [ ] Analyze simple loops
- [ ] Analyze nested loops
- [ ] Analyze recursive algorithms
- [ ] Understand amortized analysis

