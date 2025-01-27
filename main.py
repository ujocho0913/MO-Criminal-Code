import os
import pandas as pd

from helper_functions import recent_date, import_mshp

# Set directories
home_path = os.getcwd()
cache_path = home_path+r'\CACHE'
helper_path = home_path+r'\HELPER_FILES'

# Import latest MSHP datafiles for MO Criminal Charge Code
charge_code_df, ncic_df, ncic_mod_df = import_mshp(cache_path+"\\"+recent_date(cache_path))


# Create dict_01: NCIC Categories and Code (ncic_df)
ncic_df = ncic_df[['NCIC Category','Category Description']].drop_duplicates(ignore_index=True)
# ncic_df.to_csv(helper_path+r'\NCIC Category.csv', encoding='utf-8', index=False) # one-time
ncic_dict = dict(zip(ncic_df['NCIC Category'], ncic_df['Category Description']))

"""
Charge Type: "F" Felony, "M" Misdemeanor, "I" Infraction, "L" Local Ordinance, "U" Unknown
* Charge Type: "A" (Admin?) and "U" account for 7 and 2 unique Charge Codes, respectively. They also all have Legacy Charge Codes. 
I suspect these aren't ever charged in Jackson County, so we will remove.
Classification: A, B, C, D, U (added Aug 2015; ACA)
"""

# Charge Code Severity and Class Hierarchy 
charge_hierarchy = charge_code_df[['Charge Type', 'Classification']].drop_duplicates(ignore_index=True).sort_values(by=['Charge Type', 'Classification'])
charge_hierarchy.to_csv(helper_path+r'\Charge Code Hierarchy.csv', encoding='utf-8', index=False)


dict = zip(df[col1],df[col2])
df2[new_col] = df2[col].map(dict)


# Re-order charge hierarchy

def charge_hierarchy(df):
    # Order by - Sev, Class, Count
    # Is re-arranged lead count = original lead count? If yes, 1; if no, 0 (what is original lead count Sev-Class?)


# Create MO Criminal Charge Code Glossary
# Organized by NCIC category, and listed by Statute code, short description, severity, and then class 