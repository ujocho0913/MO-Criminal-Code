import pandas as pd
import os

# Script:   chargecode_cleaner.py
# Purpose:  Prepares helper files from MSHP Charge Code webpage to be used for dashboards and other data projects (https://www.mshp.dps.missouri.gov/CJ08Client/Home/ChargeCode)
# Author:   Joseph Cho, ujcho@jacksongov.org

# Set directories
home_path = os.getcwd()
cache_path = home_path+"\\Cache"

# Function name: recentDate
# Purpose: Prepare 
# Arguments: Path of Cache folder 
# Output: Folder path containing the most recent charge code data from MSHP 

def recentDate(path):

	#Initializes Blank List 
	allDates = []

	#Loops through files in the Cache folder
	for item in os.listdir(path):

        #Appends file names to list
		allDates.append(item)

	#Removes all the duplicates
	allDates = list(set(allDates))

	#Sorts the List without Duplicates
	allDates.sort()

	#Grabs the most recent file
	mostRecent = str(allDates[-1])

	#Returns that most recent file
	return mostRecent

# Function name: 
# Purpose: 
# Arguments: 
# Output: 

def cleanMSHP(path):
    #Import MSHP Columns Codebook.xlsx to add columns 
    mshp = "MSHP Columns Codebook.xlsx"
    #Loops through files in recent MSHP folder and imports as .CSV
    for item in os.listdir(path):
        if "ChargeCodeCSV" in item:
            cc_csv = pd.read_excel(mshp, sheet_name="Charge Code CSV")
            charge_code = pd.read_csv(path+"\\"+item, names=cc_csv['Column Names'], encoding='utf-8')
        elif "NCICCSV" in item:
            ncic_csv = pd.read_excel(mshp, sheet_name="NCIC CSV")
            ncic = pd.read_csv(path+"\\"+item, names=ncic_csv['Column Names'], encoding='utf-8')
        elif "NCICModifiersCSV" in item:
            ncicmod_csv = pd.read_excel(mshp, sheet_name="NCIC Modifiers CSV")
            ncic_mod = pd.read_csv(path+"\\"+item, names=ncicmod_csv['Column Names'], encoding='utf-8')
    
    return charge_code, ncic, ncic_mod

dict1, dict2, dict3 = cleanMSHP(cache_path+"\\"+recentDate(cache_path))

# Function name: 
# Purpose: 
# Arguments: 
# Output: 

def originalCrimeCategories():
    df = pd.read_csv("ChargeCodeCategories.csv", encoding='utf-8')
    category_dict = dict(zip(df['Ref. Charge Code'], df['Category']))
    dict1['Original Category'] = dict1['Charge Code'].map(category_dict)

    dict1['Statute Chapter'] = dict1['Statute'].str.lstrip("ORD").str[:3]
    print(dict1['Statute Chapter'].value_counts())

originalCrimeCategories()

dict1.to_csv("test.csv",index=False,encoding='utf-8')

# ChargeCodeCategories.CSV (Henry's categories)

# Crimes Against: (Person, Property, Society)

# Violent Crime 
# Property Crime 
# 
