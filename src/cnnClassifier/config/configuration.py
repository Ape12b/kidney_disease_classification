import os
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories# Placeholder content
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, ModelTrainingConfig, EvaluationConfig

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
    
    def prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config =self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_model_path,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            
        )
        
        return base_model_config
    
    def model_training_config(self) -> ModelTrainingConfig:
        training =self.config.model_training
        params = self.params
        create_directories([training.root_dir])
        
        training_config = ModelTrainingConfig(
            root_dir=training.root_dir,
            trained_model_path=training.trained_model_path,
            updated_base_model_path=self.config.prepare_base_model.updated_model_path,
            training_data=os.path.join(self.config.data_ingestion.unzip_dir, 'kidney-ct-scan-image'),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        
        return training_config
    
    def model_evaluation_config(self) -> EvaluationConfig:
        training =self.config.model_training
        params = self.params
        create_directories([training.root_dir])
        
        evaluation_config = EvaluationConfig(
            path_of_model=self.config.model_training.trained_model_path,
            training_data=os.path.join(self.config.data_ingestion.unzip_dir, "kidney-ct-scan-image"),
            all_params=self.params,
            mlflow_uri="https://dagshub.com/apri4u/kidney_disease_classification.mlflow",
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
            
        )
        
        return evaluation_config