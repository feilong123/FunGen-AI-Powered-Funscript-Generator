import json
import os
import time

from script_generator.constants import OUTPUT_PATH
from script_generator.debug.logger import logger


def write_json_to_file(file_path, data):
    """
    Write data to a JSON file, always overwriting if it exists.
    :param file_path: The path to the output file.
    :param data: The data to write.
    """
    logger.info(f"Exporting data...")
    export_start = time.time()

    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

        # Write the data to the file (overwrites if it exists)
    with open(file_path, 'w') as f:
        json.dump(data, f)
    export_end = time.time()
    logger.info(f"Done in {export_end - export_start} seconds.")

def load_json_from_file(file_path):
    """
    Load YOLO data from a JSON file.
    :param file_path: Path to the JSON file.
    :return: The loaded data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not load json from file as it does not exist: {file_path}")

    with open(file_path, 'r') as f:
        data = json.load(f)
        logger.info(f"Loaded data from {file_path}, length: {len(data)}")
    return data

def get_output_file_path(video_path, suffix, add_spoiler_prefix=False):
    """"
    Get the OUTPUT_PATH filename for a specific suffix (e.g. _raw_yolo.json)
    """
    filename_base = os.path.basename(video_path)[:-4]
    filename = f"{'SPOILER_' if add_spoiler_prefix else ''}{filename_base}{suffix}"
    path = os.path.join(OUTPUT_PATH, filename_base, filename)
    return path, filename

def check_create_output_folder(video_path):
    output_dir, _ = get_output_file_path(video_path, "")
    directory = os.path.dirname(output_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)