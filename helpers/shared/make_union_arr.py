
def make_union_arr(arr_1, arr_2):
    a_set = set(arr_1)
    b_set = set(arr_2)
    c_set = a_set & b_set
    res = list(c_set)
    return res
