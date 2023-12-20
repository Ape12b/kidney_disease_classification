from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import ModelEvaluation
from cnnClassifier.utils import logger
import os

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.model_evaluation_config()
        model = ModelEvaluation(model_evaluation_config)
        model.evaluation()
        model.save_score()
        model.log_onto_mlflow()
        logger.info(f"Evaluation pipeline succesful!")

if __name__ == '__main__':
    try:
        logger.info(f">>>> {{STAGE_NAME}} has started<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>> {{STAGE_NAME}} has ended<<<<")
    except Exception as e:
        raise e