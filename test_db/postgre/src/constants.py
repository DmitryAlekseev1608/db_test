import logging

from hydra import compose, initialize

initialize(version_base=None, config_path="../../../configs", job_name="app")

MAIN = compose(config_name="main")
GREENPLUM = compose(config_name="greenplum")

match MAIN.LOGGING_LEVEL:
    case "ERROR":
        LOGGING_LEVEL = logging.ERROR
    case "INFO":
        LOGGING_LEVEL = logging.INFO
