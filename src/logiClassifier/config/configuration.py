from logiClassifier.constants import *
from logiClassifier.utils import common as util
from logiClassifier.entity import entity_config as entity
import os

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
        
        self.config = util.read_yaml(config_filepath)
        self.params = util.read_yaml(params_filepath)

        util.create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> entity.DataIngestionConfig:
        config = self.config.data_ingestion

        util.create_directories([config.root_dir])

        data_ingestion_config = entity.DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_prepare_base_mode_config(self) -> entity.PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        util.create_directories([config.root_dir])

        prepare_base_model_config = entity.PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config

    
    def get_training_config(self) -> entity.TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "KIDNEY-DISEASE_DATASET-2")
        util.create_directories([
            Path(training.root_dir)
        ])

        training_config = entity.TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    

    def get_evaluation_config(self) -> entity.EvaluationConfig:
        eval_config = entity.EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/KIDNEY-DISEASE_DATASET-2",
            mlflow_uri="https://dagshub.com/princvenu-code/Kidney-Disease-Classification.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config