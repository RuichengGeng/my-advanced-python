import dataclasses
import enum


@dataclasses.dataclass(frozen=True, eq=True)
class HttpServerConfig:
    host_name: str
    port: int


@dataclasses.dataclass(frozen=True, eq=True)
class Contract:  # order information
    name: str  # name of the order
    start_hour: int  # start time of the order
    end_hour: int  # end time of the order
    duration: int  # duration of the order
    price: int  # price of the order


@dataclasses.dataclass(frozen=True, eq=True)
class OptimalSolution:  # optimal solution
    name: str


@dataclasses.dataclass(frozen=True, eq=True)
class ShipRentalOptimalSolution(
    OptimalSolution
):  # optimal solution for the spaceship rental problem
    income: int  # total income of the optimal order
    path: list[str]  # order execution list


class OptimizationProblems(enum.Enum):
    SPACESHIP_OPTIMIZE = enum.auto()
