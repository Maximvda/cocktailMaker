import logging
from logging.handlers import RotatingFileHandler

class BasicFormatter(logging.Formatter):
    def format(self, record):
        formatter = logging.Formatter("%(asctime)s\n%(levelname)s:%(name)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    green = "\x1b[32;20m"
    red = "\x1b[31;20m"
    blue = "\x1b[34;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    pre_fix = "%(asctime)s\n"
    format = "%(levelname)s:%(name)s - %(message)s"
    extra = " (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + pre_fix + blue + format + reset,
        logging.INFO: grey + pre_fix + green + format + reset,
        logging.WARNING: grey + pre_fix + yellow + format + reset,
        logging.ERROR: grey + pre_fix + red + format + reset,
        logging.CRITICAL: grey + pre_fix + bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

logging.basicConfig(level=logging.INFO)
logging.getLogger().handlers[0].setFormatter(CustomFormatter())

############################################
# Class that inits logger to write to file #
class Logger:
    def __init__(self, filename, logLevel=logging.INFO, handlers=[]):
        self.handlers = handlers
        #Creating and Configuring Logger
        my_handler = RotatingFileHandler(filename, mode='a', maxBytes=5*1024*1024,
                                         backupCount=5, encoding=None, delay=0)

        self.handlers.extend(my_handler)
        logging.basicConfig(format = CustomFormatter(),
                            level = logLevel,
                            handlers=self.handlers)

    def addHandler(self, handler):
        logging.getLogger().addHandler(handler)
