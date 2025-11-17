# Two Pointers Pattern

## Overview

The Two Pointers pattern is used when you need to search for pairs or elements in an array/list, typically when the array is sorted or when you need to process elements from both ends.

## When to Use

- Working with sorted arrays
- Finding pairs that satisfy a condition
- Removing duplicates in-place
- Comparing elements from both ends
- Palindrome problems

## Time Complexity

- **Time**: O(n) - typically single pass
- **Space**: O(1) - only using pointers

## Template

### Pattern 1: Opposite Direction (Converging)

```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process current pair
        if condition_met(arr[left], arr[right]):
            return result
        elif need_larger_value:
            left += 1
        else:
            right -= 1
    
    return default_result
```

### Pattern 2: Same Direction (Fast & Slow)

```python
def two_pointers_same_direction(arr):
    slow = 0
    
    for fast in range(len(arr)):
        if condition:
            arr[slow] = arr[fast]
            slow += 1
    
    return slow  # or arr[:slow]
```

## Common Problems

### Beginner
- [ ] Two Sum II (Sorted Array)
- [ ] Valid Palindrome
- [ ] Remove Duplicates from Sorted Array
- [ ] Move Zeroes

### Intermediate
- [ ] 3Sum
- [ ] Container With Most Water
- [ ] Trapping Rain Water
- [ ] Sort Colors

### Advanced
- [ ] 4Sum
- [ ] Minimum Window Substring
- [ ] Longest Substring Without Repeating Characters

## Problem List in This Directory

1. `two_sum_sorted.py` - Find two numbers that sum to target
2. (Add more as you solve them)

## Tips

1. **Sorted Arrays**: If the array is sorted, two pointers is often the right choice
2. **In-place Modification**: Use two pointers to avoid creating new arrays
3. **Direction Matters**: Choose opposite or same direction based on the problem
4. **Boundary Conditions**: Be careful with `left <= right` vs `left < right`
5. **Multiple Passes**: Sometimes you need multiple two-pointer passes

## Related Patterns

- **Sliding Window**: Uses two pointers but maintains a "window" of elements
- **Fast & Slow Pointers**: Used for cycle detection in linked lists

