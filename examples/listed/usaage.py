from .listed import List

double = lambda e: [e * 2]
power = lambda e: [e**2]

List.pure(3) @ double @ power
List([1, 2, 3, 4]) @ power @ double
