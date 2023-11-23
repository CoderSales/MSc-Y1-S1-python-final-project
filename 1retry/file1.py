"""
calls file2.py
"""

# B01_Import_CSV_V1.py
import pandas as pd
#%% load file via static path
  
def load_df():
    tester=r'file2.py'
    return pd.read_csv(tester, sep=';',decimal=",", skipfooter=1300, engine='python')
