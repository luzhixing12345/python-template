


from config.config import get_cfg
from utils.utils import project_preprocess, get_logger


def main():
    
    cfg = get_cfg()
    cfg = project_preprocess(cfg)
    logger = get_logger()
    logger.info("start job")
    logger.info('end job')
    return


if __name__ == '__main__':
    main()
