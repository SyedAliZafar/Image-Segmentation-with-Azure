## Custom Logging 

import os 
import sys
import logging

# 

logging_str= "[%(asctime)s- %(levelname)s]- %(module)s - %(message)s"

log_dir= "logs"
log_filepath= os.path.join(log_dir, "running.log")

os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level=logging.INFO, 
    format=logging_str, 
    handlers= [
        
            logging.StreamHandler(sys.stdout), 
               
            logging.FileHandler(log_filepath) # printing log insider the terminal
            ]


    
    )


logger= logging.getLogger("VGG Classifier Logger")
    