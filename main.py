


from config.config import get_cfg
from utils.basic_utils import project_preprocess
import logging



def main():
    
    cfg = get_cfg()
    cfg = project_preprocess(cfg)

    
    return


if __name__ == '__main__':
    main()