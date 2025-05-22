'''
Scraping the data of all the names and heights of the players in each sport, men and women's teams.
'''
import requests
from bs4 import BeautifulSoup

def process_data(urls):
    names = [] #List for storing names
    heights = [] #List for storing heights
    for url in urls: #For loop to visit each url
        page = requests.get(url)
        if page.status_code == 200: #Process data on a website if the request is sucessful
            soup = BeautifulSoup(page.content, 'html.parser')
            height_tags = soup.find_all('td', class_='height')
            name_tags = soup.find_all('td', class_='sidearm-table-player-name')

            #Using zip function, it pairs name tag with height tag and iterates both
            #In every iteration, we are working with ONE athlete only
            for name_tag, height_tag in zip(name_tags, height_tags):
                raw_height = height_tag.get_text() #Extracts the height, originally in feet and inches
                if(raw_height == '-'): #In case the data is unfilled (blank heights), medgar evans college in this case
                    continue #Proceed to the next iteration of the loop
                feet = float(raw_height.split('-')[0]) * 12 #Converts feet to inches
                inches = float(raw_height.split('-')[1]) #Extracts the inches
                height_in_inches = feet + inches
                names.append(name_tag.get_text().strip()) #Strips any empty space, extra space, line-breaks, or tabs for the names
                heights.append(height_in_inches)

    return names, heights
    
