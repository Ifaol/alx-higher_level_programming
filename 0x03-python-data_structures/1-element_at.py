#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    elif length < idx + 1:
        return None
    else:
        return (my_list[idx])
