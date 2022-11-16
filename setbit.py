def set_bit():
    n = 13
    # 13 = 1101
    # i represent which bit you wanna set
    i = 2
    mask = 1 << i-1

    n = n | mask
    print(n)
    # after set 1111 = 15

set_bit()