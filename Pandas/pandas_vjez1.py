import pandas as pd

df = pd.read_csv('pokemon_data.csv')
#df = pd.read_excel('pokemon_data.xlsx')
#df = pd.read_csv('pokemon_data.txt', delimiter='\t')

#print(df)
#print(df.head(3))

    ##read headers
#print(df.columns)


    ##read each column
#print(df['Name'][0:5])
#print(df[['Name','HP','Speed']][0:5])

    ##read each row
#iloc=integer location
#print(df.iloc[0:5])
#for index,row in df.iterrows():
    #print(index,row['Name'])
#print(df.loc[df['Type 1']=='Fire'])

    ##read a specific location (R,C)
#print(df.iloc[0,1])
#print(df.iloc[4,1])

#print(df.describe())
#print(df.sort_values('Name'))
#print(df.sort_values('Name', ascending=False))
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

    ##making changes to data

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df.head(7))
#df = df.drop(columns=['Total'])
#print(df.head(5))

#df['Total']=df.iloc[:,4:10].sum(axis=1)

#cols= list(df.columns.values)
#df = df[cols[0:4]+[cols[-1]]+cols[4:12]]
#print(df.head(5))
    
    ##Saving our Data (Exporting into Desired Format)

#df.to_csv('modified_pokemon_data.csv', index=False)
#df.to_csv('modified_pokemon_data.txt', index=False, sep='\t')


    ##filtering data
#print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')])
#print(df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison')])
#print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')&(df['HP']>70)])  
#new_df= (df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')&(df['HP']>70)]) 
# & is and in Pandas,   | is or 
#new_df.to_csv('filtered.csv')

#new_df.reset_index(drop=True, inplace=True)
#print(new_df)

#df = df.loc[df['Name'].str.contains('Mega')]
# ~ - dosent contain
#df = df.loc[~df['Name'].str.contains('Mega')]



    ##Aggregate Statistics (Groupby)
#df = pd.read_csv('pokemon_data.csv')
#df['count'] = 1
#print(df.groupby(['Type 1']).count()['count'])
#print(df.groupby(['Type 1','Type 2']).count()['count'])

    ##working with large amounts of data
new_df= pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified_pokemon_data.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

new_df = pd.concat([new_df, results])
print(new_df)
