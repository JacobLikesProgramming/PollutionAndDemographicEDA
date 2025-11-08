#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 00:04:14 2025

@author: jacobsilva
"""

WDI_ids = pd.read_csv("./files/WDI_csv/WDISeries.csv")
print(WDI_ids.columns)
WDI_ids.head()

#New dataframe that includes rows where the topic key in WDI_ids dataframe includes the keyword 'Environment'
enviro_df = WDI_ids[WDI_ids['Topic'].str.contains('Environment')]

#Create new column subtopic where it grabs the string after the : ()
enviro_df['Subtopic'] = enviro_df['Topic'].str.split(': ').str.get(1)

#Create list of unique subtopics to be printed
subtopic_listing = enviro_df['Subtopic'].unique()

#Print each iteration of subtopic in list
for sub in subtopic_listing:
    print(sub)