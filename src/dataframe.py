'''
Compiles a dataframe of all the names and heights of the players on the men and women's sports team.
'''

import pandas as pd

def sports_dataframe(names, heights):
    data = {
        'Name' : names,
        'Height' : heights
    }
    df = pd.DataFrame(data)
    avg_height = sum(heights) / len(heights) #Divides the sum of the heights and the total heights to find the average
    return df, avg_height
