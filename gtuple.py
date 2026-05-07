#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pytest


class TupleMeta(type):
    pass


class Tuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args):
        if len(args) != 2:
            raise ValueError("Tuple takes 2 arguments")
        return super().__new__(cls, args)


def test_gtuple():
    tup = Tuple("a", "b")
    assert tup == ("a", "b")
    assert tup[0] == "a"
    assert tup[1] == "b"
    with pytest.raises(AttributeError):
        tup.x
    with pytest.raises(ValueError):
        tup = Tuple(1, 2, 3)


if __name__ == "__main__":
    tup = Tuple("a", "b")
    print(tup)
