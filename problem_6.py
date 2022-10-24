def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None:
        return None
    if not len(ints):
        return "Empty list input"
    max_val = ints[0]
    min_val = ints[0]
    for i in range(1, len(ints)):
        if max_val < ints[i]:
            max_val = ints[i]
        if min_val > ints[i]:
            min_val = ints[i]
    return (min_val, max_val)
   

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
m = [i for i in range(0, 10000)]  # a list containing 0 - 9999
random.shuffle(m)
n = [i for i in range(0, 1)]  # a list containing 0 - 0
random.shuffle(n)
o = [i for i in range(0, 0)]  # a list containing nothing
random.shuffle(o)
p = None  # a None type


print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 9999) == get_min_max(m)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max(n)) else "Fail")
print ("Pass" if ("Empty list input" == get_min_max(o)) else "Fail")
print ("Pass" if (None == get_min_max(p)) else "Fail")