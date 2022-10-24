def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = pivot_index(input_list, 0, len(input_list) -1)
    
    if pivot == -1:
        return binary_search(input_list, 0, len(input_list) - 1, number)
    if input_list[pivot] == number:
        return pivot
    if number < input_list[0]:
        return binary_search(input_list, pivot + 1, len(input_list) - 1, number)
    return binary_search(input_list, 0, pivot - 1, number)

def binary_search(input_list, low_index, high_index, number):
    if low_index > high_index:
        return -1
    mid = int((low_index + high_index) / 2)
    
    if input_list[mid] == number:
        return mid
    if input_list[mid] > number:
        return binary_search(input_list, low_index, mid - 1, number)
    return binary_search(input_list, mid + 1, high_index, number)
    
def pivot_index(input_list, low_index, high_index):
    if low_index == high_index:
        low
    if low_index > high_index:
        return -1
    mid = int((low_index + high_index) / 2)
    if mid > low_index and input_list[mid] < input_list[mid - 1]:
        return mid - 1
    if mid < high_index and input_list[mid] > input_list[mid + 1]:
        return mid
    if input_list[mid] < input_list[low_index]:
        return pivot_index(input_list, low_index, mid -1)
    return pivot_index(input_list, mid + 1, high_index)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])