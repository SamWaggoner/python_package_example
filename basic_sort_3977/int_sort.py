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

"""This module sorts lists of integers in ascending order.

Three algorithms are available, including bubble sort, quick sort and insertion
sort. There are no exported classes or libraries that are used. Sorting
algorithms were created following the methods of the following sources:
Bubble sort: https://www.geeksforgeeks.org/bubble-sort/
Quick sort: https://www.youtube.com/watch?v=Hoixgm4-P4M
Insertion sort: https://www.geeksforgeeks.org/insertion-sort/
Note that bubble sort uses a flag that causes it to stop iterating through the
list early if it is already sorted. This is a slight improvement on the basic
algorithm.

Typical usage example (for any of the three implementations):

    sorted_list = bubble(unsorted_list)
"""


def bubble(int_list):
    """
    Sorts a list of integers in ascending order using the bubblesort algorithm.

    Args:
        int_list (list): The list of integers to be sorted.

    Returns:
        The sorted list of the same integers in ascending order.

    Raises:
        TypeError: The supplied list contains non-integer values.
    """

    if any(not isinstance(ele, int) for ele in int_list):
        raise TypeError("Input contains non-integer values.")

    # We make a maximum of n-1 passes, where each pass goes through the entire
    # list. At each index, we swap the element and the next if they are out of
    # order. If no swaps were made after a pass, we return immediately.

    for pass_num in range(len(int_list) - 1):
        swap_was_made = False
        for idx in range(len(int_list) - 1):
            if int_list[idx + 1] < int_list[idx]:
                temp = int_list[idx]
                int_list[idx] = int_list[idx + 1]
                int_list[idx + 1] = temp
                swap_was_made = True
        if not swap_was_made:
            return int_list
    return int_list


def quick(int_list):
    """
    Sorts a list of integers in ascending order using the quicksort algorithm.

    Args:
        int_list (list): The list of integers to be sorted.

    Returns:
        The sorted list of the same integers in ascending order.

    Raises:
        TypeError: The supplied list contains non-integer values.
    """

    if any(not isinstance(ele, int) for ele in int_list):
        raise TypeError("Input contains non-integer values.")

    if len(int_list) == 1 or len(int_list) == 0:  # This is the base case.
        return int_list

    # During each call of this recursive function, we choose a pivot and swap
    # that element with the last element. We then repeatedly find the leftmost
    # element that is larger than the pivot and the rightmost element that is
    # smaller than the pivot, and swap them until the index of the leftmost
    # element is greater than the index of the rightmost element.

    pivot_idx = -1
    pivot = int_list[pivot_idx]

    temp = int_list[-1]
    int_list[-1] = pivot
    int_list[pivot_idx] = temp

    while True:
        left_idx = "pivot is largest"
        for left in range(len(int_list) - 1):  # Find the leftmost element that
            # is larger than pivot.
            if int_list[left] > pivot:
                left_idx = left
                break

        right_idx = "pivot is smallest"
        for r in range(len(int_list) - 2, -1, -1):  # Find the rightmost element
            # that is smaller than pivot.
            if int_list[r] < pivot:
                right_idx = r
                break

        if left_idx == "pivot is largest":
            return quick(int_list[:-1]) + [pivot]
        elif right_idx == "pivot is smallest":
            return [pivot] + quick(int_list[:-1])

        if right_idx < left_idx:  # We know the pivot's location in the final array.
            return quick(int_list[: right_idx + 1]) + [pivot] + quick(int_list[left_idx:-1])

        temp = int_list[right_idx]
        int_list[right_idx] = int_list[left_idx]
        int_list[left_idx] = temp


def insertion(int_list):
    """
    Sorts a list of integers in ascending order using the insertion sort
    algorithm.

    Args:
        int_list (list): The list of integers to be sorted.

    Returns:
        The sorted list of the same integers in ascending order.

    Raises:
        TypeError: The supplied list contains non-integer values.
    """

    if any(not isinstance(ele, int) for ele in int_list):
        raise TypeError("Input contains non-integer values.")

    # Shuffle each element in the list backward as far as possible without
    # making it out of order.

    for pos in range(1, len(int_list)):
        idx = pos
        while idx - 1 > -1 and int_list[idx] < int_list[idx - 1]:
            temp = int_list[idx - 1]
            int_list[idx - 1] = int_list[idx]
            int_list[idx] = temp
            idx -= 1
    return int_list
