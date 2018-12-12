import requests 
import csv
from bs4 import BeautifulSoup
#the previous lines import the required modules

url = "https://play.google.com/store/apps" 
# request url
r = requests.get(url)

# create BeautifulSoup Object and assign an html parser
soup = BeautifulSoup(r.content,"html.parser")

# open testFile.csv for writing and open it as a variable, csv_file
with open("testFile.csv","w+", encoding="utf-8") as csv_file:
            
            # assign the headers of the 3 data columns to be collected
            fieldnames = ["App_Name", "App_Url", "App_Docid"]
            
            # tell the writer to what file to write it in and what to write
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            # Write the three fieldnames into csv_file
            writer.writeheader()
            
            # search for all data in the soup that belongs to this class
            for data in soup.find_all('div', class_='b8cIId ReQCgd Q9MA7b'):
                        # search for a inside the 'a' tags in this class
                        for a in data.find_all('a'):
                                    
                                    #assign the text found between the tag to a variable and add a tab space after each 
                                    one = (a.text + "\t") #gets the App_Name
                                    
                                    # variable two equals a combination of the base url and href followed by a tab space for each
                                    #two gets the App_Url 
                                    two = ("https://play.google.com" + a.get('href') + "\t") 
                                   
                                    
                                    #variable b equals the href
                                    b = a.get('href') 
                                    
                                    #variable three splits the href at the = and only keeps the right side or index 1 of the string
                                    # Variable three equals the App_Docid
                                    three = (b.split("=")[1])
                                    
                                    #writes the collected data into rows
                                    writer.writerow({"App_Name": one, "App_Url": two, "App_Docid": three})
                                    
#Look for this crawled data in testFile.csv 
        
                
        

        
         

    




            
    



    
    