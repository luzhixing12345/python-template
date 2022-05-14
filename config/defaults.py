from yacs.config import CfgNode as CN
import os

_C = CN()
_C.PROJECT_NAME = "project_name"
# ---------------------------------------------------------------------------- #
# Misc options
# ---------------------------------------------------------------------------- #

_C.OUTPUT_DIR = "log"

_C.LOG_CONFIGURATION = "config/logging.conf"