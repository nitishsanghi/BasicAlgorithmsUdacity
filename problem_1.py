def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    else:
        lower = 2
        upper = int(number/2)
        while(lower <= upper):
            mid = int((upper + lower)/2)
            square = mid*mid
            if(square == number):
                return mid
            elif (square < number):
                lower = mid + 1
                root = mid
            else:
                upper = mid - 1
    return root

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
