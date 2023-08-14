import streamlit
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)
_logger = logging.getLogger(__name__)


class MyClass:
    def __init__(self):
        _logger.info("Initiate my data class...")
        self.data = [1, 2, 3]

    def my_data(self):
        _logger.info("return data my data class...")
        return self.data


@streamlit.cache_resource
def cache_my_class():
    _logger.info("getting cached my class")
    return MyClass()


def update_my_data(data: MyClass):
    data.data = [4, 5, 6]


if "logger" not in streamlit.session_state:
    streamlit.session_state["logger"] = logging.getLogger("streamlit_server")

if "my_class_data" not in streamlit.session_state:
    streamlit.session_state["my_class_data"] = cache_my_class()


streamlit.session_state["logger"].info("start up server....")
streamlit.write("data")
streamlit.write(cache_my_class().my_data())
streamlit.write("end of data")

update_my_data(cache_my_class())

streamlit.write(cache_my_class().my_data())
streamlit.write("end of data2")
