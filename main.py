from VGGClassifier import logger
from VGGClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from VGGClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from VGGClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from VGGClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


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

    model_prepare= PrepareBaseModelTrainingPipeline()

    model_prepare.main()
    logger.info(f"******** stage {STAGE_NAME} completed *************")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:

        logger.info("**************************************************")
        logger.info(f"******** stage {STAGE_NAME} started *************")

        model_trainer= ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f"******** stage {STAGE_NAME} completed *************")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation"
try:

        logger.info("**************************************************")
        logger.info(f"******** stage {STAGE_NAME} started *************")

        model_evaluation= EvaluationPipeline()
        model_evaluation.main()
        logger.info(f"******** stage {STAGE_NAME} completed *************")

except Exception as e:
    logger.exception(e)
    raise e