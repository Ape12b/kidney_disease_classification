from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories# Placeholder content
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_path = PARAMS_FILE_PATH,
                 ):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        
        create_directories([self.config.artifacts_root])
    
    def data_ingestion_config(self) -> DataIngestionConfig:
        config =self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
        