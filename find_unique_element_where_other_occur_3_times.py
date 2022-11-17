import sys


def find_unique_element_where_other_occur_3_times():
    ar = [43,32,69,32,43,32,43]
    tn =  sys.maxsize
    tnp1 =0
    tnp2 =0
    for i in range(len(ar)):
        ctn = ar[i] & tn
        ctn1 = ar[i] & tnp1
        ctn2 = ar[i] & tnp2

        tn = tn & (~ctn)
        tnp1 = tnp1 | ctn

        tnp1 = tnp1 & (~ctn1)
        tnp2 = tnp2 | ctn1

        tnp2 = tnp2 & (~ctn2)
        tn = tn | ctn2
    print(tnp1)

find_unique_element_where_other_occur_3_times()