from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys

from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_transformation import DataTransformation


if __name__ == "__main__":

    logging.info("This is a log message from app.py")

    try:

        data_ingestion = DataIngestion()

        train_data_path, test_data_path = (
            data_ingestion.initiate_data_ingestion()
        )

        data_transformation = DataTransformation()

        train_arr, test_arr, _ = (
            data_transformation.initiate_data_transformation(
                train_data_path,
                test_data_path
            )
        )

        logging.info("Data Transformation completed")

    except Exception as e:

        logging.info("An error occurred in app.py")

        raise CustomException(e, sys)