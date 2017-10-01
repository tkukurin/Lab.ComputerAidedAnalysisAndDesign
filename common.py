import numpy as np

# https://stackoverflow.com/questions/1301735/counting-python-method-calls-within-another-method
def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__= fn.__name__
    return wrapper

def counts(fn):
    def wrapper(f, *args, **kwargs):
        f.called = 0
        try:
            return fn(f, *args, **kwargs)
        finally:
            wrapper.calls_to_function = f.called
    wrapper.__name__= fn.__name__
    return wrapper

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def lmap(f, x):
    return np.array(list(map(f, x)))

def swap(lst, index1, index2):
    tmp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = tmp
    return lst

pt = lambda *x: np.array(x, dtype=float)
dim = lambda pt: len(pt)
