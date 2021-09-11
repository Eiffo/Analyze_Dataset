import pandas as pd

olympic = pd.read_csv("athlete_events.csv")
regions = pd.read_csv("country_definitions.csv")
merged = pd.merge(olympic, regions, on='NOC', how='left')

gold_medals = merged[(merged.Medal == 'Gold')]
silver_medals = merged[(merged.Medal == 'Silver')]
bronze_medals = merged[(merged.Medal == 'Bronze')]

total_Gold_Medals = gold_medals.region.value_counts().reset_index(name='Medal').head(6)
total_Silver_Medals = silver_medals.region.value_counts().reset_index(name='Medal').head(6)
total_Bronze_Medals = bronze_medals.region.value_counts().reset_index(name='Medal').head(6)

print(total_Gold_Medals)
print('\n')
print(total_Silver_Medals)
print('\n')
print(total_Bronze_Medals)