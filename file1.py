"""
calls file2.py
"""

# B01_Import_CSV_V1.py
import pandas as pd
#%% load file via static path
  
def load_df():
    tester=r'C:\user\steph\OneDrive\Documents\45-semester-1\module-language-engineering\10-week-10-on\1-py-final-proj\MSc-Y1-S1-python-final-project\file2.py'
    return pd.read_csv(tester, sep=';',decimal=",", skipfooter=1300, engine='python')
