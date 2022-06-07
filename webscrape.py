import bs4 as bs
import urllib.request
import csv

list = []
cont = True


while cont == True:
    #have user enter URL to scrape or enter "quit" to quit.
    print ("Input Quit to stop the program at any time")
    url = input ("Please enter in the website URL:")
    if url == "quit":
        cont = False
        break

    try:
        #get raw information and parse information
        #use error handling in case URL is not correct
        sauce = urllib.request.urlopen (url).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')

        #gets title of district
        district = soup.title.string
        district = district.split ("CSD")[0]
        print (district)
        print ("-------------------")


        #gets total students enrolled
        enroll = soup.find("span", id="total_students").text
        print (enroll)
        print ("-------------------")
    except:
        print ("Bad URL")


    #stores value in list of dictionaries - to be saved later
    list.append ({"District Name": district , "Enrollment": enroll} )

# create CSV file - get the csv writer to write the entire dictionary
with open('NY_State_District_Enrollment.csv', 'w', newline='') as file:
    header = ["District Name", "Enrollment"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for line in list:
        writer.writerow(line)


    print("Entered into spreadsheet called NY_State_District_Enrollment")
    file.close()
