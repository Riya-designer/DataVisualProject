import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('C:/Users/Riya/Downloads/Content/Zomato-data.csv')
print(dataframe.head())

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)
dataframe['rate'] =dataframe['rate'].apply(handleRate)
print(dataframe.head())

dataframe.info()
print(dataframe.isnull().sum())

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('Types Of Restaurant')
plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result,c = 'green', marker = 'o')
plt.xlabel('Types Of Restaurant')
plt.ylabel('Votes')
plt.show()

max_votes = dataframe['votes'].max()
restaurant_with_max_vote = dataframe.loc[dataframe['votes'] == max_votes,'name']
print('Restaurant with maximum votes is: ', restaurant_with_max_vote)

sns.countplot(x=dataframe['online_order'])
plt.xlabel('online order')
plt.ylabel('Count')
plt.show()

plt.hist(dataframe['rate'],bins=5)
plt.title('Rating Distribution')
plt.show()

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.xlabel('couple')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y='rate',data=dataframe)
plt.show()

pivot_table=dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap='YlGnBu',fmt='d')
plt.title('Pivot Table')
plt.xlabel('Online Order')
plt.ylabel('Listed In Type')
plt.show()