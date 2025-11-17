"""
Test template using pytest framework.
"""

import pytest
from typing import List


class TestSolution:
    """Test class for organizing multiple test cases."""
    
    @pytest.fixture
    def solution(self):
        """Fixture to create solution instance or import solution function."""
        # from module import solution
        # return solution
        pass
    
    def test_basic_case(self, solution):
        """Test basic functionality."""
        pass
    
    def test_edge_case_empty(self, solution):
        """Test with empty input."""
        pass
    
    def test_edge_case_single(self, solution):
        """Test with single element."""
        pass
    
    def test_large_input(self, solution):
        """Test with large input."""
        pass
    
    @pytest.mark.parametrize("input_data,expected", [
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
    ])
    def test_parametrized(self, solution, input_data, expected):
        """Parametrized tests for multiple cases."""
        assert solution(input_data) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

