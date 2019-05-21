#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = None
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("Wrong type")
        except IndexError:
            print("out of range")
        finally:
            if res is not None:
                new_list.append(res)
            else:
                new_list.append(0)
    return (new_list)
