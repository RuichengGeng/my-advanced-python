import abc

import numpy as np
import pandas as pd


class CalculationServicer(abc.ABC):
    @abc.abstractmethod
    def add(self, *args):
        ...


class CalculationServicerImplementation(CalculationServicer):
    def __init__(self):
        print("Initiating calculation servicer...")

    def add(self, *arg) -> float:
        return sum(*arg)
