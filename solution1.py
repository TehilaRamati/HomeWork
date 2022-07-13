import operator
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def replace_formula(curr, arr):
    res = ''
    open = curr.count("{")
    close = curr.count("}")
    if open == close:
        if open > 0:
            while open > 0:
                open -= 1
                a = curr.split("{")[1]
                b = a.split("}")[0]
                res = curr.replace("{" + b + "}", arr[int(b)])
        else:
            res = str(curr)
    else:
        raise Exception ("Invalid formula")
    return res


def calc(arr):
    res = ''
    index = 0
    while index < len(arr):
        if not arr[index].isdigit():
            res = str(operators[arr[index]](int(res), int(arr[index + 1])))
            index += 1
        else:
            res = res + arr[index]
        index += 1
    return res


def print_list(input_array):
    index = 0
    new_list = []
    while index < len(input_array):
        print("[{}: {}]".format(index, input_array[index]), end=" ")

        index += 1
    print("\n")


def prepare_array(input_list):
    orgin_list = input_list.copy()

    index = 0
    while index < len(input_list):
        import re
        curr = replace_formula(input_list[index], input_list)
        curr = re.split('(\W+)', curr)
        curr = calc(curr)
        input_list[index] = curr
        index += 1
    print_list(input_list)
    return orgin_list


def change_value(input_array, cell, value):
    input_array[cell] = str(value)
    org_array = prepare_array(input_array)
    org_array[cell] = str(value)
    return org_array


if __name__ == '__main__':
    # input = "2,18,=2*{0},9,={2}+1*5"
    input = "2,18,=20*{0}*{0},9,={2}+1*50"
    print("#Input_file: \n{}".format(input))
    input_array = input.replace('=', '').split(',')

    print("#a:")
    input_arr = prepare_array(input_array)
    print("#b:")
    input_arr = change_value(input_arr, 0, 3)
    print("#c:")
    change_value(input_arr, 2, 1)
