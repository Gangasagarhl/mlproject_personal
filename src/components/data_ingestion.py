import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig: 
    train_data_path:str =  os.path.join('artifacts','train.csv')
    test_data_path :str =  os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')
    """
    Defining the path where we need to store the train test and data, 
    
    """
    
    
"""
When we have only the variables to be defined only 
@dataclass is enough.
When we have other than the dataclass, we can use the __init__ function shall be defined over the @dataclass
"""
class DataIngestion:
    def __init__(self): 
        #this is where we are initliaising the object of the ingestion_config, which is later used as the object variable of the class
        self.ingestion_config =  DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Enterede data")
        
        """
        Later  this shall be used to get the data frim mongo client
        and also from the server.
        """
        try:
            df = pd.read_csv('../notebook/data/stud.csv')
            #the above can be read using the various sources like mong db
            
            logging.info("Read the dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info("directory createcd")
            df.to_csv(self.ingestion_config.raw_data_path,index=False,  header=True)
            logging.info("csv stored in the directory")
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header=  True)
            logging.info("Ingestion of the data is done")
            
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
                )
            
        except Exception as e:
            raise CustomException(e,sys)
            
        
if __name__ =="__main__":
    ob= DataIngestion()
    ob.initiate_data_ingestion()