from cnnClassifier.utils import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline, STAGE_NAME as DATA_INGESTION_STAGE_NAME

try:
    logger.info(f">>>> {[DATA_INGESTION_STAGE_NAME]} has started<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>> {[DATA_INGESTION_STAGE_NAME]} has ended<<<<")
except Exception as e:
    logger.exception(e)
    raise e

from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline, STAGE_NAME as BASE_MODEL_STAGE_NAME

try:
    logger.info(f">>>> {[BASE_MODEL_STAGE_NAME]} has started<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>> {[BASE_MODEL_STAGE_NAME]} has ended<<<<")
except Exception as e:
    logger.exception(e)
    raise e

from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline, STAGE_NAME as MODEL_TRAINING_STAGE_NAME

try:
    logger.info(f">>>> {[MODEL_TRAINING_STAGE_NAME]} has started<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> {[MODEL_TRAINING_STAGE_NAME]} has ended<<<<")
except Exception as e:
    logger.exception(e)
    raise e

from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline, STAGE_NAME as MODEL_EVAL_STAGE_NAME
try:
    logger.info(f">>>> {[MODEL_EVAL_STAGE_NAME]} has started<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>> {[MODEL_EVAL_STAGE_NAME]} has ended<<<<")
except Exception as e:
    raise e