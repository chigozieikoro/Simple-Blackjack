import functools
def mapfunc(func, lst):
    if lst == []:
        return lst
    else:
        return [func(lst[0])] + mapfunc(func, lst[1:])


def filterfunc(func, lst):
    if lst == []:
        return lst
    elif func(lst[0]):
        return [lst[0]] + filterfunc(func,lst[1:])
    else:
        return filterfunc(func,lst[1:])


def reducefunc(agg, lst):
    if len(lst) == 0:
        raise TypeError("List cannot be of size 0 to use a reduce function")
    elif len(lst) == 1:
        return lst[0]
    else:
        return agg(lst[0], reducefunc(agg, lst[1:]))


def revstr(string):
    if string is None:
        return ""
    if len(string) == 0:
        return string
    else:
        return string[-1] + revstr(string[:len(string)-1])


"x =[{'key': 243}, {'key': 123456}, {'key': 124}]"

"print(mapfunc(lambda y: y['key'], x ))"

"[243,123456,124]"

mylst = [(2,3), (4,5,6), (99)]

mylst[1] = 23,107
print(mylst)




