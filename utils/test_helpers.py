"""
Helper functions for testing data structures and algorithms.
"""

from typing import List, Optional


class ListNode:
    """Definition for singly-linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


class TreeNode:
    """Definition for a binary tree node."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Create a linked list from a list of values.
    
    Args:
        values: List of values
    
    Returns:
        Head of the linked list
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert a linked list to a Python list.
    
    Args:
        head: Head of the linked list
    
    Returns:
        List of values
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def print_linked_list(head: Optional[ListNode]) -> None:
    """
    Print a linked list in readable format.
    
    Args:
        head: Head of the linked list
    """
    values = linked_list_to_list(head)
    print(" -> ".join(map(str, values)) if values else "Empty List")


def create_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Create a binary tree from level-order traversal list.
    None represents a null node.
    
    Args:
        values: Level-order traversal with None for null nodes
    
    Returns:
        Root of the binary tree
    """
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert binary tree to level-order list representation.
    
    Args:
        root: Root of the binary tree
    
    Returns:
        Level-order traversal with None for null nodes
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def print_tree(root: Optional[TreeNode], level: int = 0, prefix: str = "Root: ") -> None:
    """
    Print binary tree in a tree-like structure.
    
    Args:
        root: Root of the binary tree
        level: Current level (for recursion)
        prefix: Prefix for the current node
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

