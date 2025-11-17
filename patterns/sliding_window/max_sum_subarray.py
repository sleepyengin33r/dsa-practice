"""
Problem Name: Maximum Sum Subarray of Size K
Platform: GeeksforGeeks
Difficulty: Easy
Pattern: Sliding Window (Fixed Size)
Link: https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k

Description:
-----------
Given an array of integers and a number k, find the maximum sum of a subarray
of size k.

Examples:
--------
Example 1:
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]

Example 2:
Input: arr = [2, 3, 4, 1, 5], k = 2
Output: 7
Explanation: Subarray with maximum sum is [3, 4]

Constraints:
-----------
- 1 <= k <= arr.length <= 10^5
- -10^4 <= arr[i] <= 10^4

Approach:
--------
Use sliding window of fixed size k:
1. Calculate sum of first k elements (initial window)
2. Slide window one element at a time:
   - Add new element entering the window
   - Remove element leaving the window
3. Track maximum sum seen

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only using variables
"""

from typing import List


def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Find maximum sum of any subarray of size k.
    
    Args:
        arr: Input array
        k: Size of subarray
    
    Returns:
        Maximum sum of subarray of size k
    """
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Add new element, remove old element
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def max_sum_subarray_verbose(arr: List[int], k: int) -> int:
    """
    More verbose version showing the sliding window process.
    
    Args:
        arr: Input array
        k: Size of subarray
    
    Returns:
        Maximum sum of subarray of size k
    """
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_start = 0
    window_sum = 0
    max_sum = float('-inf')
    
    for window_end in range(len(arr)):
        # Expand window: add element
        window_sum += arr[window_end]
        
        # Once we hit window size k
        if window_end >= k - 1:
            # Update max sum
            max_sum = max(max_sum, window_sum)
            
            # Shrink window: remove leftmost element
            window_sum -= arr[window_start]
            window_start += 1
    
    return max_sum


# ==================== Test Cases ====================

def test_example_1():
    """Test case 1"""
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    expected = 9  # [5, 1, 3]
    assert max_sum_subarray(arr, k) == expected
    assert max_sum_subarray_verbose(arr, k) == expected
    print("✅ Test 1 passed")


def test_example_2():
    """Test case 2"""
    arr = [2, 3, 4, 1, 5]
    k = 2
    expected = 7  # [3, 4]
    assert max_sum_subarray(arr, k) == expected
    assert max_sum_subarray_verbose(arr, k) == expected
    print("✅ Test 2 passed")


def test_negative_numbers():
    """Test with negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    expected = -3  # [-1, -2]
    assert max_sum_subarray(arr, k) == expected
    print("✅ Negative numbers test passed")


def test_edge_cases():
    """Test edge cases"""
    # Single element
    arr = [5]
    k = 1
    assert max_sum_subarray(arr, k) == 5
    
    # k equals array length
    arr = [1, 2, 3, 4]
    k = 4
    assert max_sum_subarray(arr, k) == 10
    
    # All same elements
    arr = [5, 5, 5, 5]
    k = 2
    assert max_sum_subarray(arr, k) == 10
    
    print("✅ Edge cases passed")


if __name__ == "__main__":
    # Run tests
    test_example_1()
    test_example_2()
    test_negative_numbers()
    test_edge_cases()
    print("\n✨ All tests passed!")
    
    # Demo with detailed output
    print("\n--- Demo ---")
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_sum_subarray(arr, k)
    print(f"Array: {arr}")
    print(f"Window size: {k}")
    print(f"Maximum sum: {result}")

