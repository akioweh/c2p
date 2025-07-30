from itertools import permutations
from functools import cache


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    @staticmethod
    def orien(a: 'Point', b: 'Point', c: 'Point'):
        res = (c.x - b.x) * (b.y - a.y) - (b.x - a.x) * (c.y - b.y)
        if res == 0:
            return 0
        elif res < 0:
            return -1
        else:
            return 1

    def __imatmul__(self, ax: 'Ax'):
        if ax.vert:
            self.x += 2 * (ax.v - self.x)
        else:
            self.y += 2 * (ax.v - self.y)
        return self


class Ax:
    def __init__(self, vert: bool, v: int, l: int, r: int):
        self.vert = vert
        self.v = v
        self.l = l
        self.r = r

    @classmethod
    def from_coords(cls, x1, y1, x2, y2):
        if x1 == x2:
            return cls(True, x1, min(y1, y2), max(y1, y2))
        else:
            return cls(False, y1, min(x1, x2), max(x1, x2))

    def __rmatmul__(self, p: Point) -> Point:
        if self.vert:
            return Point(p.x + 2 * (self.v - p.x), p.y)
        else:
            return Point(p.x, p.y + 2 * (self.v - p.y))


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @classmethod
    def from_coords(cls, x1, y1, x2, y2):
        return cls(Point(x1, y1), Point(x2, y2))

    @classmethod
    def from_ax(cls, ax: Ax):
        if ax.vert:
            return cls(Point(ax.v, ax.l), Point(ax.v, ax.r))
        else:
            return cls(Point(ax.l, ax.v), Point(ax.r, ax.v))

    def boxes(self, p: Point):
        xl, xr = self.p1.x, self.p2.x
        if xr < xl:
            xl, xr = xr, xl
        yl, yr = self.p1.y, self.p2.y
        if yr < yl:
            yl, yr = yr, yl
        return xl <= p.x <= xr and yl <= p.y <= yr

    def __contains__(self, p: Point):
        return self.boxes(p) and Point.orien(self.p1, p, self.p2) == 0

    def __imatmul__(self, ax: Ax):
        self.p1 @= ax
        self.p2 @= ax
        return self

    def intersects(self, other: 'Line'):
        o1 = Point.orien(self.p1, self.p2, other.p1)
        o2 = Point.orien(self.p1, self.p2, other.p2)
        o3 = Point.orien(other.p1, other.p2, self.p1)
        o4 = Point.orien(other.p1, other.p2, self.p2)

        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and self.boxes(other.p1):
            return True
        if o2 == 0 and self.boxes(other.p2):
            return True
        if o3 == 0 and other.boxes(self.p1):
            return True
        if o4 == 0 and other.boxes(self.p2):
            return True
        return False

    def orien(self) -> int:
        h = self.p2.x > self.p1.x
        v = self.p2.y > self.p1.y
        if v == h:
            return 0 if v else 2
        else:
            return 1 if v else 3


class Box(Line):
    def normalize(self):
        o = self.orien()
        if o == 0:
            return
        if o == 2:
            self.p1, self.p2 = self.p2, self.p1
        elif o == 1:
            self.p1.x, self.p2.x = self.p2.x, self.p1.x
        else:
            self.p1.y, self.p2.y = self.p2.y, self.p1.y

    def contains_ax(self, ax: Ax):
        if ax.vert:
            return self.p1.x <= ax.v <= self.p2.x and not (ax.l > self.p2.y or ax.r < self.p1.y)
        else:
            return self.p1.y <= ax.v <= self.p2.y and not (ax.l > self.p2.x or ax.r < self.p1.x)


def solve():
    N = read_int()
    TARGET = Point(*read_ints())
    walls_ax = [Ax.from_coords(*read_ints()) for _ in range(N)]
    walls_ln = [Line.from_ax(ax) for ax in walls_ax]

    @cache  # up to 8*8*4 = [small number] different states
    def get_cull_box(_src_idx: int, _dst_idx: int, _orien: int) -> Box | None:
        if _src_idx == -1:
            sx, sy = 0, 0
        else:
            _src = walls_ax[_src_idx]
            if _src.vert:
                sx = _src.v
                sy = _src.l if _orien <= 1 else _src.r
            else:
                sy = _src.v
                sx = _src.r if _orien == 1 or _orien == 2 else _src.l
        if _dst_idx == -1:
            dx, dy = TARGET.x, TARGET.y
        else:
            _dst = walls_ax[_dst_idx]
            if _dst.vert:
                dx = _dst.v
                dy = _dst.r if _orien <= 1 else _dst.l
            else:
                dy = _dst.v
                dx = _dst.l if _orien == 1 or _orien == 2 else _dst.r
        box = Box.from_coords(sx, sy, dx, dy)
        if box.orien() != _orien:
            return None  # misaligned orientation = target is behind
        box.normalize()
        return box

    def check_clearance(ray: Line, _src_idx: int, _dst_idx: int, _mask: list[bool]) -> bool:
        _cull_box = get_cull_box(_src_idx, _dst_idx, ray.orien())
        if _cull_box is None:
            return False
        return not any(ray.intersects(walls_ln[i]) for i in range(N) if _mask[i] and _cull_box.contains_ax(walls_ax[i]))

    wall_mask = [True] * N
    for ans in range(N, -1, -1):
        for order in permutations(range(N), ans):
            proj = TARGET.copy()
            for i in reversed(order):
                proj @= walls_ax[i]
            ray = Line(Point(0, 0), proj)
            prv_wall_idx = -1
            for step, cur_wall_idx in enumerate(order):
                wall_mask[cur_wall_idx] = False
                if not ray.intersects(walls_ln[cur_wall_idx]):
                    break
                if not check_clearance(ray, prv_wall_idx, cur_wall_idx, wall_mask):
                    break
                ray @= walls_ax[cur_wall_idx]
                prv_wall_idx = cur_wall_idx
            else:  # make sure path to hole is now obstructionless
                if check_clearance(ray, prv_wall_idx, -1, wall_mask):
                    write_int(ans)
                    return
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
