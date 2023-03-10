from . import SideEffect


def show_multiply_by_2(x: int) -> SideEffect[int]:
    return SideEffect(x * 2)
