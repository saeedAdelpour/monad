from . import Computation


def f(a: int) -> Computation[float]:
    if a == 0:
        return Computation(error="Bad Input")
    return Computation(result=a - 1)


def g(x: int) -> Computation[str]:
    return Computation(result=str(x**2))


Computation.pure(3) @ f @ f @ f @ f @ g
