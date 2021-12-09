import os
import yaml

from utils.utils import ROOT_DIR


class Variables:
    def __init__(self) -> None:
        with open(os.path.join(ROOT_DIR, "config", "config.yaml"), "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        # variables for logger
        logging_config = config["LOGGING"]
        self.log_level = logging_config["LEVEL"]
        self.log_format = logging_config["FORMAT"]

        # variables for csv
        csv_config = config["CSV"]
        self.train_data_path = csv_config["TRAIN_DATA_LOC"]
        self.drive_link = csv_config["DRIVE_LINK"]


var = Variables()
