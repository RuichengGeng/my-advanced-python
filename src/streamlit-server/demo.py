import os
import logging
from my_functions import foo
import streamlit as st

logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
_logger = logging.getLogger("my_logger")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "log", "log_info.log")
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'))
_logger.addHandler(file_handler)


def main():
    _logger.info("Start up server...")
    # foo()
    st.write("Hello")
    st.write(foo())


if __name__ == "__main__":
    main()
