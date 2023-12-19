import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def download(self):
        '''
        Fetch data from G-Drive
        '''
        self.model = tf.keras.applications.VGG16(
            include_top=self.config.params_include_top,
            weights=self.config.params_weights,
            input_shape=self.config.params_image_size
        )
        self.save_model(path=self.config.base_model_path, model=self.model)
    
    def update(self):
        self.updated_model=self._update_model(freeze_all=True,
                                            freeze_till=0,
                                            model=self.model,
                                            classes=self.config.params_classes,
                                            learning_rate=self.config.params_learning_rate)
        self.save_model(path=self.config.updated_base_model_path, model=self.updated_model)
    
    @staticmethod
    def _update_model(freeze_all: bool, 
                      freeze_till:int,
                      model:tf.keras.Model,
                      classes:int,
                      learning_rate:float):
        if freeze_all:
            model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:freeze_till]:
                layer.trainable = True
        
        flatten_in=tf.keras.layers.Flatten()(model.output)
        predictions=tf.keras.layers.Dense(
            activation="softmax",
            units=classes
        )(flatten_in)
        
        updated_model = tf.keras.models.Model(
            inputs = flatten_in,
            outputs = predictions
        )
        
        updated_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )
        
        updated_model.summary()
        return updated_model
        
    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)