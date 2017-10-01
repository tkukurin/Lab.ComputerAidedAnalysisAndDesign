import numpy as np

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def lmap(f, x):
    return np.array(list(map(f, x)))

def swap(lst, index1, index2):
    tmp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = tmp
    return lst