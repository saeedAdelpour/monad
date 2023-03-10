from .maybe import Maybe


def f(x: float) -> Maybe[float]:
    if x == 0:
        return Maybe(None)
    return Maybe(1 / x)


def g(x: float) -> Maybe[float]:

    if x < (1 / 5):
        return Maybe(None)

    return Maybe(3 + x)


f(1) @ g @ g @ g
