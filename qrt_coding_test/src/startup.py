import os
import sys
import logging
from http.server import HTTPServer

import domain
from servicers import OptimizationServer

sys.path.append(os.path.join("src"))


def main(http_config: domain.HttpServerConfig):
    web_server = HTTPServer(
        (http_config.host_name, http_config.port), OptimizationServer
    )
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        web_server.server_close()
        _logger.error("Server stopped.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    _logger = logging.getLogger(__name__)
    _logger.info("Set up logger")

    # http configuration
    _http_config = domain.HttpServerConfig(host_name="localhost", port=8080)
    _logger.info(f"Server starting http://{_http_config.host_name}:{_http_config.port}")
    main(_http_config)
