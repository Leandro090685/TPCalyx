import logging
import os


class Logs:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("logs/report_logs.txt", mode='a')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s','%d/%m/%Y - %H:%M:%S')
        file_handler.setFormatter(formatter)
        

        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)