from __future__ import annotations
import os
import psutil
import weakref

import anytree
from memory_profiler import profile
from typing import Optional

import numpy as np

import utils


class MyNode(anytree.Node):
    def __init__(
        self,
        name: str,
        parent: Optional[MyNode] = None,
        children: Optional[list[MyNode]] = [],
        data: Optional[np.ndarray] = None
    ):
        if children is None:
            children = []
        self._data = data
        super().__init__(name=name, parent=parent, children=children)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d: np.ndarray):
        self._data = d

    def __del__(self):
        print(f"Delete my node : {self.name}")


class MyEfficientNode(anytree.Node):
    def __init__(
        self,
        name: str,
        data: Optional[np.ndarray] = None,
        parent: Optional[MyEfficientNode] = None,
        children: Optional[list[MyEfficientNode]] = [],
    ):
        if not parent:
            _parent = None
        else:
            _parent = weakref.ref(parent)()
        self._parent = _parent
        self._data = data
        self._children = children
        self._name = name
        super().__init__(
            name=self._name,
            parent=self._parent,
            children=self._children
        )

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, p: Optional[MyEfficientNode]):
        if p is None:
            self._parent = None
        else:
            _parent = weakref.ref(p)()
            self._parent = _parent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d: np.ndarray):
        self._data = d

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, c: list[MyEfficientNode]):
        self._children = c

    def __del__(self):
        print(f"Delete my efficient node : {self.name}")


class MyObject:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n

    def __del__(self):
        print(f"Delete my node : {self.name}")


def _np_data_provider(num: int) -> np.ndarray:
    return np.random.randn(num)


def func1():
    for _ in range(10):
        a = MyEfficientNode(name="1", data=_np_data_provider(100_000))
        b = MyEfficientNode(name="2", parent=a, data=_np_data_provider(100_000))


def func2():
    for _ in range(10):
        a = MyNode(name="1", data=_np_data_provider(100_000))
        b = MyNode(name="2", parent=a, data=_np_data_provider(100_000))


@profile
def main():
    func1()
    func2()
    print("end")

    process = psutil.Process(os.getpid())
    print(f"memory usage {utils.bytesto(process.memory_info().rss, 'm')} M")  # in MB


if __name__ == "__main__":
    main()
    print("end of program")
