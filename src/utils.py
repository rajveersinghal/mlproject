import os
import sys
import pickle
import pandas as pd
from src.exception import CustomException
from src.logger import logging

# ----------------------------
# Save object (like a trained model)
# ----------------------------
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved successfully at {file_path}")

    except Exception as e:
        logging.error(f"Error saving object: {e}")
        raise CustomException(e, sys)

# ----------------------------
# Load object (like a saved model)
# ----------------------------
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            logging.info(f"Loading object from {file_path}")
            return pickle.load(file_obj)

    except Exception as e:
        logging.error(f"Error loading object: {e}")
        raise CustomException(e, sys)

# ----------------------------
# Read CSV data file
# ----------------------------
def read_csv_data(file_path):
    try:
        logging.info(f"Reading CSV file from {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully with shape: {df.shape}")
        return df

    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        raise CustomException(e, sys)

# ----------------------------
# Write DataFrame to CSV
# ----------------------------
def write_csv_data(df, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        df.to_csv(file_path, index=False)
        logging.info(f"DataFrame written successfully to {file_path}")

    except Exception as e:
        logging.error(f"Error writing DataFrame: {e}")
        raise CustomException(e, sys)
