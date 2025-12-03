import sys
import os
import json
from os import path

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
base_dir = os.path.dirname(os.path.dirname(script_dir))
folder_name = os.path.basename(script_dir)

print(base_dir+"/KBUtilLib/src")
sys.path = [base_dir+"/KBUtilLib/src",base_dir+"/cobrakbase",base_dir+"/ModelSEEDpy/"] + sys.path

# Import utilities with error handling
from kbutillib import NotebookUtils

import hashlib
import pandas as pd
from modelseedpy import AnnotationOntology, MSPackageManager, MSMedia, MSModelUtil, MSBuilder, MSATPCorrection, MSGapfill, MSGrowthPhenotype, MSGrowthPhenotypes, ModelSEEDBiochem, MSExpression

class NotebookUtil(NotebookUtils):
    def __init__(self,**kwargs):
        super().__init__(
            notebook_folder=script_dir,
            name="PangenomeAnalysis",
            user="chenry",
            retries=5,
            proxy_port=None,
            **kwargs
        )

    # PLACE ALL UTILITY FUNCTIONS NEEDED FOR NOTEBOOKS HERE
    #
    # This project focuses on pangenome analyses using:
    # - BERDL: Bacterial Evolution and Redundancy Detection Library
    # - PLM: Protein Language Models
    # - SKANI: Fast and accurate ANI calculator for genomes
    # - Other pangenome analysis tools

# Initialize the NotebookUtil instance
util = NotebookUtil()
