# Update the components
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_ds(self):
        img_height = self.config.params_image_size[:-1][0]
        img_width = self.config.params_image_size[:-1][1]
        img_size = (img_height, img_width)
        
        self.train_ds = tf.keras.utils.image_dataset_from_directory(
                self.config.training_data,
                validation_split=0.2,
                subset="training",
                seed=123,
                image_size=img_size,
                batch_size=self.config.params_batch_size)
        
        self.val_ds = tf.keras.utils.image_dataset_from_directory(
                self.config.training_data,
                validation_split=0.2,
                subset="validation",
                seed=123,
                image_size=img_size,
                batch_size=self.config.params_batch_size)
        
        # Optimizing
        AUTOTUNE = tf.data.AUTOTUNE

        self.train_ds = self.train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        self.val_ds = self.val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        
        
        # Normalizing
        normalization_layer = tf.keras.layers.Rescaling(1./255)
        
        self.train_ds = self.train_ds.map(lambda x, y: (normalization_layer(x), y))
        self.val_ds = self.val_ds.map(lambda x, y: (normalization_layer(x), y))
        
        # Augmenting train dataset
        data_augmentation = tf.keras.Sequential(
            [
                tf.keras.layers.RandomFlip("horizontal",
                                input_shape=(img_height,
                                            img_width,
                                            3)),
                tf.keras.layers.RandomRotation(0.1),
                tf.keras.layers.RandomZoom(0.1),
            ]
            )
        self.train_ds = self.train_ds.map(lambda x, y: (data_augmentation(x), y))             
        
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
    
    def train(self):
        
        self.model.summary()
        self.model.fit(
            self.train_ds,
            epochs=self.config.params_epochs,
            validation_data=self.val_ds
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )