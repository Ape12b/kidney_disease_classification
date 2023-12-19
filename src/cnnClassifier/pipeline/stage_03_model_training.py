from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import ModelTraining
from cnnClassifier.utils import logger
import os

STAGE_NAME = "Model training stage"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_training_config = config.model_training_config()
        model = ModelTraining(model_training_config)
        model.get_base_model()
        model.train_valid_ds()
        model.train()
        logger.info(f"Training pipeline succesful!")

if __name__ == '__main__':
    try:
        logger.info(f">>>> {{STAGE_NAME}} has started<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> {{STAGE_NAME}} has ended<<<<")
    except Exception as e:
        raise e