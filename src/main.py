import pandas as pd
import torch
import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='log.log', encoding='utf8', level=logging.DEBUG)
    if torch.cuda.is_available():
        device = "cuda"
    else:
        logger.warning("Cuda not available.")
        devices = "cpu"

if __name__ == '__main__':
    logger.error("Hello")
    main()