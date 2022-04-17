from graph import show_graph
from generation import data_matrix, get_res_vector_by_variables
from func import get_net, get_y, new_weight, report_print


variables, table = data_matrix()


def get_table_with_weights(weights):
    res = []
    for i in range(len(variables)):
        net = get_net(weights, variables[i])
        y = get_y(net, 2)
        res += [y]
    return res


def main_algorithm(res, vars_, errors, weight_vector, task_number):
    for i in range(len(vars_)):
        # get y
        net = get_net(weight_vector, vars_[i])
        y = get_y(net, task_number)
        res += [y]
        # check result
        delta = table[i] - y
        errors += [abs(delta)]
        if delta != 0:
            weight_vector[0] = new_weight(weight_vector[0], delta, 1, task_number)
            for j in range(1, len(weight_vector)):
                weight_vector[j] = new_weight(weight_vector[j], delta, vars_[i][j - 1], task_number)


def task(task_number, res=None):
    print("Task number:", task_number)
    if res is None:
        res = []
    weight_vector = [0, 0, 0, 0, 0]
    epoh_errors = []
    era = 1
    while res != table:
        res = []
        errors = []
        main_algorithm(res, variables, errors, weight_vector, task_number)
        report_print(epoh_errors, errors, era, weight_vector, res)
    show_graph(epoh_errors)


def last_task(task_number):
    print("Task number:", task_number)
    w_res, num_ep, count_el = 0, 0, 0
    new_variables, del_item, index_from_start = variables[:len(variables) - 1], variables[len(variables) - 1], 15
    while True:
        res = []
        weight_vector = [0, 0, 0, 0, 0]
        ep = 0
        tmp = get_res_vector_by_variables(new_variables)
        epoh_errors = []
        era = 1
        while res != tmp:
            res = []
            errors = []
            main_algorithm(res, new_variables, errors, weight_vector, task_number)
            ep += 1
            if ep >= 100:
                break
            report_print(epoh_errors, errors, era, weight_vector, res)
        # Search element for delete
        if get_table_with_weights(weight_vector) != table:
            new_variables += [del_item]
        if index_from_start == 0:
            break
        del_item = new_variables[index_from_start - 1]
        del new_variables[index_from_start - 1]
        index_from_start -= 1
        # Variables for report
        w_res = weight_vector
        count_el = len(new_variables)
        num_ep = ep
    print("\n\n\n------------------------------------------------------------------------------------------------")
    print("Final weights for task", task_number, ":", w_res)
    print("Number of epochs", num_ep)
    print("Count of elements for study", count_el)


if __name__ == '__main__':
    task(1)
    task(2)
    last_task(3)
