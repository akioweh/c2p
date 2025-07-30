from itertools import permutations
from fractions import Fraction


class Vec2:
    def __init__(self, x: Fraction | int, y: Fraction | int):
        self.x = Fraction(x)
        self.y = Fraction(y)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __add__(self, other: 'Vec2'):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2'):
        return self + (-other)

    def __mul__(self, a: Fraction):
        return self.__class__(self.x * a, self.y * a)

    def __xor__(self, other: 'Vec2') -> Fraction:
        return self.x * other.x + self.y * other.y

    def __matmul__(self, ax: 'Wall'):
        return self.__class__(-self.x, self.y) if ax.vert else self.__class__(self.x, -self.y)


class Point(Vec2):
    def __matmul__(self, ax: 'Wall'):
        if ax.vert:
            return self.__class__(self.x + 2 * (ax.v - self.x), self.y)
        else:
            return self.__class__(self.x, self.y + 2 * (ax.v - self.y))


class Wall:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.vert = x1 == x2 and x1 != 0
        self.v = x1 if self.vert else y1
        self.upper = max(y1, y2) if self.vert else max(x1, x2)
        self.lower = min(y1, y2) if self.vert else min(x1, x2)

    def __contains__(self, p: Point) -> bool:
        v = p.x if self.vert else p.y
        r = p.y if self.vert else p.x
        return v == self.v and self.lower <= r <= self.upper


class Ray:
    def __init__(self, origin: Point, dv: Vec2):
        self.A = origin
        self.dv = dv

    def __call__(self, t: Fraction) -> Point:
        return self.A + self.dv * t

    def collide_on(self, ax: Wall) -> tuple[Fraction, Point] | None:
        if ax.vert:
            x = ax.v
            if Vec2(x - self.A.x, 0) ^ self.dv <= 0:  # direction culling
                return None
            t = (x - self.A.x) / self.dv.x
        else:
            y = ax.v
            if Vec2(0, y - self.A.y) ^ self.dv <= 0:
                return None
            t = (y - self.A.y) / self.dv.y
        res = self(t)
        if res not in ax:
            return None
        return t, res


def solve():
    N = read_int()
    TARGET = Point(*read_ints())
    walls = [Wall(*read_ints()) for _ in range(N)]
    walls.append(Wall(TARGET.x, TARGET.y, TARGET.x, TARGET.y))  # used in final obstruction check

    def trace_ray(_ray: Ray, mask: list[bool]) -> tuple[int, tuple[Fraction, Point]] | None:
        _cols = [(i, res) for i in range(N + 1) if mask[i] and (res := _ray.collide_on(walls[i])) is not None]
        return min(_cols, key=lambda v: v[1][0], default=None)

    wall_mask = [True] * N + [False]
    for ans in range(N, -1, -1):
        for order in permutations(range(N), ans):
            proj = TARGET
            for i in reversed(order):
                proj @= walls[i]
            ray = Ray(Point(0, 0), Vec2(proj.x, proj.y))
            for step in range(ans):
                if (res := trace_ray(ray, wall_mask)) is None:
                    break
                col_wall_idx, (_, col_point) = res
                if col_wall_idx != order[step]:
                    break
                ray = Ray(col_point, ray.dv @ walls[col_wall_idx])
                wall_mask[order[step]] = False
            else:  # make sure path to hole is now obstructionless
                wall_mask[N] = True
                if (res := trace_ray(ray, wall_mask)) is not None and res[0] == N:
                    write_int(ans)
                    return
                wall_mask[N] = False
            for i in range(N):
                wall_mask[i] = True

    write_str('impossible')


### Python 3.10-3.13 compatible competitive programming template ###
# 23 July 2025 Version
from collections.abc import Callable, Iterable, Iterator
from sys import stdin, stdout
from typing import TypeVar

T = TypeVar('T')

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: type[int] = int) -> int:
    """Reads a line as a single integer"""
    return int_t(srdl())


def read_str() -> str:
    """Reads a line as-is"""
    return srdl().strip()


def write_ints(arr: Iterable[int]):
    """Writes a list of integers as a space-separated line"""
    swrt(' '.join(map(str, arr)))
    swrt('\n')


def write_int(val: int):
    """Writes a single integer as a line"""
    swrt(str(val))
    swrt('\n')


def write_str(val: str):
    """Writes a single string as a line"""
    swrt(val)
    swrt('\n')


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:  # type: ignore[assignment]
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# Single-case format
if __name__ == '__main__':
    solve()
