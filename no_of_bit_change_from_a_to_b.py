def no_of_bit_change_from_a_to_b():
    a = 22
    b = 27
    #  we xor property - it return 1 where we have opposite bit ex (10 ,01) = 1 and (11 or 00) = 0
    # let do xor first

    c = a^b
    # now we need to number of set bit in c then we will get final result
    # for this I am using two approach

    # 1st ----**********-----------
    # print(c)
    # count = 0
    # while c:
    #     if c & 1 == 1:
    #         count =count + 1
    #     c = c >>1
    #
    # print(count)
    #     ------------------------**********______

    #     second way
    count = 0
    while c:
        #  n & (n-1) this method always do zero last significant digit
        c &= (c-1)
        count += 1
    print(count)






no_of_bit_change_from_a_to_b()