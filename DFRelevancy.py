#Create list of relevant subtopics, as of now we are only interested in emissions and add to new subdataframe only rows where the subtopic is in the relevant subtopics list 
relevantSubtopics = ["Emissions"]
Emissions_df_seriesC1 = enviro_df[enviro_df['Subtopic'].isin(relevantSubtopics)]

#Grab the series code from the series_c_emissions df and compute a listing of all series codes and if a series code in the list matches the value of series code in WDI_data df, copy row
series_c_emissions = Emissions_df_seriesC1["Series Code"].unique()
Emissions_df = WDI_data[WDI_data['Indicator Code'].isin(series_c_emissions)]

#Print how many emission indicators (Length of the emissions dataframe) there are in the study
print(f"There are {len(Emissions_df)} emissions indicators in the study.")
