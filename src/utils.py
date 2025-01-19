#for calling or loading the datset
#for saving the model on the cloud
#then directly linking/calling into the components
#It has Some common Functionalities that can be used throughout the function
import os
import sys
import dill

import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)