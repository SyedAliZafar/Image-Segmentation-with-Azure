import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define project name

project_name = "VGG Classifier"

# Specify list of folders need to be created
# Constructor files
list_of_files = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py", 
        f"src/{project_name}/components/__init__.py", 
        f"src/{project_name}/utils__init__.py",  
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",  
        "dvc.ymal",
        "params.yaml",
        "requirements.txt",
        "setup.py",
        "reserach/trials.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")


    # Check whether the file exists or not and whether the existing file is empty or not

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty {filepath}")

    else:
        logging.info(f"File {filepath} already exists")
