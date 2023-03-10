from __future__ import annotations

from typing import Callable, Any

from core import Monad, A, B


class SideEffect(Monad[A]):
    def __init__(self, x: A):
        print("print on scrren: {}".format(x))
        self.x = x

    def __matmul__(self, f: Callable[[A], SideEffect[B]]) -> SideEffect[B]:
        return f(self.x)

    def pure(x: Any):
        return SideEffect(x)
