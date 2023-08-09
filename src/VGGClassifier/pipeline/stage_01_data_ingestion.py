from VGGClassifier.config.configuration import ConfigurationManager
from VGGClassifier.components.data_ingestion import DataIngestion
from VGGClassifier import logger



class DataIngestionTrainingPipeline():  
    def __init__(self):
        pass

    # Need to explicitly call this method in order to configure the data ingestion pipeline
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        print("configuration loaded successfully", data_ingestion_config)


        data_ingestion = DataIngestion(config=data_ingestion_config)
        print("Data ingestion files", data_ingestion)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":

    try:
        logger.info(f">>>stage {STAGE_NAME} started<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed<<<")

    except Exception as e:
        logger.exception(e)
        raise e