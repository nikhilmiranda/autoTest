import logging
import inspect

def customLogger(logLevel = logging.DEBUG):

    # [Check Blue 12.7] 'inspect' gets the name of the Class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt = '%d.%m.%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
