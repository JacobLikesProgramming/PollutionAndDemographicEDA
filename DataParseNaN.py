#Remove all rows where the year is unnamed 64
Emissions_df.drop(Emissions_df[Emissions_df['Year'] == "Unnamed: 64"].index, inplace=True)

#The columns that are to be subsetted
subsetted_columns = ['Country Name', 'Indicator Code']

#Create empty list to store subdataframes that have been interpolated
interpolated_dfs = []

#Loop through each individual country's indicator
for (country, indicator), group_df in Emissions_df.groupby(subsetted_columns):
    
    #Interpolate Indicator value and append the interpolated dataframe to the list
    group_df['Indicator Value'] = group_df['Indicator Value'].interpolate()
    interpolated_dfs.append(group_df)
    
#Concatenate interpolated dataframe
Emissions_df = pd.concat(interpolated_dfs)

#Drop all rows where there are any NaN values left over
Emissions_df.dropna(subset=['Indicator Value'], inplace=True)
