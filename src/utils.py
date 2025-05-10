import numpy as np
import pandas as pd
import dill
import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.exception import CustomException

def save_object(file_path, obj):
    """
    This function saves the object to a file.
    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Object saved successfully")
    except Exception as e:
        raise CustomException(e, sys)   