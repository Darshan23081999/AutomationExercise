# import logging
#
# class logGen():
#     @staticmethod
#     def logger():
#         logging.basicConfig(filemode='..\\logs\\automation.log',format='%(asctime)s:%(levelname)s:%(message)s',deffmt='%m/%d/%y %I:%M:%s%p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger
#
import logging
import os
class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + "\\logs\\automation.log"
        logging.basicConfig(filename=path,format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
