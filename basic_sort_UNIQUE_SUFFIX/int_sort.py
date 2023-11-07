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

"""
int_sort.py: This module sorts lists of integers in ascending order. Three 
algorithms are available, including bubble sort, quick sort and insertion sort.

Author:         SEWDO
Date created:   11/07/23
For:            COS 397, Homework 6
"""

def bubble(int_list):
    """
    Sorts a list of integers in ascending order using the bubblesort algorithm.

    Args:
        int_list (list): The list of integers to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Raises:
        ValueError: Raised if int_list contains non-integer values.
    """

    # sanitize input
    if any(not isinstance(ele, int) for ele in int_list):
        raise ValueError("ERROR: Input contains non-integer values.")
    
    # make a maximum of n-1 passes
    for pass_num in range(len(int_list)-1):
        swap_was_made = False
        # iterate through the entire list
        for idx in range(len(int_list)-1):
            # swap the current and next elements if they are out of order
            if int_list[idx+1] < int_list[idx]:
                temp = int_list[idx]
                int_list[idx] = int_list[idx+1]
                int_list[idx+1] = temp
                swap_was_made = True
        # if no swaps were made, then the list is completely sorted
        if not swap_was_made:
            return int_list
    return int_list


def quick(int_list):
    """
    Sorts a list of integers in ascending order using the quicksort algorithm.

    Args:
        int_list (list): The list of integers to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Raises:
        ValueError: Raised if int_list contains non-integer values.
    """

    # sanitize input
    if any(not isinstance(ele, int) for ele in int_list):
        raise ValueError("ERROR: Input contains non-integer values.")
    
    # base case
    if len(int_list) == 1:
        return int_list

    # choose a pivot index
    pivot_idx = -1
    pivot = int_list[pivot_idx]

    # swap the pivot with the element at the end of the list
    temp = int_list[-1]
    int_list[-1] = pivot
    int_list[pivot_idx] = temp

    while True:
        # find leftmost element that is larger than pivot
        left_idx = "pivot is largest"
        for l in range(len(int_list)-1):
            if int_list[l] > pivot:
                left_idx = l
                break
        # find rightmost element that is smaller than pivot
        right_idx = "pivot is smallest"
        for r in range(len(int_list)-2, -1, -1):
            if int_list[r] < pivot:
                right_idx = r
                break

        # if pivot is the largest or smallest, then we already know its
        #   location in the final array. Call quick() on the rest of the list.
        if left_idx == "pivot is largest":
            return quick(int_list[:-1]) + [pivot]
        elif right_idx == "pivot is smallest":
            return [pivot] + quick(int_list[:-1])
        
        # if all swappings have occurred, then we know the pivot's location in
        #   the final array. 
        if right_idx < left_idx:
            return quick(int_list[:right_idx + 1]) + [pivot] + quick(int_list[left_idx:-1])
        
        # else swap the left and right indexes and continue the while loop, 
        #   since there could be more swaps possible
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
        list: The sorted list in ascending order.

    Raises:
        ValueError: Raised if int_list contains non-integer values.
    """

    # sanitize input
    if any(not isinstance(ele, int) for ele in int_list):
        raise ValueError("ERROR: Input contains non-integer values.")
    
    # for each element in the list
    for pos in range(1, len(int_list)):
        idx = pos
        # shuffle it backward as far as possible without making it out of order
        while idx - 1 > -1 and int_list[idx] < int_list[idx-1]:
            # swap the element with the previous element
            temp = int_list[idx-1]
            int_list[idx-1] = int_list[idx]
            int_list[idx] = temp
            idx -= 1
    return int_list