import os
import pandas as pd

from helper_functions import recent_date, import_mshp, create_dict

# Set directories 
home_path = os.getcwd()
cache_path = home_path+r'\CACHE'
helper_path = home_path+r'\HELPER_FILES'

# Import latest MSHP datafiles for MO Criminal Charge Code
charge_code_df, ncic_df, ncic_mod_df = import_mshp(cache_path+"\\"+recent_date(cache_path))


# Create dict_01: NCIC Categories and Code (ncic_df)
ncic_df = ncic_df[['NCIC Category','Category Description']]


dict = zip(df[col1],df[col2])
df2[new_col] = df2[col].map(dict)


# Re-order charge hierarchy

def charge_hierarchy(df):
    # Order by - Sev, Class, Count
    # Is re-arranged lead count = original lead count? If yes, 1; if no, 0 (what is original lead count Sev-Class?)