# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:57:19 2020

@author: Syamanthaka
"""

#!/usr/bin/env python

## Necessary imports
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter
import yaml
import os

def excel_writer(path, df_to_write):
    writer = pd.ExcelWriter(path, engine ='xlsxwriter')
    df_to_write.to_excel(writer,'Sheet1',index=False)
    writer.save()
    
    return

def path_parser(path):
    head, tail = os.path.split(path)    
    new_path = os.path.join(head, 'historic_tube_data.xlsx')
   
    return(new_path)

def one_time(bulk_file_path):
    print("Hello and welcome to the one time process")
    print("You entered ", bulk_file_path)
    
    try:
        bulk_df = pd.read_excel(bulk_file_path, sheet_name="Sheet1")
        new_df = process_info(bulk_df)
        print(new_df)
        
        new_path = path_parser(bulk_file_path)
        
        excel_writer(new_path, new_df)
        print("File has been saved at ", new_path)
    except FileNotFoundError:
        print("Please enter valid file")
    
    return(1)
    
def monthly_update(bulk_file_path, monthly_file):
    print("Going to process the records for this month")
    print("Your bulk file is located at ", bulk_file_path)
    print("Your new file is at ", monthly_file)
    
    try:
        monthly_df = pd.read_excel(monthly_file, sheet_name="Sheet1")
        new_monthly_df = process_info(monthly_df)
        
        historic_df = pd.read_excel(bulk_file_path, sheet_name="Sheet1")
        historic_df_new = historic_df.append(new_monthly_df, ignore_index=True, sort=False)
        
        print("File is ready to be saved. Overwriting old historic file")
        excel_writer(bulk_file_path, historic_df_new)
         
          
    except FileNotFoundError:
        print("Please enter valid file")   
   
    return(1)

def process_info(input_df):
    print("Processing..... ")
        
    config_yaml = open("project_config.yml", 'r')
    config_params = yaml.load(config_yaml, Loader=yaml.FullLoader)
    
    ## Iterating through the config parameters and selecting from the df only the params as required by the project
    for k, v in config_params.items():
        if k in input_df.columns:
            input_df = input_df[input_df[k].isin(v)]
            
    
    ## Aggregate by Market, Year and month. So for 17 rows per year per month for each of the 17 markets.
    ## We are interested in IB and Consumption aggregation. 
    ## Ignore System code as it is getting summed as a number
    input_df = input_df.groupby(['Market', 'Year', 'Month']).sum()
    
    ## Calculate failure rate as Consumption/IB
    input_df['Failure_rate'] = input_df['Consumption'] / input_df['IB']
    
    ## Reset index for preparing to write to excel
    input_df.reset_index(level=input_df.index.names, inplace=True)
    
    return(input_df)
    
def main():
    #Ask if this is one time for a big file or new month repeat
    
    yes = set(['yes', 'y'])
    no = set(['no', 'n'])
    prompt = '>'
    
    print("Hello, let's process the Tube IB data\n")
    print("Are you doing a one time batch process? ")
    process_type = input(prompt)
    
    if process_type in yes:
        print("Kindly enter the path of the file you want to process (eg. C:/foo/bar/baz.xlsx) ")
        one_time_file = input(prompt)
        print("Calling process function")
        one_time(one_time_file)
    elif process_type in no:
        print("Kindly enter path of already existing historical file (eg. C:/foo/bar/baz.xlsx) ")
        history_file = input(prompt)
        print("Now kindly enter path of the file you want to process (eg. C:/foo/bar/this_month.xlsx) ")
        monthly_file = input(prompt)
        print("Processing..... ")
        monthly_update(history_file, monthly_file)
    else:
        print("please enter a valid input")
        main()
        
main()
