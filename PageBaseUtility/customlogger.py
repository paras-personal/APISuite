import inspect
import logging
import os
from datetime import date


def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_folder_path = os.path.join(os.path.abspath(__file__ + '/../../'), 'Logs')
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        log_file_path = os.path.join(log_folder_path, f'Logs_{date.today()}.log')
        fileHnadler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        fileHnadler.setLevel(logLevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHnadler.setFormatter(formatter)
        logger.addHandler(fileHnadler)
    return logger