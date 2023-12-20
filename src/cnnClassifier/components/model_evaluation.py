from pathlib import Path
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json
import mlflow
from urllib.parse import urlparse
import tensorflow as tf


class ModelEvaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    
    def _test_ds(self):
        img_height = self.config.params_image_size[:-1][0]
        img_width = self.config.params_image_size[:-1][1]
        img_size = (img_height, img_width)
        
        self.test_ds = tf.keras.utils.image_dataset_from_directory(
                self.config.training_data,
                validation_split=0.3,
                subset="validation",
                seed=123,
                image_size=img_size,
                batch_size=self.config.params_batch_size)
        
        # Optimizing
        AUTOTUNE = tf.data.AUTOTUNE

        self.test_ds = self.test_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        
        # Normalizing
        normalization_layer = tf.keras.layers.Rescaling(1./255)
        
        self.test_ds = self.test_ds.map(lambda x, y: (normalization_layer(x), y))          
        
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._test_ds()
        self.score = self.model.evaluate(self.test_ds)
    
    def save_score(self):
        scores = {"loss": self.score[0],
                  "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
    
    def log_onto_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0],
                  "accuracy": self.score[1]})
            
            # Model registry won't work with filestorage
            if tracking_uri_type_store != "file":
                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(
                    self.model, "model", registered_model_name="VGG16_Model"
                )
            else:
                mlflow.sklearn.log_model(self.model, "model")