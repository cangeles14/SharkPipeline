#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:34:03 2020

@author: christopher
"""
# Imports/libraries needed
import pandas as pd
import re

def read_dataset(dataset_path):
    # Function that reads the data from the filepath entered
    df = pd.read_csv(dataset_path, engine='python')
    return df

def drop_columns(df):
    # Function to drop unrelevant columns from dataset
    
    # Strip columns of spacing
    
    for col in df.columns:
        df.rename(columns={col: col.strip(' ')}, inplace = True)
    # Make everything lowercase and change all NaN values to NA
    df.fillna('NA', inplace=True)   
    # Drop columns
    cols_to_drop = ['Date', 'Area', 'Location', 'Name', 'Sex',
                    'Age', 'Time', 'Investigator or Source', 'pdf',
                    'href formula', 'href', 'Case Number.1', 'Case Number.2',
                    'original order', 'Unnamed: 22', 'Unnamed: 23']
    # Run drop function on list of cols to drop
    df.drop(cols_to_drop, axis=1, inplace =True)
    
    return df

def drop_rows(df):
    # Function to remove unwanted rows
    # Make a df of all rows where year is less than 1980
    rows_to_drop = df[df.Year < 1980]
    
    #Drop these rows
    df.drop(rows_to_drop, axis=0, inplace=True)
    
    return df

def remove_nan(df):
    # Create a function to remove all NaN values
    
    return df


def clean_activity(df):
    # Function to clean activity column, creating organized categories  
    # Make all values lowercase to work with
    df.Activity = df.Activity.str.lower()
    
    # Create a dict with multiple changes to make
    # Obtained by looking at top 10 most frequent activity
    # df.Activity.value_counts().head(15)
    activity_change_list= {'surfing':['surf','boarding'],\
                           'swimming':['swim', 'wading','standing'],\
                           'fishing':['fish','spearfishing'],\
                           'diving':['scuba diving','snorkeling']}
    
    # Function to replace value according to dict keys/value
    for key,values in activity_change_list.items():
        for value in values:
            df.loc[df.Activity.str.contains(value),'Activity'] = key
         
    # Change all to other     
    df.loc[(~df.Activity.isin(activity_change_list))&(df.Activity!='NA'),'Activity'] = 'other'
    
    return df
    
    