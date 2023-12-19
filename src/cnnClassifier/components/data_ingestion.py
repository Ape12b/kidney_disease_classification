import os
import zipfile
import gdown
from cnnClassifier.utils import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download(self):
        '''
        Fetch data from G-Drive
        '''
        try:
            
            url = self.config.source_URL
            file_id = url.split("/")[-2]
            
            zip_file_path = self.config.local_data_file
            prefix_url = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix_url+file_id, zip_file_path)
            logger.info(f"Downloaded the file from {url} to {zip_file_path}")
        except Exception as e:
            raise e
    
    def extract_zip(self):
        """
        Extract zip files
        """
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file, 'r') as file:
            file.extractall(unzip_path)
            