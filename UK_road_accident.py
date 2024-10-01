## IMPORTING THE REQUIRED LIBRARY

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# LOADING THE DATA FROM SOURCE

df1 = pd.read_csv('Accident_Information.csv')
df2 = pd.read_csv('Vehicle_Information.csv', delimiter =',', encoding='ISO-8859-1')

df1.info()

df1.head(5)
df2.head(5)

# LINKING THE TWO DATASETS

df_merged = pd.merge(df1, df2, on='Accident_Index', how='inner')

pd.set_option('display.max_columns', None)

df_merged.head(5)
df_merged.tail(5)

df_merged = df_merged.drop(['2nd_Road_Class', '2nd_Road_Number', 'Year_x', 'Driver_IMD_Decile', 'Engine_Capacity_.CC.'], axis = 1)

df_merged = df_merged.drop(['1st_Road_Class', '1st_Road_Number'], axis = 1)

df_merged.info()
df_merged.dtypes

df_merged.head(5)
df_merged['Accident_Severity'].unique()

# CHECKING THE UNIQUE VALUES IN THE COLUMNS
column_names = df_merged.columns # To extract the column names
column_names 
column_names_list = column_names.tolist() # to convert the column names to lists
column_names_list

for column in column_names_list:
    if column in df_merged.columns: # check if the column exists in the df_merged
        unique_values = df_merged[column].unique() # to extract the unique values
        print(f"Unique values in column '{column}':")
        print (unique_values)
    else:
        print(f"Column '{column}' does not exist in df_merged")

# SPECIFYING THE NEEDED COLUMNS TO BE SELECTED FROM DF_MERGED TABLE

selected_columns = ['Accident_Index', 'Year_y', 'Date', 'Day_of_Week', 'Accident_Severity', 'Number_of_Casualties','Number_of_Vehicles', 'Carriageway_Hazards',
                    'Junction_Control', 'Junction_Detail', 'Light_Conditions', 'Local_Authority_(Highway)',
                    'Pedestrian_Crossing-Human_Control', 'Pedestrian_Crossing-Physical_Facilities',
                    'Police_Force', 'Road_Surface_Conditions', 'Road_Type','Special_Conditions_at_Site', 
                    'Speed_limit', 'Time', 'Urban_or_Rural_Area', 'Weather_Conditions', 'InScotland',
                    'Age_Band_of_Driver', 'Age_of_Vehicle', 'Sex_of_Driver', 'Propulsion_Code',
                    'Skidding_and_Overturning', 'Towing_and_Articulation', 'Vehicle_Type',
                    'Was_Vehicle_Left_Hand_Drive', 'Journey_Purpose_of_Driver', 'Latitude', 'Longitude']

df_selected = df_merged[selected_columns]

df_selected.head(5)

# CREATE A COLUMN 'MONTH' FROM COLUMN 'DATE'

df_selected['Date'] = pd.to_datetime(df_selected['Date'])

df_selected['Month'] = df_selected['Date'].dt.month

df_selected.shape #(2058408, 35)

month_mapping = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

df_selected['Month_Name'] = df_selected['Month'].map(month_mapping) # CREATING A COLUMN FOR MONTH NAME

df_selected.head(5)

# TREATING NULL VALUES IN THE DATA

df_selected.isnull().sum().sort_values(ascending=False)

df_selected = df_selected.drop(['Carriageway_Hazards', 'Special_Conditions_at_Site', 'Age_of_Vehicle'], axis=1)

df_selected.drop(['Skidding_and_Overturning'], axis=1, inplace=True)

df_selected['Pedestrian_Crossing-Physical_Facilities'].unique()

# EXPLORATORY DATA ANALYSIS - ACCIDENT TREND ANALYSIS
# First ordered the data by month
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df_selected['Month_Name'] = pd.Categorical(df_selected['Month_Name'], categories = months_order, ordered= True)

# Group by year and month
monthly_trends = df_selected.groupby(['Year_y', 'Month_Name'])['Number_of_Casualties'].sum().reset_index()
monthly_trends

# Pivot the data for easy plotting

monthly_trends_pivot = monthly_trends.pivot(index='Month_Name', columns='Year_y', values='Number_of_Casualties')
monthly_trends_pivot

# Plotting the accident trends over the years

plt.figure(figsize=(15, 10))
sns.heatmap(monthly_trends_pivot, annot=True, fmt='g', cmap='YlGnBu')
plt.title('Accident Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Month')

plt.figure(figsize=(12,8))
for year in monthly_trends_pivot.columns:
    plt.plot(monthly_trends_pivot.index, monthly_trends_pivot[year], marker='o', label= year)
plt.title('Accident Casualities by Month (2005 - 2016)')
plt.xlabel('Month')
plt.ylabel('Number of Casualties')
plt.xticks(rotation = 45)
plt.legend(title = 'Year')
plt.tight_layout()
plt.show()

# Average number of casualties per year

average_annual_casualties = monthly_trends.groupby('Year_y')['Number_of_Casualties'].mean().reset_index()
average_annual_casualties

# Plotting this series

plt.figure(figsize=(10, 6))
sns.lineplot(x='Year_y', y='Number_of_Casualties', data=average_annual_casualties, color = 'red')
plt.title('Average Number of Casualties per Year (2005 - 2016)')
plt.xlabel('Year')
plt.ylabel('Average Number of Casualties')

# Total number of casualties per year

total_annual_casualties = monthly_trends.groupby('Year_y')['Number_of_Casualties'].sum().reset_index()
total_annual_casualties

# Plot of total annual casualties

plt.figure(figsize=(10, 6))
sns.lineplot(x='Year_y', y='Number_of_Casualties', data=total_annual_casualties, color = 'red')
plt.title('Total Number of Casualties per Year (2005 - 2016)')
plt.xlabel('Year')
plt.ylabel('Total Number of Casualties')

# Total monthly casualties 

total_monthly_casualties = monthly_trends.groupby('Month_Name')['Number_of_Casualties'].sum().reset_index()
total_monthly_casualties

# Plot 

plt.figure(figsize=(12,8))
sns.lineplot(x='Month_Name', y='Number_of_Casualties', data=total_monthly_casualties, color='red')
plt.title('Total Number of Casualties by Month (2005 - 2016)')
plt.xlabel('Month')

# EXPORT THE DATA IN CSV

df_selected.to_csv('Traffic_Accidents_Cleaned.csv', index=False)

print('Data exported successfully to Traffic_Accidents_Cleaned.csv')

