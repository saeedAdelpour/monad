from __future__ import annotations
from typing import Callable
from core import Monad, A, B


class Computation(Monad[A]):
    """this class does error handling"""

    def __init__(self, *, result=None, error=None):
        self.result = result
        self.error = error

    def __matmul__(self, f: Callable[[A], Computation[B]]) -> Computation[B]:
        if self.error is not None:
            return Computation(error=self.error + "\nError Ocuured in perv computation")
        return f(self.result)

    def pure(x: A):
        return Computation(result=x)

    def __repr__(self) -> str:
        return f"Computation result={self.result} error={self.error}"
