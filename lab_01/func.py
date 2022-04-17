CONST_NU = 0.3


def func(num):
    return 0.5 * (num / (1 + abs(num)) + 1)


def derivate(num):
    if num > 0:
        return -0.5 * (num / pow(1 + num, 2)) + 0.5 / (1 + num)
    return 0.5 * (num / pow(1 - num, 2)) + 0.5 / (1 - num)


def get_net(weight_vector, data_vector):
    res = weight_vector[0]
    for i in range(len(data_vector)):
        res += data_vector[i] * weight_vector[i + 1]
    return res


def new_weight(current_weight, sigma, x, task_number):
    if task_number == 1:
        return current_weight + CONST_NU * sigma * x
    return current_weight + CONST_NU * sigma * derivate(x) * x


def get_y(net, task_number):
    if task_number == 1:
        return net >= 0
    return func(net) >= 0.5


def report_print(epoh_errors, errors, era, weight_vector, res):
    epoh_errors += [sum(errors)]
    print("era:", era)
    print("\t- weight vector", weight_vector)
    print("\t- current vector of values:", res)
    print("\t- epochs errors:", epoh_errors[len(epoh_errors) - 1])
    era += 1

