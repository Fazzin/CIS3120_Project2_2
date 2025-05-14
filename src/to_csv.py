'''
The parameters that the function takes are dictionaries.
The roster that it pulls from is a dictionary
The function iterates through the dictionary:
    1) Converts the dataframe into CSVs
    2) Prints the category of each sport and how many rows of data has been saved to the CSV file
'''

def to_csv(roster):    
    for key, df, in roster.items(): #Iterates through the dictionary by key and df (category and dataframe)
        df.to_csv(f'{key}.csv', index=False) #Converts dataframe into a csv by the category name.csv (Also removes index)
        print(f'{key}: {len(df)} rows saved to {key}.csv') 
