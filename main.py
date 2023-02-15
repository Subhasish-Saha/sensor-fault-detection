
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline

#from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

if __name__ == "__main__":
    try:
        print('Pipeline started')
        traning_pipeline = TrainPipeline()
        traning_pipeline.run_pipeline()
        print('Pipeline stopped')
    except Exception as e:
        print(e)
        logging.exception(e)