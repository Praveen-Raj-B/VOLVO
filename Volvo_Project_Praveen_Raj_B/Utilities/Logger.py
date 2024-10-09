import logging
import os

class Logger:
    @classmethod
    def setupLogger(cls, name, filePath, fileMode, level=logging.INFO):
        if not os.path.isdir(filePath.split("/")[0]):
            os.makedirs(filePath.split("/")[0])
        formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
        handler = logging.FileHandler('./' + filePath, mode=fileMode, encoding="utf-8")
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger
