#Melt emissions_df while keeping id_vars as fixed values, and create dropdown for each year as well as another column for its corresponding indicator value
Emissions_df = Emissions_df.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name='Year', value_name="Indicator Value")

#Show top 10 rows of Emissions_df to view updated df
Emissions_df.head(10)
