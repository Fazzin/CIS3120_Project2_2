'''
Function for finding the names and heights of the athletes with the 5 shortest heights for both men and women in each sport.
'''

'''
Notes:
df must be a pandas.DataFrame
n is an int with a default value of 5 
col is a string
the result returns a dataframe
'''

def shortest_height(df, n = 5, col="Height"):
    df_sorted = df.sort_values(col, ascending=True).reset_index(drop=True) #Sorts the height column from smallest to largest and resets row num to 0
    row_of_cutoff = n - 1
    if row_of_cutoff >= len(df_sorted): #In case the roster is smaller than n (5)
        row_of_cutoff = len(df_sorted) - 1 
    cut_off_height = df_sorted.loc[row_of_cutoff, col] #Looks up the single cell of the nth (5 in this case) shortest person
    mask = df_sorted[col] <= cut_off_height #Boolean is true if the athlete's height is less than the cutoff
    df_shortest = df_sorted[mask][["Name", col]] #Filter the sorted DataFrame using the mask to keep only the "Name" and height columns
    return df_shortest
