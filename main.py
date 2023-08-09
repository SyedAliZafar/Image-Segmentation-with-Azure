from VGGClassifier import logger
from VGGClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from VGGClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


logger.info("Welcom to the VGG Classifier logging!")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info("**************************************************")
    logger.info(f"******** stage {STAGE_NAME} started *************")

    obj= PrepareBaseModelTrainingPipeline()

    obj.main()
    logger.info(f"******** stage {STAGE_NAME} completed *************")

except Exception as e:
    logger.exception(e)