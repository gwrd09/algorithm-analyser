from typing import TypeVar

T = TypeVar('T')

def bubble_sort(lst: list[T]) -> None:
    """Sorts a list in-place by comparing elements 
    and swapping them if the elements are in the wrong order.

    Time complexity is O(n^2).
    """
    for i in range(len(lst)-1):
        for j in range(len(lst)-(1+i)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def insertion_sort(lst: list[T]) -> None:
    """Sorts a list in-place by building a sorted section
    on the left. Starting from the second element it swaps
    backwards until the element is correctly placed, repeating
    this until elements are correctly sorted.

    Time complexity is O(n^2).
    """
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
        i += 1

def merge_sort(lst: list[T]) -> list[T]:
    """Sorts a list by recursively splitting the input 
    list down into single elements, merging two
    sorted sublists until a fully sorted list is produced.

    Time complexity is O(n logn).
    """
    if len(lst) <= 1:
        return lst.copy()
    left_lst = merge_sort(lst[:len(lst)//2])  
    right_lst = merge_sort(lst[len(lst)//2:])  
    return merge(left_lst, right_lst)

def merge(left: list[T], right: list[T]) -> list[T]:
    """Merges two sorted lists into a single sorted list.
    Compares the smallest elements and appends the smaller one 
    to a new list. Continues until all elements are ordered. 
    Assumes both lists are already ordered.
    """
    result=[]
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    result.extend(left[l_index:])
    result.extend(right[r_index:])
    return result

def quick_sort(lst: list[T], lo, hi) -> None:
    """Sorts a list by recursively partioning the input and sorting the elements
    around a pivot, until a fully sorted list is produced.

    Time complexity is O(n logn).
    """
    if (lo >= hi) or (lo < 0):
        return
    p = partition(lst, lo, hi)
    quick_sort(lst, lo, (p - 1))
    quick_sort(lst, p + 1, hi)

def partition(lst: list[T], lo, hi) -> int:
    """Takes a sublist and swaps digits around a pivot, to the left if its lower than the
    value of the pivot, and to the right if its higher than the value of the pivot.
    """
    pivot = lst[hi]
    
    i = lo
    for j in range(lo, hi):
        if lst[j] <= pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i