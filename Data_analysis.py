import pandas as pd

# Read csv files using pandas
olympic = pd.read_csv("athlete_events.csv") 
regions = pd.read_csv("country_definitions.csv")
merged = pd.merge(olympic, regions, on='NOC', how='left') # merge 2 previous loaded files

# Search for 3 differed medals
gold_medals = merged[(merged.Medal == 'Gold')]
silver_medals = merged[(merged.Medal == 'Silver')]
bronze_medals = merged[(merged.Medal == 'Bronze')]

# Search for total of medals in top 6 country
total_Gold_Medals = gold_medals.region.value_counts().reset_index(name='Medal').head(6)
total_Silver_Medals = silver_medals.region.value_counts().reset_index(name='Medal').head(6)
total_Bronze_Medals = bronze_medals.region.value_counts().reset_index(name='Medal').head(6)

print("\nNumber of gold medals:")
print(total_Gold_Medals)
print("\nNumber of silver medals:")
print(total_Silver_Medals)
print("\nNumber of bronze medals:")
print(total_Bronze_Medals)