# Repository Structure

This document provides a complete overview of your DSA practice repository structure.

## 📁 Complete Directory Tree

```
dsa-practice/
│
├── README.md                          # Main repository overview and progress tracking
├── GETTING_STARTED.md                 # Detailed guide to get started
├── STRUCTURE.md                       # This file - repository structure overview
├── .gitignore                        # Python gitignore configuration
├── requirements.txt                  # Python dependencies
│
├── 📚 data_structures/               # Data structure implementations
│   ├── __init__.py
│   ├── arrays/
│   │   └── __init__.py
│   ├── linked_lists/
│   │   ├── __init__.py
│   │   └── singly_linked_list.py    # ✅ Example implementation
│   ├── stacks/
│   │   └── __init__.py
│   ├── queues/
│   │   └── __init__.py
│   ├── trees/
│   │   └── __init__.py
│   ├── graphs/
│   │   └── __init__.py
│   ├── heaps/
│   │   └── __init__.py
│   ├── hash_tables/
│   │   └── __init__.py
│   └── tries/
│       └── __init__.py
│
├── 🔧 algorithms/                    # Algorithm implementations
│   ├── __init__.py
│   ├── sorting/
│   │   └── __init__.py
│   ├── searching/
│   │   └── __init__.py
│   ├── recursion/
│   │   └── __init__.py
│   ├── dynamic_programming/
│   │   └── __init__.py
│   ├── greedy/
│   │   └── __init__.py
│   ├── divide_and_conquer/
│   │   └── __init__.py
│   └── backtracking/
│       └── __init__.py
│
├── 🎯 patterns/                      # Problems organized by patterns (RECOMMENDED)
│   ├── __init__.py
│   │
│   ├── two_pointers/                # Start here! 👈
│   │   ├── __init__.py              # Pattern description
│   │   ├── README.md                # Detailed pattern guide
│   │   └── two_sum_sorted.py       # ✅ Example problem
│   │
│   ├── sliding_window/              # Great for subarray problems
│   │   ├── __init__.py
│   │   └── max_sum_subarray.py     # ✅ Example problem
│   │
│   ├── fast_slow_pointers/          # Linked list problems
│   │   └── __init__.py
│   │
│   ├── merge_intervals/             # Scheduling problems
│   │   └── __init__.py
│   │
│   ├── cyclic_sort/                 # Array problems with [1..n] range
│   │   └── __init__.py
│   │
│   ├── in_place_reversal/           # Linked list reversal
│   │   └── __init__.py
│   │
│   ├── tree_bfs/                    # Level-order traversal
│   │   └── __init__.py
│   │
│   ├── tree_dfs/                    # Depth-first search
│   │   └── __init__.py
│   │
│   ├── two_heaps/                   # Median problems
│   │   └── __init__.py
│   │
│   ├── subsets/                     # Combinations & permutations
│   │   └── __init__.py
│   │
│   ├── modified_binary_search/      # Advanced search
│   │   └── __init__.py
│   │
│   ├── top_k_elements/              # Heap problems
│   │   └── __init__.py
│   │
│   └── k_way_merge/                 # Merge multiple sorted lists
│       └── __init__.py
│
├── 📊 problems/                      # Problems organized by difficulty
│   ├── __init__.py
│   ├── easy/
│   │   └── __init__.py
│   ├── medium/
│   │   └── __init__.py
│   ├── hard/
│   │   └── __init__.py
│   └── by_company/                  # Optional: company-specific
│       └── __init__.py
│
├── 📋 templates/                     # Code templates
│   ├── problem_template.py          # Standard problem template
│   └── test_template.py             # Pytest template
│
├── 🛠️ utils/                         # Helper utilities
│   ├── __init__.py
│   ├── common.py                    # Common utility functions
│   └── test_helpers.py              # Testing helpers (ListNode, TreeNode, etc.)
│
└── 📝 notes/                         # Study notes and references
    ├── time_complexity.md           # Big O notation guide
    ├── space_complexity.md          # Space complexity guide
    └── pattern_notes.md             # Complete patterns reference
```

## 🎯 Key Directories Explained

### 1. **patterns/** - Pattern-Based Organization (⭐ RECOMMENDED)

This is your primary workspace! Each pattern directory contains:
- Pattern description in `__init__.py`
- Optional `README.md` with detailed guides
- Multiple problems demonstrating the pattern

**Why use patterns?**
- Helps recognize similar problems quickly
- Builds pattern recognition skills
- Makes interview prep more efficient

**Example workflow:**
```bash
# Learn the Two Pointers pattern
1. Read: patterns/two_pointers/__init__.py
2. Study: patterns/two_pointers/README.md
3. Practice: patterns/two_pointers/two_sum_sorted.py
4. Add more problems as you solve them
```

