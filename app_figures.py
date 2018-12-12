import requests
import csv
import urllib
from bs4 import BeautifulSoup
#the previous lines import the required modules

# create the page variable to request and store the url
page = requests.get('https://appfigures.com/top-apps/google-play/united-states/top-overall')

# create soup as the BeautifulSoup object and assign a html parser to use 
soup = BeautifulSoup(page.content,"html.parser")  #beautifulsoup object

# creates/opens appfigures.cvs for writing and stores it is the variable csv_file
with open("appfigures.csv","w+", encoding="utf-8") as csv_file:
            
            # assigns 3 titles for the headers of the 3 columns to be saved in appfigures.csv
            fieldnames = ["App_Name", "App_Docid", "App_Rank"]
            
            #tells the writer what file to write in and what to write in each column of the csv_file
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            #tells the writer to go ahead and write what was asked in the previous line
            writer.writeheader()
            
            # searches for all the data in the soup that belongs to this class and div
            for data in soup.find_all('div', class_='s177842908-0 s1376732636-1'):
                        #searches for a inside the 'a' tags in the same class as above
                        for a in data.find_all('a'):
                                    
                                    #assigns the text found between the tag to the variable and adds a space or tab following each one
                                    one = a.get('title') # gets the App_Name
                                    
                                   
                                   # b gets the href only
                                    b = a.get('href')
                                    # variable two splits the href at the = and only keeps the right side of the string or index[1]
                                    two = (b.split("=")[1]) # two is equal to the App_Docid
                                    
                                    #variable three gets the rank 
                                    three = a.text[0]  # three is equal to App_Rank
                               
                                #tells the writer to write the data crawled and stored in one, two, and three into the rows of the csv_file
                                    writer.writerow({"App_Name": one, "App_Docid": two, "App_Rank": three})
            
            #This data is found in the appfigures.csv file 
