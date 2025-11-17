# Problem-Solving Patterns

A comprehensive guide to common algorithmic patterns for coding interviews.

## 1. Two Pointers

**When to Use:**
- Problems with sorted arrays or linked lists
- Need to find pairs or triplets
- Comparing elements from both ends

**Key Characteristics:**
- Two pointers moving towards each other or same direction
- Often O(n) time complexity
- O(1) space complexity

**Common Problems:**
- Two Sum (sorted array)
- Remove duplicates
- Container with most water
- Valid palindrome

**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process current pair
        if condition:
            # Move pointers
            left += 1
            right -= 1
        elif another_condition:
            left += 1
        else:
            right -= 1
```

---

## 2. Sliding Window

**When to Use:**
- Contiguous subarray/substring problems
- Find maximum/minimum sum/length
- Problems with "window" constraints

**Key Characteristics:**
- Fixed or variable window size
- O(n) time complexity
- Track window state with variables

**Common Problems:**
- Maximum sum subarray of size k
- Longest substring with k distinct characters
- Minimum window substring
- Fruits into baskets

**Template:**
```python
def sliding_window(arr, k):
    window_start = 0
    window_sum = 0
    max_sum = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Expand window
        
        # Shrink window if needed
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return max_sum
```

---

## 3. Fast & Slow Pointers

**When to Use:**
- Cycle detection in linked lists
- Finding middle element
- Palindrome linked list

**Key Characteristics:**
- Two pointers moving at different speeds
- Fast pointer moves 2x speed of slow
- Often O(n) time, O(1) space

**Common Problems:**
- Linked list cycle detection
- Find cycle start
- Happy number
- Middle of linked list

**Template:**
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## 4. Merge Intervals

**When to Use:**
- Overlapping intervals
- Scheduling problems
- Range problems

**Key Characteristics:**
- Sort intervals first (usually by start time)
- Compare current with previous
- Merge or keep separate

**Common Problems:**
- Merge overlapping intervals
- Insert interval
- Meeting rooms
- Minimum meeting rooms

**Template:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlap
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return merged
```

---

## 5. Cyclic Sort

**When to Use:**
- Array with numbers in range 1 to n
- Find missing/duplicate numbers
- Problems where index = value - 1

**Key Characteristics:**
- Place each number at its correct index
- O(n) time, O(1) space
- Array modification required

**Common Problems:**
- Find missing number
- Find all duplicates
- Find corrupt pair
- First missing positive

**Template:**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
```

---

## 6. In-place Reversal of Linked List

**When to Use:**
- Reverse linked list or parts of it
- Modify list structure

**Key Characteristics:**
- Reverse pointers in-place
- O(n) time, O(1) space
- Track previous, current, next nodes

**Common Problems:**
- Reverse linked list
- Reverse sublist
- Reverse k-group
- Rotate list

**Template:**
```python
def reverse_list(head):
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

---

## 7. Tree BFS (Breadth-First Search)

**When to Use:**
- Level-order traversal
- Minimum depth problems
- Problems requiring level-by-level processing

**Key Characteristics:**
- Use queue for traversal
- Process nodes level by level
- O(n) time, O(w) space (w = max width)

**Common Problems:**
- Level order traversal
- Zigzag traversal
- Minimum depth
- Level averages

**Template:**
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

---

## 8. Tree DFS (Depth-First Search)

**When to Use:**
- Path problems
- Subtree problems
- Need to explore all branches

**Key Characteristics:**
- Use recursion or stack
- Pre-order, in-order, post-order
- O(n) time, O(h) space (h = height)

**Common Problems:**
- Path sum
- All paths
- Diameter of tree
- Maximum depth

**Template:**
```python
def dfs(root, target_sum):
    if not root:
        return False
    
    if not root.left and not root.right:  # Leaf
        return root.val == target_sum
    
    # Recursive DFS
    return (dfs(root.left, target_sum - root.val) or
            dfs(root.right, target_sum - root.val))
```

---

## 9. Two Heaps

**When to Use:**
- Find median
- Sliding window median
- Problems requiring min and max simultaneously

**Key Characteristics:**
- Max heap for smaller half
- Min heap for larger half
- Balance heaps to maintain median

**Common Problems:**
- Find median from data stream
- Sliding window median
- IPO problem
- Maximize capital

**Template:**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Smaller half (negated)
        self.min_heap = []  # Larger half
    
    def add_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
```

---

## 10. Subsets

**When to Use:**
- Find all combinations
- Find all permutations
- Generate all subsets

**Key Characteristics:**
- Backtracking approach
- Build solution incrementally
- O(2ⁿ) or O(n!) time complexity

**Common Problems:**
- All subsets
- All permutations
- Combinations
- Letter case permutation

**Template:**
```python
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

---

## 11. Modified Binary Search

**When to Use:**
- Sorted or rotated arrays
- Search in infinite array
- Find boundary conditions

**Key Characteristics:**
- O(log n) time complexity
- Modified conditions for mid comparison
- Handle edge cases carefully

**Common Problems:**
- Search in rotated array
- Find peak element
- Search in infinite array
- First bad version

**Template:**
```python
def binary_search_modified(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Modified condition
        if condition:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

---

## 12. Top K Elements

**When to Use:**
- Find K largest/smallest elements
- K most frequent elements
- Sorting related problems

**Key Characteristics:**
- Use heap (priority queue)
- Maintain heap of size K
- O(n log k) time complexity

**Common Problems:**
- Kth largest element
- K closest points
- Top K frequent elements
- Sort characters by frequency

**Template:**
```python
import heapq

def top_k_elements(arr, k):
    min_heap = []
    
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return list(min_heap)
```

---

## 13. K-way Merge

**When to Use:**
- Merge K sorted arrays/lists
- Find smallest range
- Problems with multiple sorted inputs

**Key Characteristics:**
- Use min heap
- Track which list each element came from
- O(n log k) time complexity

**Common Problems:**
- Merge K sorted lists
- Kth smallest in sorted matrix
- Smallest range covering K lists
- Find median in stream

**Template:**
```python
import heapq

def merge_k_sorted_lists(lists):
    min_heap = []
    
    # Initialize heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

---

## Pattern Selection Guide

| Input Type | Common Patterns |
|------------|----------------|
| Sorted Array | Two Pointers, Binary Search |
| Array with Range [1..n] | Cyclic Sort |
| Subarray/Substring | Sliding Window |
| Linked List | Fast & Slow Pointers, In-place Reversal |
| Tree | BFS, DFS |
| Find K Elements | Top K, Heap |
| Multiple Sorted Lists | K-way Merge |
| Overlapping Ranges | Merge Intervals |
| All Combinations | Subsets, Backtracking |
| Find Median | Two Heaps |

## Tips for Pattern Recognition

1. Read the problem carefully and identify keywords
2. Look at constraints (sorted? range? tree?)
3. Think about what data structure fits best
4. Consider time/space complexity requirements
5. Practice! Pattern recognition improves with experience

