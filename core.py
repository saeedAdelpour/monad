"""
mondas in a design pattern in functional programming

we need three functions for monad
1- contain value
2- turn a value in monad
3- apply function to interact with value
"""
from __future__ import annotations
from typing import TypeVar, Generic, Callable

A = TypeVar("A")
B = TypeVar("B")


class Monad(Generic[A]):
    def __matmul__(self, f: Callable[[A], Monad[B]]) -> Monad[B]:
        pass

    def pure(x: A) -> Monad[A]:
        pass
