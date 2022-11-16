def find_bit():
    n = 17
    # 10001
    i = 5
    mask = 1 << i-1
    print(mask)
    if n & mask == 0:
        print("find 0")
    else:
        print("1")

find_bit()
