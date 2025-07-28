from random import getrandbits


class hish(int):
    salt = getrandbits(64)
    def __hash__(self):
        return super().__hash__() ^ hish.salt

