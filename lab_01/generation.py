def data_matrix():
    bool_vars = [False, True]
    vars_ = []
    res = []
    for x1 in bool_vars:
        for x2 in bool_vars:
            for x3 in bool_vars:
                for x4 in bool_vars:
                    res_func = (not x1 or not x2 or not x3) and (not x2 or not x3 or x4)
                    vars_ += [[x1, x2, x3, x4]]
                    res += [res_func]
    return vars_, res


def get_res_vector_by_variables(arr_x):
    res = []
    for els in arr_x:
        res += [(not els[0] or not els[1] or not els[2]) and (not els[1] or not els[2] or els[3])]
    return res
