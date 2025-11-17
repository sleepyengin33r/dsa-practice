# Getting Started with DSA Practice

Welcome to your Data Structures and Algorithms practice repository! This guide will help you start solving problems effectively.

## 🚀 Quick Start

### 1. Set Up Your Environment

```bash
# Navigate to the repository
cd dsa-practice

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Example Problems

Try running the example problems to see the structure:

```bash
# Run a pattern-based problem
python patterns/two_pointers/two_sum_sorted.py

# Run a sliding window problem
python patterns/sliding_window/max_sum_subarray.py

# Run a data structure implementation
python data_structures/linked_lists/singly_linked_list.py
```

### 3. Create Your First Problem

Copy the template and start solving:

```bash
# Copy the template
cp templates/problem_template.py patterns/two_pointers/my_problem.py

# Edit the file with your solution
# Run your solution
python patterns/two_pointers/my_problem.py
```

## 📝 Problem-Solving Workflow

### Step 1: Choose Where to Place Your Solution

Decide which directory fits best:

- **By Pattern**: `patterns/two_pointers/`, `patterns/sliding_window/`, etc.
- **By Data Structure**: `data_structures/arrays/`, `data_structures/trees/`, etc.
- **By Difficulty**: `problems/easy/`, `problems/medium/`, `problems/hard/`
- **By Algorithm**: `algorithms/dynamic_programming/`, `algorithms/sorting/`, etc.

💡 **Tip**: You can place the same problem in multiple directories or use symbolic links!

### Step 2: Use the Template

Start with `templates/problem_template.py`:

```python
"""
Problem Name: Two Sum
Platform: LeetCode
Problem Number: #1
Difficulty: Easy
Pattern: Hash Table
Link: https://leetcode.com/problems/two-sum/

Description:
-----------
Given an array of integers nums and an integer target, return indices
of the two numbers that add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def solution(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def test_solution():
    assert solution([2, 7, 11, 15], 9) == [0, 1]
    assert solution([3, 2, 4], 6) == [1, 2]
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_solution()
```

### Step 3: Test Your Solution

Run tests directly:
```bash
python your_problem.py
```

Or use pytest for more detailed testing:
```bash
pytest your_problem.py -v
pytest patterns/ -v  # Run all tests in patterns directory
```

### Step 4: Track Your Progress

Update the README.md progress checklist as you complete problems!

## 🎯 Recommended Learning Path

### Week 1-2: Master the Basics
1. **Arrays & Strings**
   - Two Pointers pattern (5-10 problems)
   - Sliding Window pattern (5-10 problems)

2. **Linked Lists**
   - Implement singly linked list
   - Fast & Slow Pointers pattern
   - In-place Reversal pattern

### Week 3-4: Trees and Graphs
3. **Binary Trees**
   - Tree BFS pattern (level order traversal)
   - Tree DFS pattern (pre/in/post order)

4. **Graphs**
   - BFS and DFS implementations
   - Common graph problems

### Week 5-6: Advanced Topics
5. **Heaps & Priority Queues**
   - Top K Elements pattern
   - Two Heaps pattern

6. **Dynamic Programming**
   - Start with classic problems (fibonacci, climbing stairs)
   - Memoization → Tabulation

### Week 7-8: Polish Skills
7. **Backtracking**
   - Subsets pattern
   - Permutations and combinations

8. **Advanced Patterns**
   - Modified Binary Search
   - K-way Merge

## 📚 Using Helper Functions

The repository includes helpful utilities:

### Test Helpers
```python
from utils.test_helpers import create_linked_list, print_tree

# Create linked list from array
head = create_linked_list([1, 2, 3, 4, 5])

# Create binary tree
root = create_binary_tree([1, 2, 3, None, None, 4, 5])

# Print tree structure
print_tree(root)
```

### Common Utilities
```python
from utils.common import timing_decorator

@timing_decorator
def my_solution(arr):
    # Your solution
    pass

# This will print execution time
my_solution([1, 2, 3, 4, 5])
```

## 🧪 Testing Best Practices

### 1. Test Different Cases
- **Basic cases**: Normal input
- **Edge cases**: Empty, single element, maximum size
- **Boundary cases**: Min/max values
- **Special cases**: Duplicates, negative numbers

### 2. Use Assertions
```python
def test_my_solution():
    # Test basic case
    assert solution([1, 2, 3]) == expected_result
    
    # Test edge case
    assert solution([]) == []
    
    # Test with custom message
    result = solution([1, 2, 3])
    assert result == expected, f"Expected {expected}, got {result}"
```

### 3. Parametrized Testing with Pytest
```python
import pytest

@pytest.mark.parametrize("input_data,expected", [
    ([1, 2, 3], 6),
    ([0], 0),
    ([-1, -2], -3),
])
def test_sum(input_data, expected):
    assert sum_array(input_data) == expected
```

## 📊 Analyzing Complexity

Always analyze and document:

### Time Complexity Examples
```python
# O(1) - Constant
def get_first(arr):
    return arr[0]

# O(log n) - Logarithmic
def binary_search(arr, target):
    # Halving search space each iteration
    pass

# O(n) - Linear
def linear_search(arr, target):
    for item in arr:  # Single loop
        if item == target:
            return True

# O(n log n) - Linearithmic
def merge_sort(arr):
    # Sorting algorithms
    pass

# O(n²) - Quadratic
def bubble_sort(arr):
    for i in range(len(arr)):  # Nested loops
        for j in range(len(arr)):
            pass
```

### Space Complexity
```python
# O(1) - Constant space
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    # Only using two variables

# O(n) - Linear space
def create_copy(arr):
    return arr[:]  # New array of size n
```

## 💡 Tips for Success

1. **Consistency > Intensity**: Solve 1-2 problems daily rather than 20 in one day
2. **Understand, Don't Memorize**: Focus on understanding patterns
3. **Code Without Looking**: Try to implement from memory after learning
4. **Review Regularly**: Revisit problems after 1 week, 1 month
5. **Time Yourself**: Practice under timed conditions
6. **Explain Your Approach**: Write comments or explain out loud
7. **Learn from Mistakes**: When stuck, analyze why
8. **Track Progress**: Update your README checklist

## 🔗 Additional Resources

### Online Judges
- [LeetCode](https://leetcode.com) - Most popular, great for interviews
- [HackerRank](https://www.hackerrank.com) - Good for basics
- [Codeforces](https://codeforces.com) - Competitive programming
- [GeeksforGeeks](https://www.geeksforgeeks.org) - Comprehensive explanations

### Learning Resources
- [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview) - Pattern-based approach
- [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) - Essential problems
- [NeetCode](https://neetcode.io) - Video explanations

### Reference
- Time/Space Complexity: See `notes/time_complexity.md`
- Patterns Guide: See `notes/pattern_notes.md`

## 🎓 Example Study Schedule

### Daily (1-2 hours)
- 📖 15 min: Review pattern notes
- 💻 45 min: Solve 1-2 new problems
- 🔄 30 min: Review previous problems

### Weekly Review
- ✅ Review solved problems
- 📝 Update progress tracking
- 🎯 Identify weak areas
- 📚 Deep dive into one topic

## 🤝 Contributing to Your Repository

As you solve problems, consider:

1. **Document Patterns**: Add notes about what you learned
2. **Create READMEs**: Add README.md in subdirectories
3. **Optimize Solutions**: Come back and improve your code
4. **Add Test Cases**: Improve test coverage
5. **Write Helpers**: Create utility functions you use often

## ❓ Need Help?

1. Check `notes/` directory for complexity and pattern guides
2. Look at example problems in `patterns/` directories
3. Review pattern-specific README files
4. Use the templates in `templates/` directory

---

Happy Coding! 🚀 Remember: Everyone struggles at first. Persistence is key!

