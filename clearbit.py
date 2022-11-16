def clear_bit():
    n= 309
    #  100110101
    # let suppose you wanna clear 5th bit "100100101" - final out put
    i = 5
    mask = ~(i << i-1)
    n = n & mask
    print(n)
clear_bit()

