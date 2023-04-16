import inspect
import logging
import os


def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_folder_path = os.path.join(os.path.abspath(__file__ + '/../../'), 'Logs')
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        fileHnadler = logging.FileHandler("Automation".format(loggerName), mode='w', encoding='utf-8')
        fileHnadler.setLevel(logLevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHnadler.setFormatter(formatter)
        logger.addHandler(fileHnadler)
    return logger