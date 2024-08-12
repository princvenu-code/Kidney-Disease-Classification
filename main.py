from src.logiClassifier import logger

from logiClassifier import logger
from logiClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from logiClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion_pipeline = DataIngestionPipeline()
    # data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} comleted <<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e