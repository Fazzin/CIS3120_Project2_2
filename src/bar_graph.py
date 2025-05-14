'''
The function has one parameter, a dataframe. Expects it with columns
The function converts the dataframe into a bar graph.
There are some minor adjustments to the bar graph to ensure that data is illustrated effectively.
Finally, the function pops a window of the bar graph figure and closes the figure to save memory.
'''

import matplotlib.pyplot as plt

def bar_graph(avg_height):
    bar_graph = avg_height.plot.bar(x="Team Category", y="Average Height", title="Average Heights Among Athletes")
    plt.ylabel("Average Height (inches)") #Y axis label
    plt.tight_layout() #Ensures every text fits into the bar graph image
    plt.show()
    plt.close() #Saves memory by closing the same figure (if we ever use a different bar graph)
    return bar_graph #Return is not needed but may be useful in the future as it returns the axes object
