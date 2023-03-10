from __future__ import annotations
from typing import Callable, List as ListType
from itertools import chain


from core import Monad, A, B


class List(Monad[A]):
    def __init__(self, l: ListType[A]):
        self.l = l

    def __matmul__(self, f: Callable[[A], List[B]]) -> List[B]:
        return List(list(chain(*map(f, self.l))))

    def pure(x: A):
        return List([x])

    def __repr__(self) -> str:
        return f"List {self.l}"
