# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================
import pytest
import numpy as np
from basic_sort_UNIQUE_SUFFIX import bubble, quick, insertion


def is_sorted(int_list):
    """
    Testing oracle.
    """
    return int_list == sorted(int_list)


@pytest.fixture
def int_lists():
    # Fixture that creates testing data for all tests
    return [
        # Sorted list
        [1, 2, 3],
        # Reversed list
        [3, 2, 1],
        # List with duplicate elements
        [1, 1, 1, 1, 1],
        # Random list generated using NumPy
        list(np.random.randint(low=-10, high=200, size=5)),
        # Large list for scalability testing
        list(range(1000, 0, -1)),
        # List with a mix of positive and negative numbers
        [-5, 2, -8, 9, 0],
        # List with only one element
        [42],
        # Empty list
        [],
    ]


@pytest.mark.parametrize("int_list", int_lists)
# Test the bubble sort algorithm
def test_bubble(int_list):
    sorted_list = bubble(int_list.copy())
    assert is_sorted(sorted_list)


@pytest.mark.parametrize("int_list", int_lists)
# Test the quick sort algorithm
def test_quick(int_list):
    sorted_list = quick(int_list.copy())
    assert is_sorted(sorted_list)


@pytest.mark.parametrize("int_list", int_lists)
# Test the insertion sort algorithm
def test_insertion(int_list):
    sorted_list = insertion(int_list.copy())
    assert is_sorted(sorted_list)
