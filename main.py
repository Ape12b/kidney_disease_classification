from cnnClassifier.utils import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline, STAGE_NAME as DATA_INGESTION_STAGE_NAME

try:
    logger.info(f">>>> {{DATA_INGESTION_STAGE_NAME}} has started<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>> {{DATA_INGESTION_STAGE_NAME}} has ended<<<<")
except Exception as e:
    logger.exception(e)
    raise e