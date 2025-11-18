"""
Problem Name: Maximum Sum Subarray of Size K
Platform: GeeksforGeeks
Difficulty: Easy
Pattern: Sliding Window (Fixed Size)
Link: https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k


Approach:
--------
Use sliding window of fixed size k:
1. Move till window end is less than length of array
2. keep adding the rightmost element to the window sum
3. window size is not reached, move the window end to the right
4. window size is reached, calculate the maximum sum and slide the window by removing the leftmost element

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only using variables
"""


def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Find maximum sum of any subarray of size k.

    Args:
        arr: Input array
        k: Size of subarray

    Returns:
        Maximum sum of subarray of size k
    """
    # edge cases
    if not arr or k <= 0 or k > len(arr):
        return 0

    window_start = 0
    window_end = 0
    window_sum = 0
    max_sum = float("-inf")

    # move till window end is less than length of array
    while window_end < len(arr):
        window_sum += arr[window_end]
        # window size is not reached
        if window_end - window_start + 1 < k:
            window_end += 1
            # window size is reached
        elif window_end - window_start + 1 == k:
            # do the calculation
            max_sum = max(max_sum, window_sum)
            #   slide the window by removing the leftmost element and adding the rightmost element
            window_sum = window_sum - arr[window_start]
            window_start += 1
            window_end += 1
    # return the maximum sum
    return int(max_sum)


# ==================== Test Cases ====================


def test_example_1():
    """Test case 1"""
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    expected = 9  # [5, 1, 3]
    assert max_sum_subarray(arr, k) == expected
    print("✅ Test 1 passed")


def test_example_2():
    """Test case 2"""
    arr = [2, 3, 4, 1, 5]
    k = 2
    expected = 7  # [3, 4]
    assert max_sum_subarray(arr, k) == expected
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
