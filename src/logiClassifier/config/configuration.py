from logiClassifier.constants import *
from logiClassifier.utils import common as util
from logiClassifier.entity import entity_config as entity

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

        util.create_directories(config.root_dir)

        data_ingestion_config = entity.DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

        