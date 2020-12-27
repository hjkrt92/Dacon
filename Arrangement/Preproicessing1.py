def align(string_keys, string_values):
    x1, x2, x3, x4, x5 = [], [], [], [], []
    l1, l2, l3, l4, l5 = [], [], [], [], []
    for _keys, _values in zip(string_keys, string_values):
        if _keys == "영세":
            x1.append(_keys)
            l1.append(_values)
        elif _keys == "중소":
            x2.append(_keys)
            l2.append(_values)
        elif _keys == "중소1":
            x3.append(_keys)
            l3.append(_values)
        elif _keys == "중소2":
            x4.append(_keys)
            l4.append(_values)
        else:
            x5.append(_keys)
            l5.append(_values)
    x = x1 + x2 + x3 + x4 + x5
    l = l1 + l2 + l3 + l4 + l5
    return x, l
from collections import deque

def get_five(arr,arr2):
    m = max(arr)
    m_1 = arr.index(m)
    k_1 = arr2[m_1]
    del arr[m_1]
    del arr2[m_1]
    m2 = max(arr)
    m_2 = arr.index(m2)
    k_2 = arr2[m_2]
    del arr[m_2]
    del arr2[m_2]
    m3 = max(arr)
    m_3 = arr.index(m3)
    k_3 = arr2[m_3]
    del arr[m_3]
    del arr2[m_3]
    m4 = max(arr)
    m_4 = arr.index(m4)
    k_4 = arr2[m_4]
    del arr[m_4]
    del arr2[m_4]
    m5 = max(arr)
    m_5 = arr.index(m5)
    k_5 = arr2[m_5]
    del arr[m_5]
    del arr2[m_5]
    x = "{}".format(k_1),"{}".format(k_2),"{}".format(k_3),"{}".format(k_4),"{}".format(k_5)
    y = [m,m2,m3,m4,m5]
    return x,y


def get_twenty(arr,arr2):
    m = max(arr)
    m_1 = arr.index(m)
    k_1 = arr2[m_1]
    del arr[m_1]
    del arr2[m_1]
    m2 = max(arr)
    m_2 = arr.index(m2)
    k_2 = arr2[m_2]
    del arr[m_2]
    del arr2[m_2]
    m3 = max(arr)
    m_3 = arr.index(m3)
    k_3 = arr2[m_3]
    del arr[m_3]
    del arr2[m_3]
    m4 = max(arr)
    m_4 = arr.index(m4)
    k_4 = arr2[m_4]
    del arr[m_4]
    del arr2[m_4]
    m5 = max(arr)
    m_5 = arr.index(m5)
    k_5 = arr2[m_5]
    del arr[m_5]
    del arr2[m_5]
    m6 = max(arr)
    m_6 = arr.index(m6)
    k_6 = arr2[m_6]
    del arr[m_6]
    del arr2[m_6]
    m7 = max(arr)
    m_7 = arr.index(m7)
    k_7 = arr2[m_7]
    del arr[m_7]
    del arr2[m_7]
    m8 = max(arr)
    m_8 = arr.index(m8)
    k_8 = arr2[m_8]
    del arr[m_8]
    del arr2[m_8]
    m9 = max(arr)
    m_9 = arr.index(m9)
    k_9 = arr2[m_9]
    del arr[m_9]
    del arr2[m_9]
    m10 = max(arr)
    m_10 = arr.index(m10)
    k_10 = arr2[m_10]
    del arr[m_10]
    del arr2[m_10]
    m11 = max(arr)
    m_11 = arr.index(m11)
    k_11 = arr2[m_11]
    del arr[m_11]
    del arr2[m_11]
    m12 = max(arr)
    m_12 = arr.index(m12)
    k_12 = arr2[m_12]
    del arr[m_12]
    del arr2[m_12]
    m13 = max(arr)
    m_13 = arr.index(m13)
    k_13= arr2[m_13]
    del arr[m_13]
    del arr2[m_13]
    m14 = max(arr)
    m_14 = arr.index(m14)
    k_14 = arr2[m_14]
    del arr[m_14]
    del arr2[m_14]
    m15 = max(arr)
    m_15 = arr.index(m15)
    k_15 = arr2[m_15]
    del arr[m_15]
    del arr2[m_15]
    m16 = max(arr)
    m_16 = arr.index(m16)
    k_16= arr2[m_16]
    del arr[m_16]
    del arr2[m_16]
    m17 = max(arr)
    m_17 = arr.index(m17)
    k_17 = arr2[m_17]
    del arr[m_17]
    del arr2[m_17]
    m18 = max(arr)
    m_18= arr.index(m18)
    k_18 = arr2[m_18]
    del arr[m_18]
    del arr2[m_18]
    m19= max(arr)
    m_19= arr.index(m19)
    k_19= arr2[m_19]
    del arr[m_19]
    del arr2[m_19]
    m20= max(arr)
    m_20 = arr.index(m20)
    k_20 = arr2[m_20]
    del arr[m_20]
    del arr2[m_20]
    x = ["{}".format(k_1),"{}".format(k_2),"{}".format(k_3),"{}".format(k_4),"{}".format(k_5),"{}".format(k_6),"{}".format(k_7),"{}".format(k_8),"{}".format(k_9),"{}".format(k_10),\
        "{}".format(k_11),"{}".format(k_12),"{}".format(k_13),"{}".format(k_14),"{}".format(k_15),"{}".format(k_16),"{}".format(k_17),"{}".format(k_18),"{}".format(k_19),"{}".format(k_20)]

    y = [m,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20]
    return x,y





