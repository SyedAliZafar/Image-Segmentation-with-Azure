from VGGClassifier.config.configuration import ConfigurationManager
from VGGClassifier.components.evaluation import Evaluation
from VGGClassifier import logger


STAGE_NAME = 'Evaluation'
class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f'********************************')
        logger.info(f'>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<')
        obj= EvaluationPipeline()
        obj.main()
    except Exception as e:
        raise e

