from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.base_model_preparation import PrepareBaseModel
from cnnClassifier.utils import logger
import os

STAGE_NAME = "Prepare base model stage"

class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        base_model_config = config.prepare_base_model_config()
        base_model = PrepareBaseModel(base_model_config)
        base_model.download()
        base_model.update()
        logger.info(f"Base model pipeline succesful!")

if __name__ == '__main__':
    try:
        logger.info(f">>>> {{STAGE_NAME}} has started<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>> {{STAGE_NAME}} has ended<<<<")
    except Exception as e:
        raise e