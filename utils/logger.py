# encoding: utf-8
"""
@author:  sherlock
@contact: sherlockliao01@gmail.com
"""

import logging
import logging.config
import os

def set_logger(cfg):
    logging.config.fileConfig(cfg.LOG_CONFIGURATION)
    logger = logging.getLogger('LOGGER')
    
    file_handler = logging.FileHandler(os.path.join(cfg.OUTPUT_DIR, f"{cfg.PROJECT_NAME}.log"))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logger.handlers[0].formatter)
    logger.addHandler(file_handler)
    
    
def get_logger():
    return logging.getLogger('LOGGER')
