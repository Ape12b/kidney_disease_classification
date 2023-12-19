from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.utils import logger
import os

STAGE_NAME = "Data ingestion stage"

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.data_ingestion_config()
        ingestor = DataIngestion(data_ingestion_config)
        ingestor.download()
        ingestor.extract_zip()
        os.remove(data_ingestion_config.local_data_file)
        logger.info(f"Ingestion pipeline succesful!")


if __name__ == '__main__':
    try:
        logger.info(f">>>> {{STAGE_NAME}} has started<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>> {{STAGE_NAME}} has ended<<<<")
    except Exception as e:
        raise e
        