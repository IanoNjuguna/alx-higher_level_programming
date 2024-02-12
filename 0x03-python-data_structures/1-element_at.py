def element_at(my_list, idx):

    list_length = len(my_list) - 1

    if my_list[idx] < 0:
        return None
    elif my_list[idx] >= list_length:
        return None
    else:
        return my_list[idx]
