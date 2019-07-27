def _list(f):
    def w(*args, **kwargs):
        return list(f(*args, **kwargs))
    return w


@_list
def append(l1, l2):
    yield from l1
    yield from l2


@_list
def concat(l):
    while l:
        e, *l = l
        yield from e


@_list
def filter(f, l):
    for e in l:
        if f(e):
            yield e


def length(l):
    r = 0
    while l:
        _, *l = l
        r += 1
    return r


@_list
def map(f, l):
    while l:
        e, *l = l
        yield f(e)


def foldl(f, l, i):
    while l:
        e, *l = l
        i = f(i, e)
    return i


def foldr(f, l, i):
    while l:
        *l, e = l
        i = f(e, i)
    return i


@_list
def reverse(l):
    while l:
        *l, e = l
        yield e
