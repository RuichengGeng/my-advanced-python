import abc
import copy
import logging

import domain

_logger = logging.getLogger(__name__)


class ProblemSpecificOptimizer(abc.ABC):
    @abc.abstractmethod
    def do_optimization(self, data: list) -> domain.OptimalSolution:
        pass


class ShipRentalOptimizer(ProblemSpecificOptimizer):
    def __init__(self):
        pass

    def do_optimization(
        self, data: list[domain.Contract]
    ) -> domain.ShipRentalOptimalSolution:
        """
        use dynamic programming to solve the optimal ship rental problem.
        The core of dp is to find the transition equation between state i and i + 1.
        In this problem, we define state i is first i contracts and i+1 is state i + 1 more contract,
        so we have 2 choice when i + 1 comes:
            * don't do i + 1, then fun[i+1] = f[i]
            * do i + 1, then f[i+1] = f[j] + price[i+1], where j satisfies that end_hour[j] <= start_hour[i].
        So we iterate over all sorted contracts(sort by end time) and a inner reverse loop over [i, i - 1, ...,0] to find
        a suitable s.t end hour of contact j is earlier than start time of i. In this step, we could use bisection finder
        to reduce time complexity from O(n) to O(log(n)).
        One special case is that for just competing contract: (start, end, price) = (0, 1 , 1) and (0, 2 , 2), it is not
        covered by previous discussion, so we add a fake contract(0, 0, 0) at the very beginning.
        Args:
            data: list of contracts

        Returns:
            optimal solution, consisting of income and path
        """

        def _find_most_recent_previous_contract(current_contract_idx: int) -> int:
            """
            Use bisection method to find the most recent available contract index
            Args:
                current_contract_idx: current contract index

            Returns:
                int: most recent available previous contract index
            """
            if current_contract_idx == 1:
                return 0
            _current_contract_start_hour = contracts[current_contract_idx].start_hour
            _left, _right = 0, current_contract_idx
            while _left <= _right:
                mid = int((_left + _right) / 2)
                if contracts[mid].end_hour > _current_contract_start_hour:
                    _right = mid - 1
                else:
                    _left = mid + 1
            return _right

        _logger.info("Doing optimization on ship rental optimization...")
        number_of_contracts = len(data)
        contracts = sorted(data, key=lambda p: p.end_hour)  # sort contract by end time
        contracts = [
            domain.Contract("fake", 0, 0, 0, 0)
        ] + contracts  # add a fake contract at start to deal with edge cases
        dp = [0] * (number_of_contracts + 1)  # dp result recorder
        path = []
        for _ in range(number_of_contracts + 1):
            path.append([0] * (number_of_contracts + 1))
        for contract_idx in range(1, number_of_contracts + 1):
            dp[contract_idx] = dp[contract_idx - 1]  # assign optimal of i = i - 1
            path[contract_idx] = copy.deepcopy(
                path[contract_idx - 1]
            )  # assign optimal of i = i - 1
            most_recent_previous_contract = _find_most_recent_previous_contract(
                contract_idx
            )
            if (
                dp[most_recent_previous_contract] + contracts[contract_idx].price
                > dp[contract_idx]
            ):  # find better result
                dp[contract_idx] = (
                    dp[most_recent_previous_contract] + contracts[contract_idx].price
                )
                # once find better result, do dp path update
                path[contract_idx][: most_recent_previous_contract + 1] = copy.deepcopy(
                    path[most_recent_previous_contract][
                        : most_recent_previous_contract + 1
                    ]
                )
                path[contract_idx][most_recent_previous_contract + 1 : contract_idx] = [
                    0
                ] * (contract_idx - most_recent_previous_contract - 1)
                path[contract_idx][contract_idx] = contract_idx
        final_path = [int(i) for i in path[-1] if i]
        contract_name = [contracts[i].name for i in final_path]
        return domain.ShipRentalOptimalSolution(
            name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
            income=dp[number_of_contracts],
            path=contract_name,
        )


class Optimizer:
    def __init__(self, optimizers: dict[str, ProblemSpecificOptimizer]):
        self._optimizers = optimizers

    def do_optimization(self, data: list, task_name: str) -> domain.OptimalSolution:
        return self._optimizers[task_name].do_optimization(data)
