import random

import pytest


def bubble_sort(data: list, asc: bool = True):
    """
    bubble sort, time complexity O(n^2)
    Args:
        data: input data, the order of number are messy
        asc: ascending order or not

    Returns:
        sorted list
    """
    for i in range(len(data)):
        for j in range(len(data) - 1, i, -1):
            if asc:
                if data[j] < data[i]:
                    data[i], data[j] = data[j], data[i]
            else:
                if data[j] > data[i]:
                    data[i], data[j] = data[j], data[i]
    return data


def selection_sort(data: list, asc: bool = True):
    """
    selection sort: iterate over all index and select the max/min of remaining list to replace current value
    time complexity O(n^2)
    Args:
        data: input data, the order of number are messy
        asc: ascending order or not
    """

    def _find_target_index(current_idx: int) -> None | int:
        _target_idx = current_idx
        for i in range(current_idx + 1, len(data)):
            if asc:
                if data[i] <= data[_target_idx]:
                    _target_idx = i
            else:
                if data[i] >= data[_target_idx]:
                    _target_idx = i
        return _target_idx

    for idx in range(len(data)):
        target_idx = _find_target_index(idx)
        if target_idx:
            data[idx], data[target_idx] = data[target_idx], data[idx]
    return data


def insertion_sort(data: list, asc: bool = True):
    """
    insertion sort, just like our sort card process: suppose first n items are sorted, proceed to n + 1 and see which place
    should insert backwardly. time complexity: O(n^2)
    Args:
        data: input data, the order of number are messy
        asc: ascending order or not
    """
    for idx1 in range(0, len(data) - 1):
        for idx2 in range(idx1 + 1, 0, -1):
            if asc:
                if data[idx2] <= data[idx2 - 1]:
                    data[idx2], data[idx2 - 1] = data[idx2 - 1], data[idx2]
            else:
                if data[idx2] >= data[idx2 - 1]:
                    data[idx2], data[idx2 - 1] = data[idx2 - 1], data[idx2]
    return data


def _get_partition_idx(data: list, left_idx: int, right_idx: int) -> int:
    pivot_value = data[left_idx]
    j = left_idx
    for i in range(left_idx + 1, right_idx + 1):
        if data[i] < pivot_value:
            j += 1
            data[i], data[j] = data[j], data[i]
    data[left_idx], data[j] = data[j], data[left_idx]
    return j


def _left_pivot_quick_sort(data: list, left_idx: int, right_idx: int):
    if left_idx >= right_idx:
        return
    partition_idx = _get_partition_idx(data, left_idx, right_idx)
    _left_pivot_quick_sort(data, left_idx, partition_idx - 1)
    _left_pivot_quick_sort(data, partition_idx + 1, right_idx)


def quick_sort(data: list, asc: bool = True):
    _left_pivot_quick_sort(data, 0, len(data) - 1)
    return data


def merge_sort(data: list, asc: bool = True):
    if len(data) == 1:
        return data
    data1 = merge_sort(data[: int(len(data) / 2)])
    data2 = merge_sort(data[int(len(data) / 2) :])
    return _merge(data1, data2)


def _merge(data1: list, data2: list):
    _res = []
    while len(data1) and len(data2):
        if data1[0] > data2[0]:
            _res.append(data2[0])
            data2.pop(0)
        else:
            _res.append(data1[0])
            data1.pop(0)
    if data1:
        _res = _res + data1
    if data2:
        _res = _res + data2
    return _res


def test_sort():
    _data = [3, 2, 2, 1]
    res = bubble_sort(_data)
    print(res)

    _data = [3, 2, 2, 1]
    res = selection_sort(_data)
    print(res)

    _data = [3, 2, 2, 1]
    res = insertion_sort(_data)
    print(res)

    _data = [3, 2, 2, 1]
    res = quick_sort(_data)
    print(res)

    _data = [3, 2, 2, 1]
    res = merge_sort(_data)
    print(res)


if __name__ == "__main__":
    test_sort()
