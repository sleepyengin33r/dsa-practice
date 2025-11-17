"""
Problem Name: Two Sum II - Input Array Is Sorted
Platform: LeetCode
Problem Number: #167
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Description:
-----------
Given a 1-indexed array of integers 'numbers' that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific 
target number. Return the indices of the two numbers (1-indexed).

You may not use the same element twice.
Your solution must use only constant extra space.

Examples:
--------
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

Constraints:
-----------
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Only one valid answer exists

Approach:
--------
Use two pointers approach:
1. Start with left pointer at beginning and right pointer at end
2. Calculate sum of elements at both pointers
3. If sum equals target, return indices (1-indexed)
4. If sum is less than target, move left pointer right (need larger sum)
5. If sum is greater than target, move right pointer left (need smaller sum)

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only using two pointers
"""

from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target in sorted array.
    
    Args:
        numbers: Sorted array of integers
        target: Target sum
    
    Returns:
        1-indexed positions of the two numbers
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1
    
    # No solution found (problem guarantees one exists)
    return []


# ==================== Test Cases ====================

def test_example_1():
    """Test case 1: Basic case"""
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    assert two_sum_sorted(numbers, target) == expected
    print("✅ Test 1 passed")


def test_example_2():
    """Test case 2: Middle elements"""
    numbers = [2, 3, 4]
    target = 6
    expected = [1, 3]
    assert two_sum_sorted(numbers, target) == expected
    print("✅ Test 2 passed")


def test_example_3():
    """Test case 3: Negative numbers"""
    numbers = [-1, 0]
    target = -1
    expected = [1, 2]
    assert two_sum_sorted(numbers, target) == expected
    print("✅ Test 3 passed")


def test_edge_cases():
    """Test edge cases"""
    # Two elements only
    numbers = [1, 2]
    target = 3
    assert two_sum_sorted(numbers, target) == [1, 2]
    
    # Negative target
    numbers = [-5, -3, -1, 0, 2]
    target = -4
    assert two_sum_sorted(numbers, target) == [2, 3]
    
    # Large numbers
    numbers = [1, 2, 3, 4, 5, 100, 200]
    target = 300
    assert two_sum_sorted(numbers, target) == [6, 7]
    
    print("✅ Edge cases passed")


if __name__ == "__main__":
    # Run tests
    test_example_1()
    test_example_2()
    test_example_3()
    test_edge_cases()
    print("\n✨ All tests passed!")
    
    # Or run with pytest:
    # pytest two_sum_sorted.py -v

