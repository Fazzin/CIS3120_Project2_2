'''
Main calls 9 functions 
1) Prints introduction
2) Scrape four roster categories (men/women, volleyball/swimming&diving) into variables
3) Build dataframes into variables
4) Prints the dataframes
5) Exports the dataframes into CSVs and SQLite (optional)
6) Computes top 5 tallest/shortest heights (includes duplicates so there may be more than 5) into a dataframe
7) Generates a bar graph figure (optional)

To run: python -m src.main 
'''

from .introduction import introduction
from .scraping import process_data
from .dataframe import sports_dataframe
from .average_height import average_height
from .tallest_height import tallest_height
from .shortest_height import shortest_height
from .bar_graph import bar_graph
from .to_csv import to_csv
from .to_sql import to_sql

def main():
    introduction()
    sports_teams = {
    #men's volleyball teams
    'mens_volleyball': ['https://ccnyathletics.com/sports/mens-volleyball/roster', 'https://lehmanathletics.com/sports/mens-volleyball/roster', 'https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster', 
                        'https://johnjayathletics.com/sports/mens-volleyball/roster', 'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster', 'https://mecathletics.com/sports/mens-volleyball/roster', 
                        'https://www.huntercollegeathletics.com/sports/mens-volleyball', 'https://yorkathletics.com/sports/mens-volleyball/roster', 'https://ballstatesports.com/sports/mens-volleyball/roster'],
    #men's swimming & diving teams
    'mens_swimming_diving': ['https://csidolphins.com/sports/mens-swimmin', 'https://yorkathletics.com/sports/mens-swimmi', 'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster', 
                               'https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster', 'https://lindenwoodlions.com/sports/mens-swimming-and-diving/roster', 'https://mckbearcats.com/sports/mens-swimming-and-diving/roster', 
                               'https://ramapoathletics.com/sports/mens-swimming-and-diving/roster', 'https://oneontaathletics.com/sports/mens-swimming-and-diving/roster', 'https://bubearcats.com/sports/mens-swimmin', 
                               'https://albrightathletics.com/sports/mens-swimming-and-diving/roster/2021-22'], 
    #women's volleyball teams
    'womens_volleyball': ['https://bmccathletics.com/sports/womens-volleyball/roster', 'https://yorkathletics.com/sports/womens-volleyball/roster', 'https://hostosathletics.com/sports/womens-volleyball/roster', 
                           'https://bronxbroncos.com/sports/womens-volleyball/roster/2021', 'https://queensknights.com/sports/womens-volleyball/roster', 'https://augustajags.com/sports/wvball/roster',
                           'https://flaglerathletics.com/sports/womens-volleyball/roster', 'https://pacersports.com/sports/womens-volleyball/roster', 'https://www.golhu.com/sports/womens-volleyball/roster'],
    #women's swimming & diving teams 
    'womens_swimming_diving': ['https://csidolphins.com/sports/womens-swimming-and-diving/roster', 'https://queensknights.com/sports/womens-swimming-and-diving/roster', 'https://yorkathletics.com/sports/womens-swimming-and-diving/roster', 
                                 'https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster/2021-22?path=wswim', 'https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster', 'https://lindenwoodlions.com/sports/womens-swimming-and-diving/roster', 
                                 'https://mckbearcats.com/sports/womens-swimming-and-diving/roster', 'https://ramapoathletics.com/sports/womens-swimming-and-diving/roster', 'https://keanathletics.com/sports/womens-swimming-and-diving/roster', 
                                 'https://oneontaathletics.com/sports/womens-swimming-and-diving/roster']
    }

    #Variables for scraping all the data 
    mens_volleyball_names, mens_volleyball_heights = process_data(sports_teams['mens_volleyball'])
    mens_swimming_diving_names, mens_swimming_diving_heights = process_data(sports_teams['mens_swimming_diving'])
    womens_volleyball_names, womens_volleyball_heights = process_data(sports_teams['womens_volleyball'])
    womens_swimming_diving_names, womens_swimming_diving_heights = process_data(sports_teams['womens_swimming_diving'])

    #Variables for creating the dataframe and the average height using the scraped data
    mens_volleyball_df, mens_volleyball_avg_height = sports_dataframe(mens_volleyball_names, mens_volleyball_heights)
    mens_swimming_diving_df, mens_swimming_diving_avg_height = sports_dataframe(mens_swimming_diving_names, mens_swimming_diving_heights)
    womens_volleyball_df, womens_volleyball_avg_height = sports_dataframe(womens_volleyball_names, womens_volleyball_heights)
    womens_swimming_diving_df, womens_swimming_diving_avg_height = sports_dataframe(womens_swimming_diving_names, womens_swimming_diving_heights)

    #Variable for average height for all four sport categories
    average_heights = average_height(mens_volleyball_avg_height, mens_swimming_diving_avg_height, womens_volleyball_avg_height, womens_swimming_diving_avg_height)

    #Variables for the five tallest heights using the dataframe
    mens_volleyball_tall, mens_volleyball_short = tallest_height(mens_volleyball_df), shortest_height(mens_volleyball_df)
    mens_swimming_diving_tall, mens_swimming_diving_short = tallest_height(mens_swimming_diving_df), shortest_height(mens_swimming_diving_df)
    womens_volleyball_tall, womens_volleyball_short = tallest_height(womens_volleyball_df), shortest_height(womens_volleyball_df)
    womens_swimming_diving_tall, womens_swimming_diving_short = tallest_height(womens_swimming_diving_df), shortest_height(womens_swimming_diving_df)

    #Dataframe of all current athletes as a dictionary
    rosters = {
        "Mens_Volleyball" : mens_volleyball_df,
        "Mens_Swimming_Diving" : mens_swimming_diving_df,
        "Womens_Volleyball" : womens_volleyball_df,
        "Womens_Swimming_Diving" : womens_swimming_diving_df
    }
    
    #Prints the category and dataframe using the dictionary for simplicity purposes
    for category, dataframe in rosters.items():
        print(f'\n{category} Roster')
        print(dataframe)

    #While loop for CSV
    while(True):
        export_answer = input("Would you like to export the rosters to CSV files? [Y/N] ").strip().lower() #Ensures all answers will be in lower case
        if export_answer in {"y", "yes"}:
            to_csv(rosters)
            break
        elif export_answer in {"n", "no"}:
            print("Data will not be exported.")
            break
        print("Please enter y / yes or n / no")
    #While loop for SQL
    while(True):
        export_answer = input("Would you like to export the rosters to a SQL Database? [Y/N] ").strip().lower() #Ensures all answers will be in lower case
        if export_answer in {"y", "yes"}:
            to_sql(rosters)            
            break
        elif export_answer in {"n", "no"}:
            print("Data will not be exported.")
            break
        print("Please enter y / yes or n / no")

    #Average height of all athletes in their respective sport and gender
    print(f'\nThe average height of the four sport categories are:\n {average_heights}')

    #Top 5 tallest athletes (includes duplicates, so might be more than 5) in their respective sport and gender
    print(f'\nThe tallest athletes for men\'s volleyball are: \n{mens_volleyball_tall}')
    print(f'\nThe shortest athletes for men\'s volleyball are: \n{mens_volleyball_short}')
    print(f'\nThe tallest athletes for men\'s swimming and diving are: \n{mens_swimming_diving_tall}')
    print(f'\nThe shortest athletes for men\'s swimming and diving are: \n{mens_swimming_diving_short}')
    print(f'\nThe tallest athletes for women\'s volleyball are: \n{womens_volleyball_tall}')
    print(f'\nThe shortest athletes for women\'s volleyball are: \n{womens_volleyball_short}')
    print(f'\nThe tallest athletes for women\'s swimming and diving are: \n{womens_swimming_diving_tall}')
    print(f'\nThe shortest athletes for women\'s swimming and diving are: \n{womens_swimming_diving_short}')

    #Generated bar graph for the average heights for the different team categories
    while(True):
        bar_answer = input("Would you like to generate a bar graph for the average heights? [Y/N] ").strip().lower() #Ensures all answers will be in lower case
        if bar_answer in {"y", "yes"}:
            print("The bar graph has been generated as a figure image!")
            bar_graph(average_heights) 
            break
        elif bar_answer in {"n", "no"}:
            print("No bar graph has been generated.")
            break
        print("Please enter y / yes or n / no")


if __name__ == "__main__":
    main()