### 2. **data_structures/** - Core Implementations

Implement and understand fundamental data structures:
- Build them from scratch to understand internals
- Reference implementations for problem solving
- Practice common operations

**Example**: `singly_linked_list.py` includes:
- Complete LinkedList class
- Common operations (insert, delete, reverse)
- Comprehensive test cases

### 3. **algorithms/** - Algorithm Categories

Classic algorithm implementations:
- Sorting algorithms (bubble, merge, quick, etc.)
- Searching algorithms (binary search, DFS, BFS)
- Dynamic programming solutions
- Greedy algorithms

### 4. **problems/** - Difficulty-Based Organization

Alternative organization by difficulty level:
- Quick access to problems at your skill level
- Track progression from easy → hard
- Useful for systematic practice

### 5. **templates/** - Starter Code

Ready-to-use templates:
- **problem_template.py**: Complete problem structure
- **test_template.py**: Pytest-based testing

Copy and modify for new problems!

### 6. **utils/** - Helper Functions

Reusable utilities:
- **common.py**: Timing decorator, array helpers
- **test_helpers.py**: `ListNode`, `TreeNode`, conversion functions

**Example usage:**
```python
from utils.test_helpers import create_linked_list, print_tree
from utils.common import timing_decorator
```

### 7. **notes/** - Learning Resources

Reference documents:
- Time & space complexity guides
- Pattern recognition guide
- Algorithm explanations

## 🚀 Quick Start Commands

```bash
# View the structure
ls -R

# Run example problems
python3 patterns/two_pointers/two_sum_sorted.py
python3 patterns/sliding_window/max_sum_subarray.py
python3 data_structures/linked_lists/singly_linked_list.py

# Copy template for new problem
cp templates/problem_template.py patterns/two_pointers/my_problem.py

# Run all tests in a directory
pytest patterns/two_pointers/ -v
pytest patterns/ -v  # All patterns

# Install dependencies
pip install -r requirements.txt
```

## 📝 File Naming Conventions

Follow these conventions for consistency:

### Problem Files
- Use snake_case: `two_sum_sorted.py`
- Be descriptive: `longest_substring_no_repeat.py`
- Avoid numbers: `problem_167.py` ❌ → `two_sum_sorted.py` ✅

### Implementation Files
- Descriptive names: `singly_linked_list.py`
- Algorithm names: `merge_sort.py`, `binary_search.py`

### Test Files
- Prefix with `test_`: `test_linked_list.py`
- Or include tests in same file (see examples)

## 🎓 Recommended Organization Strategy

### Strategy 1: Pattern-First (Recommended for Interview Prep)
```
patterns/
  two_pointers/
    - two_sum_sorted.py
    - remove_duplicates.py
    - container_with_water.py
  sliding_window/
    - max_sum_subarray.py
    - longest_substring_k.py
```

### Strategy 2: Platform-Based
```
problems/
  easy/
    - leetcode_1_two_sum.py
    - leetcode_21_merge_lists.py
  medium/
    - leetcode_15_three_sum.py
```

### Strategy 3: Hybrid (Best of Both)
Use patterns as primary, symlink to difficulty:
```bash
# Create problem in pattern directory
vim patterns/two_pointers/two_sum.py

# Symlink to difficulty directory
ln -s ../../patterns/two_pointers/two_sum.py problems/easy/two_sum.py
```

## 📊 Tracking Progress

Update `README.md` as you complete problems:

```markdown
### Patterns Mastery
- [x] Two Pointers (5/10)
  - [x] Two Sum II
  - [x] Remove Duplicates
  - [x] Valid Palindrome
  - [x] Container With Most Water
  - [x] 3Sum
- [ ] Sliding Window (3/10)
  - [x] Max Sum Subarray
  - [x] Longest Substring K
  - [x] Min Window Substring
```

## 🔗 Next Steps

1. ✅ **You are here** - Repository is set up!
2. 📖 Read `GETTING_STARTED.md` for detailed workflow
3. 🎯 Start with `patterns/two_pointers/` (beginner-friendly)
4. 📝 Review `notes/pattern_notes.md` for pattern overview
5. 💪 Solve your first problem using the template!

## 💡 Tips

- **One pattern at a time**: Master a pattern before moving to the next
- **Multiple attempts**: Solve the same problem multiple times over weeks
- **Document learnings**: Add comments explaining your approach
- **Test thoroughly**: Edge cases matter in interviews
- **Time yourself**: Practice under time constraints

---

**Happy coding! 🚀 You're all set to become a DSA master!**

