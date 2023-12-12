import dis


def for_loop(n):
    my_list = []
    for x in range(n):
        my_list.append(x)
    return my_list


def list_comp(n):
    return [x for x in range(n)]


dis.dis(for_loop)
dis.dis(list_comp)
