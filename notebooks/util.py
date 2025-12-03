import sys
import os, time
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
from kbutillib import NotebookUtils, KBPLMUtils

import hashlib
import pandas as pd

class NotebookUtil(NotebookUtils,KBPLMUtils):
    def __init__(self,**kwargs):
        super().__init__(
            notebook_folder=script_dir,
            name="TNseqPropagationAnalysis",
            user="chenry",
            retries=5,
            proxy_port=None,
            **kwargs
        )
        self.spark = None 

    def run_query(self,query):
        w0, u0, s0, *_ = time.time(), *os.times()[:2]
        df = self.spark.sql(query)
        row_count = df.count()
        w1, u1, s1, *_ = time.time(), *os.times()[:2]
        print(f"wall={w1-w0:.2f}s user={u1-u0:.2f}s sys={s1-s0:.2f}s")
        return df

    def save_dataframe(self, name, df, format='csv'):
        """
        Save a pandas DataFrame to nboutput directory.

        Args:
            name: Name for the output file (without extension)
            df: pandas DataFrame to save
            format: Output format ('csv', 'tsv', 'excel')
        """
        output_dir = os.path.join(self.notebook_folder, 'nboutput')
        os.makedirs(output_dir, exist_ok=True)

        if format == 'csv':
            filepath = os.path.join(output_dir, f"{name}.csv")
            df.to_csv(filepath, index=False)
        elif format == 'tsv':
            filepath = os.path.join(output_dir, f"{name}.tsv")
            df.to_csv(filepath, sep='\t', index=False)
        elif format == 'excel':
            filepath = os.path.join(output_dir, f"{name}.xlsx")
            df.to_excel(filepath, index=False)
        else:
            raise ValueError(f"Unsupported format: {format}")

        print(f"Saved DataFrame to {filepath}")
        return filepath

    def load_dataframe(self, name, format='csv'):
        """
        Load a pandas DataFrame from nboutput directory.

        Args:
            name: Name of the file (without extension)
            format: Input format ('csv', 'tsv', 'excel')

        Returns:
            pandas DataFrame
        """
        output_dir = os.path.join(self.notebook_folder, 'nboutput')

        if format == 'csv':
            filepath = os.path.join(output_dir, f"{name}.csv")
            df = pd.read_csv(filepath)
        elif format == 'tsv':
            filepath = os.path.join(output_dir, f"{name}.tsv")
            df = pd.read_csv(filepath, sep='\t')
        elif format == 'excel':
            filepath = os.path.join(output_dir, f"{name}.xlsx")
            df = pd.read_excel(filepath)
        else:
            raise ValueError(f"Unsupported format: {format}")

        print(f"Loaded DataFrame from {filepath}")
        return df

# Initialize the NotebookUtil instance
util = NotebookUtil()
