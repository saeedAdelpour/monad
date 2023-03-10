from __future__ import annotations

from typing import Optional, Callable
from core import Monad, A, B


class Maybe(Monad[A]):
    """

    this class interacts with functions that return a float or not
    suppose these functions
    def f(x: float) -> Optional[float]:
        pass
    def g(x: float) -> Optional[float]:
        pass

        "
        we need a pipeline of f and g.
        this functions may return a float or not,
        the problem is these functions may return differnt type
        we need a robust type for these functions to interact with each other
        "

    """

    def __init__(self, value: A = None) -> None:
        self.value = value

    def __matmul__(self, f: Callable[[A], Monad[B]]) -> Monad[B]:
        """
        we check the type of f arg only here
        there is no need to check type of f arg in each function
        """
        if self.value is not None:
            return f(self.value)
        return Maybe(None)

    def pure(x: A) -> Monad[A]:
        return Maybe(x)

    def __repr__(self) -> str:
        return "<monad.value: {}>".format(self.value)
