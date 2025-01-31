import logging
from datetime import datetime

import pandas as pd
import torch

logging.basicConfig(filename='log.log', encoding='utf8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    if torch.cuda.is_available():
        device = "cuda"
    else:
        logger.warning("Cuda not available.")
        devices = "cpu"

if __name__ == '__main__':
    main()