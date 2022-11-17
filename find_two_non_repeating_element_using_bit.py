def find_two_non_repeating_element_using_bit():
    ar = [3,4,5,3,2,2,4,1]
    res = 0
    for i in range(len(ar)):
        res = res ^ ar[i]
    print(res)

    # by this we get right most set bit
    res = res & -res
    a = 0
    b= 0
    for i in range(len(ar)):
        if ar[i] & res >0:
            a = a ^ ar[i]
        else:
            b = b ^ ar[i]
    print(a,b)


find_two_non_repeating_element_using_bit()