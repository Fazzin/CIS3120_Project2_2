'''
Finds the average height in each of the 4 dataframes. 4 averages in total.
'''

import pandas as pd

def average_height(avg_height1, avg_height2, avg_height3, avg_height4): 
    data = {
        'Team Category' : ["Men's Volleyball Team", "Men's Swimming & Diving Team", "Women's Volleyball Team", "Women's Swimming & Diving Team"],
        'Average Height' : [avg_height1, avg_height2, avg_height3, avg_height4], # List of average heights provided as function arguments
        'Rounded Average Height' : [round(avg_height1), round(avg_height2), round(avg_height3), round(avg_height4)] # rounded average heights using round function
    }
    df = pd.DataFrame(data) # convert dictionary to pandas dataframe 
    return df
