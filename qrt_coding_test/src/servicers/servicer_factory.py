import functools
import domain
from servicers import optimization_servicer


class ServiceProvider:
    def __init__(self):
        pass

    @functools.cached_property
    def _ship_rental_optimizer(self) -> optimization_servicer.ShipRentalOptimizer:
        return optimization_servicer.ShipRentalOptimizer()

    @functools.cached_property
    def optimizer(self) -> optimization_servicer.Optimizer:
        return optimization_servicer.Optimizer(
            optimizers={
                domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name: self._ship_rental_optimizer
            }
        )
