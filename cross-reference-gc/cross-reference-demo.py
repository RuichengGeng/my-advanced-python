import os
import psutil
import weakref

from memory_profiler import profile


class A(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._parent = weakref.ref(parent) if parent else parent
        # self._parent = parent
        self.children = set()
        self.workload = ' ' * 128 * 1024 * 1024

    @property
    def parent(self):
        if not self._parent:
            return self._parent
        _parent = self._parent()
        if _parent:
            return _parent
        else:
            raise LookupError("Parent was destroyed")

    def __del__(self):
        print("delete", self.name)


class B(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._parent = parent
        self.children = set()
        self.workload = ' ' * 128 * 1024 * 1024

    @property
    def parent(self):
        if not self._parent:
            return self._parent
        _parent = self._parent()
        if _parent:
            return _parent
        else:
            raise LookupError("Parent was destroyed")

    def __del__(self):
        print("delete", self.name)


@profile
def main():
    for _ in range(10):
        a = A(name=1)
        a.children.add(A(name=2, parent=a))
    for _ in range(10):
        b = B(name=1)
        b.children.add(B(name=2, parent=b))

    print("end")
    process = psutil.Process(os.getpid())
    print(f"memory usage {bytesto(process.memory_info().rss, 'g')} G")  # in Gb


if __name__ == "__main__":
    main()
