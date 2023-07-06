import pytest
import domain
from servicers import optimization_servicer


@pytest.fixture(scope="function")
def ship_rental_optimizer() -> optimization_servicer.ShipRentalOptimizer:
    return optimization_servicer.ShipRentalOptimizer()


@pytest.mark.parametrize(
    (
        "contracts",
        "expected_result",
    ),
    [
        # normal case
        (
            [
                domain.Contract("1", 0, 5, 5, 10),
                domain.Contract("2", 3, 10, 7, 14),
                domain.Contract("3", 5, 14, 9, 8),
                domain.Contract("4", 5, 14, 9, 7),
            ],
            domain.ShipRentalOptimalSolution(
                name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
                income=18,
                path=["1", "3"],
            ),
        ),
        # edge case1: 2 contract competing
        (
            [
                domain.Contract("1", 0, 5, 5, 10),
                domain.Contract("2", 0, 10, 10, 11),
            ],
            domain.ShipRentalOptimalSolution(
                name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
                income=11,
                path=["2"],
            ),
        ),
        # case 3
        (
            [
                domain.Contract("1", 1, 3, 2, 20),
                domain.Contract("2", 2, 5, 3, 20),
                domain.Contract("3", 3, 10, 7, 100),
                domain.Contract("4", 4, 6, 2, 70),
                domain.Contract("5", 6, 9, 3, 60),
            ],
            domain.ShipRentalOptimalSolution(
                name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
                income=150,
                path=["1", "4", "5"],
            ),
        ),
        # case 4
        (
            [
                domain.Contract("1", 1, 3, 2, 50),
                domain.Contract("2", 2, 4, 2, 10),
                domain.Contract("3", 3, 5, 2, 40),
                domain.Contract("4", 3, 6, 3, 70),
            ],
            domain.ShipRentalOptimalSolution(
                name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
                income=120,
                path=["1", "4"],
            ),
        ),
        # case 5
        (
            [
                domain.Contract("1", 1, 2, 1, 5),
                domain.Contract("2", 1, 3, 2, 6),
                domain.Contract("3", 1, 4, 3, 4),
            ],
            domain.ShipRentalOptimalSolution(
                name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
                income=6,
                path=["2"],
            ),
        ),
    ],
)
def test_func(contracts, expected_result, ship_rental_optimizer):
    result = ship_rental_optimizer.do_optimization(contracts)
    assert result.name == expected_result.name
    assert result.income == expected_result.income
    assert set(result.path) == set(expected_result.path)
