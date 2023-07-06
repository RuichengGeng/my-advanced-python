import functools
import json
import logging
import traceback
import urllib.parse
from http.server import BaseHTTPRequestHandler

import domain
from servicers import servicer_factory
from _typing import JsonDict, JsonList

_logger = logging.getLogger(__name__)


def _parse_contract_data(data: JsonList) -> list[domain.Contract]:
    _contracts = []
    for contract in data:
        _contracts.append(
            domain.Contract(
                name=contract["name"],
                start_hour=contract["start"],
                end_hour=contract["start"] + contract["duration"],
                duration=contract["duration"],
                price=contract["price"],
            )
        )
    return _contracts


def _get_task_name(url_path: str) -> str:
    return "_".join(url_path.split("/"))[1:].upper()


class OptimizationServer(BaseHTTPRequestHandler):
    @functools.cached_property
    def _servicer_factory(self) -> servicer_factory.ServiceProvider:
        return servicer_factory.ServiceProvider()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello QRT! This is Ruicheng.".encode("utf-8"))

    def do_POST(self):
        url_path = urllib.parse.urlparse(self.path)
        task_name = _get_task_name(url_path.path)
        _logger.info(f"Doing a post request: {task_name}")
        if task_name == domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name:
            self._ship_rental_optimization()
        else:
            _logger.warning(f"post task: {task_name} is not supported!")
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({}).encode("utf-8"))

    def _ship_rental_optimization(self) -> None:
        try:
            test_data = self._get_data_from_post()
            _logger.info(f"Parsing contract data from http input...")
            contract_data = _parse_contract_data(test_data)
            _logger.info(f"There are {len(contract_data)} contracts...")
            optimization_result = self._servicer_factory.optimizer.do_optimization(
                data=contract_data,
                task_name=domain.OptimizationProblems.SPACESHIP_OPTIMIZE.name,
            )
            optimization_result_dict = self._parse_optimal_result(optimization_result)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(optimization_result_dict).encode("utf-8"))
        except Exception:
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({"info": "Ship rental optimization task failed"}).encode(
                    "utf-8"
                )
            )
            _logger.error(traceback.format_exc())

    def _get_data_from_post(self) -> JsonList:
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)
        test_data = json.loads(post_body)
        return test_data

    def _parse_optimal_result(self, result: domain.OptimalSolution) -> JsonDict:
        if isinstance(result, domain.ShipRentalOptimalSolution):
            return {"income": result.income, "path": result.path}
        else:
            raise NotImplementedError(
                "Other optimization problems are not supported yet"
            )
