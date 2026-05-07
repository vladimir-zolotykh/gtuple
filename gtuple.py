#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from operator import itemgetter
import pytest


class TupleBase(tuple):
    def __init_subclass__(cls, *args):
        super().__init_subclass__(*args)
        fields = cls._fields if hasattr(cls, "_fields") else []
        for n, field in enumerate(fields):
            setattr(cls, field, property(itemgetter(n)))


class Tuple(TupleBase):
    def __new__(cls, *args):
        if hasattr(cls, "_fields") and len(args) != len(cls._fields):
            raise ValueError(f"{cls.__name__} takes {len(cls._fields)} arguments")
        return super().__new__(cls, args)


class Point(Tuple):
    _fields = ["x", "y"]


class Exercise(Tuple):
    _fields = ["exercise_name", "weight", "reps"]


def test_point():
    p = Point(10, 20)
    assert (p[0], p[1]) == (10, 20)
    assert (p.x, p.y) == (10, 20)
    with pytest.raises(ValueError) as err:
        p = Point(10, 20, 30)
    assert str(err.value) == "Point takes 2 arguments"


def test_exercise():
    dat = ("squat", 90.0, 3)
    e = Exercise(*dat)
    assert (e.exercise_name, e.weight, e.reps) == dat


def test_gtuple():
    dat = ("a", "b")
    tup = Tuple(*dat)
    assert tup == dat
    assert (tup[0], tup[1]) == dat
