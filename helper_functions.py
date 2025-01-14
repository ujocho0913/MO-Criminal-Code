import os 
import pandas as pd

# Set directories 
home_path = os.getcwd()
cache_path = home_path+r'\CACHE'
helper_path = home_path+r'\HELPER_FILES'

# Define function: recent_date()
def recent_date(path):
    cache_dates = []
    for item in os.listdir(path):
        cache_dates.append(item)

    cache_dates = list(set(cache_dates))
    cache_dates.sort()
    new_date = str(cache_dates[-1])

    return new_date

# Define function: import_mshp()
def import_mshp(path):
    mshp = helper_path+r'\MSHP Columns Codebook.xlsx'
    for item in os.listdir(path):
        if "ChargeCodeCSV" in item:
            cc_csv = pd.read_excel(mshp, sheet_name="Charge Code CSV")
            charge_code = pd.read_csv(path+"\\"+item, names=cc_csv['Column Names'], encoding='utf-8')
        if "NCICCSV" in item:
            ncic_csv = pd.read_excel(mshp, sheet_name="NCIC CSV")
            ncic = pd.read_csv(path+"\\"+item, names=ncic_csv['Column Names'], encoding='utf-8')
        if "NCICModifiersCSV" in item:
            ncicmod_csv = pd.read_excel(mshp, sheet_name="NCIC Modifiers CSV")
            ncic_mod = pd.read_csv(path+"\\"+item, names=ncicmod_csv['Column Names'], encoding='utf-8')

    return charge_code, ncic, ncic_mod

# Define function: create_dict()
def create_dict(df, col1, col2):
    dict = zip(df[col1],df[col2])
    return dict
