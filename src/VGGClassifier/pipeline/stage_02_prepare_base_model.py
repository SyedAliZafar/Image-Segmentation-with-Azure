from VGGClassifier.config.configuration import ConfigurationManager
from VGGClassifier.components.prepare_base_model import PrepareBaseModel
from VGGClassifier import logger


STAGE_NAME = 'Prepare Base Model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config= ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()

        prepare_base_model = PrepareBaseModel(prepare_base_model_config)

        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':

    try:
        logger.info("**************************************************")
        logger.info(f"******** stage {STAGE_NAME} started *************")

        obj= PrepareBaseModelTrainingPipeline()

        obj.main()
        logger.info(f"******** stage {STAGE_NAME} completed *************")

    except Exception as e:
        logger.exception(e)




