#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class TupleMeta(type):
    pass


class Tuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args):
        return super().__new__(cls, args)


if __name__ == "__main__":
    tup = Tuple(("a", "b"))
    print(tup)
