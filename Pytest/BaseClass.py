import logging

class BaseClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger