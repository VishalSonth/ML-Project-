import os
import sys 
from src.exception import CustomException 
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split 
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifcats',"train.csv")
    test_data_path:str=os.path.join('artifcat',"test_csv")
    raw_data_path:str=os.path.join('artifcat',"data_csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component ")
        try:
            df=pd.read_csv('')
        except:
            pass
        

