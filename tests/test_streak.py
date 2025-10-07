import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Test a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4]) == 4

def test_multiple_streaks_longest_first():
    """Test with multiple streaks, where the longest is first."""
    assert longest_positive_streak([5, 6, 7, 0, 1, 2]) == 3

def test_multiple_streaks_longest_in_middle():
    """Test with multiple streaks, with the longest in the middle."""
    assert longest_positive_streak([1, 0, 5, 6, 7, 8, -1, 2, 3]) == 4

def test_multiple_streaks_longest_last():
    """Test the case where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 7]) == 4

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([3, 4, -1, 2]) == 2

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([3, 4, 0, 2, 5]) == 2

def test_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -10]) == 0

def test_all_ones():
    """Test a simple streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_example_from_prompt():
    """Test the specific example given in the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3