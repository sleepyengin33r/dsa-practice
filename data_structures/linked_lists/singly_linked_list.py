"""
Singly Linked List Implementation

A basic implementation of a singly linked list with common operations.
"""

from typing import Optional, List


class ListNode:
    """Node in a singly linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


class SinglyLinkedList:
    """Singly Linked List with common operations."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self) -> bool:
        """Check if list is empty."""
        return self.head is None
    
    def get_size(self) -> int:
        """Get the size of the list."""
        return self.size
    
    def insert_at_beginning(self, val: int) -> None:
        """
        Insert a node at the beginning.
        Time: O(1), Space: O(1)
        """
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, val: int) -> None:
        """
        Insert a node at the end.
        Time: O(n), Space: O(1)
        """
        new_node = ListNode(val)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert_at_position(self, val: int, position: int) -> bool:
        """
        Insert a node at specific position (0-indexed).
        Time: O(n), Space: O(1)
        """
        if position < 0 or position > self.size:
            return False
        
        if position == 0:
            self.insert_at_beginning(val)
            return True
        
        new_node = ListNode(val)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return True
    
    def delete_at_beginning(self) -> Optional[int]:
        """
        Delete node at beginning.
        Time: O(1), Space: O(1)
        """
        if not self.head:
            return None
        
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val
    
    def delete_at_end(self) -> Optional[int]:
        """
        Delete node at end.
        Time: O(n), Space: O(1)
        """
        if not self.head:
            return None
        
        if not self.head.next:
            val = self.head.val
            self.head = None
            self.size -= 1
            return val
        
        current = self.head
        while current.next.next:
            current = current.next
        
        val = current.next.val
        current.next = None
        self.size -= 1
        return val
    
    def delete_by_value(self, val: int) -> bool:
        """
        Delete first node with given value.
        Time: O(n), Space: O(1)
        """
        if not self.head:
            return False
        
        # If head needs to be deleted
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, val: int) -> bool:
        """
        Search for a value in the list.
        Time: O(n), Space: O(1)
        """
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        Time: O(n), Space: O(1)
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def to_list(self) -> List[int]:
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def from_list(self, values: List[int]) -> None:
        """Create linked list from Python list."""
        self.head = None
        self.size = 0
        for val in values:
            self.insert_at_end(val)
    
    def __str__(self) -> str:
        """String representation of the list."""
        if not self.head:
            return "Empty List"
        return " -> ".join(str(node.val) for node in self._iterate())
    
    def _iterate(self):
        """Generator to iterate through nodes."""
        current = self.head
        while current:
            yield current
            current = current.next


# ==================== Test Cases ====================

def test_basic_operations():
    """Test basic linked list operations."""
    ll = SinglyLinkedList()
    
    # Test empty list
    assert ll.is_empty() == True
    assert ll.get_size() == 0
    
    # Insert at beginning
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    assert ll.to_list() == [1, 2, 3]
    assert ll.get_size() == 3
    
    # Insert at end
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    assert ll.to_list() == [1, 2, 3, 4, 5]
    
    print("✅ Basic operations test passed")


def test_insertion():
    """Test insertion at various positions."""
    ll = SinglyLinkedList()
    
    ll.insert_at_position(1, 0)  # [1]
    ll.insert_at_position(3, 1)  # [1, 3]
    ll.insert_at_position(2, 1)  # [1, 2, 3]
    assert ll.to_list() == [1, 2, 3]
    
    print("✅ Insertion test passed")


def test_deletion():
    """Test deletion operations."""
    ll = SinglyLinkedList()
    ll.from_list([1, 2, 3, 4, 5])
    
    # Delete at beginning
    val = ll.delete_at_beginning()
    assert val == 1
    assert ll.to_list() == [2, 3, 4, 5]
    
    # Delete at end
    val = ll.delete_at_end()
    assert val == 5
    assert ll.to_list() == [2, 3, 4]
    
    # Delete by value
    ll.delete_by_value(3)
    assert ll.to_list() == [2, 4]
    
    print("✅ Deletion test passed")


def test_search():
    """Test search operation."""
    ll = SinglyLinkedList()
    ll.from_list([10, 20, 30, 40])
    
    assert ll.search(20) == True
    assert ll.search(25) == False
    
    print("✅ Search test passed")


def test_reverse():
    """Test reverse operation."""
    ll = SinglyLinkedList()
    ll.from_list([1, 2, 3, 4, 5])
    
    ll.reverse()
    assert ll.to_list() == [5, 4, 3, 2, 1]
    
    print("✅ Reverse test passed")


if __name__ == "__main__":
    test_basic_operations()
    test_insertion()
    test_deletion()
    test_search()
    test_reverse()
    print("\n✨ All tests passed!")
    
    # Demo
    print("\n--- Demo ---")
    ll = SinglyLinkedList()
    ll.from_list([1, 2, 3, 4, 5])
    print(f"Original list: {ll}")
    
    ll.reverse()
    print(f"Reversed list: {ll}")
    
    ll.insert_at_position(99, 2)
    print(f"After inserting 99 at position 2: {ll}")

