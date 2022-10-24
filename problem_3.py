def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = binary_insert_sort(input_list)
    n = len(input_list)
    n_one = n // 2
    n_two = n - n_one
    array_one = 0
    array_two = 0
    for i in range(len(input_list) - 1, -1, -2):
        n_two -= 1
        array_two += input_list[i]*pow(10,n_two)
    for i in range(len(input_list) - 2, -1, -2):
        n_one -= 1
        array_one += input_list[i]*pow(10,n_one)
    return [array_two, array_one]
    
    
def binary_search(input_list, low_index, high_index, number):
    if low_index > high_index:
        return low_index
    if low_index == high_index:
        if number < input_list[low_index]:
            return low_index
        else:
            return low_index+1
    
    mid = int((low_index + high_index) / 2)
    
    if input_list[mid] > number:
        return binary_search(input_list, low_index, mid - 1, number)
    elif input_list[mid] < number:
        return binary_search(input_list, mid + 1, high_index, number)
    return mid

def binary_insert_sort(input_list):
    for i in range(1, len(input_list)):
        number = input_list[i]
        j = binary_search(input_list, 0, i-1, number)
        input_list = input_list[:j] + [number] + input_list[j:i] + input_list[i+1:]
    return input_list
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0,1], [1, 0]])
test_function([[0,0], [0, 0]])