import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook

excel = openpyxl.Workbook()
sheet = excel.active

sheet.append(["Car Name","Car Company","Price","Purchased Year","Fuel","Kilometers Travelled","Transmission","Location"])

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'}
# Hyderabad
Hundayi_data = requests.get("https://www.cardekho.com/used-hyundai+cars+in+hyderabad",headers=headers)
soup = BeautifulSoup(Hundayi_data.text, "html.parser")

#print(data.raise_for_status())

Tata_data = requests.get("https://www.cardekho.com/used-tata+cars+in+hyderabad",headers=headers)
Tata = BeautifulSoup(Tata_data.text, "html.parser")

Mahindra_data = requests.get("https://www.cardekho.com/used-mahindra+cars+in+hyderabad",headers=headers)
Mahindra = BeautifulSoup(Mahindra_data.text, "html.parser")

Honda_data = requests.get("https://www.cardekho.com/used-honda+cars+in+hyderabad",headers=headers)
Honda = BeautifulSoup(Honda_data.text, "html.parser")

#Banglore
Hundayi_Banglore = requests.get("https://www.cardekho.com/used-hyundai+cars+in+bangalore",headers=headers)
B_Hundayi = BeautifulSoup(Hundayi_Banglore.text,"html.parser")

Tata_Banglore =  requests.get("https://www.cardekho.com/used-tata+cars+in+bangalore",headers=headers)                   
B_Tata = BeautifulSoup(Tata_Banglore.text,"html.parser")

Mahindra_Banglore =  requests.get("https://www.cardekho.com/used-mahindra+cars+in+bangalore",headers=headers)                   
B_Mahindra = BeautifulSoup(Mahindra_Banglore.text,"html.parser")

Honda_Banglore =  requests.get("https://www.cardekho.com/used-honda+cars+in+bangalore",headers=headers)                   
B_Honda= BeautifulSoup(Honda_Banglore.text,"html.parser")

#Hyderabad Cars
Hundayi_cars = soup.find("body").find("div",class_="listViewCard").find("div",class_="gsc_row")\
           .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")

for car in Hundayi_cars:
    try:
        name = car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string

        car_company = car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[1]

        price = car. find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year =  int(car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("div",class_="dotsDetails")\
                    .text.split("•")[1]

        travelled = car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                        .find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                            .find("div",class_="dotsDetails").text.split("•")[2]

        location = car. find("div",class_="NewUcExCard posR").find("div",class_="distanceText").text.split(",")[1]
        
        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue


Tata_cars =Tata.find("body").find("div",class_="listViewCard").find("div",class_="gsc_row")\
           .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")

for tata_car in Tata_cars:
    try:
        name = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string

        car_company = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[1]

        price = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year =  int(tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("div",class_="dotsDetails")\
                    .text.split("•")[1]

        travelled = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                        .find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                            .find("div",class_="dotsDetails").text.split("•")[2]

        location = tata_car. find("div",class_="NewUcExCard posR").find("div",class_="distanceText").text.split(",")[1]
        
        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue

Mahindra_cars =Mahindra.find("body").find("div",class_="listViewCard").find("div",class_="gsc_row")\
               .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")

for mahindar_car in Mahindra_cars:
    try:
        name = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string
        
        car_company = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[1]

        price = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year = int(mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("div",class_="dotsDetails")\
                    .text.split("•")[1]

        travelled = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                        .find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                            .find("div",class_="dotsDetails").text.split("•")[2]

        location = mahindar_car. find("div",class_="NewUcExCard posR").find("div",class_="distanceText").text.split(",")[1]
        
        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue

Honda_cars =Honda.find("body").find("div",class_="listViewCard").find("div",class_="gsc_row")\
        .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")


for honda_car in Honda_cars:
    try:
        name = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string

        car_company = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[1]

        price = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year = int(honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("div",class_="dotsDetails")\
                    .text.split("•")[1]

        travelled = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                        .find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section")\
                            .find("div",class_="dotsDetails").text.split("•")[2]

        location = honda_car. find("div",class_="NewUcExCard posR").find("div",class_="distanceText").text.split(",")[1]
        
        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue

#Banglore Cars
B_Hundayi_cars = B_Hundayi.find("body").find("div",class_="app-content").find("div",class_="gsc_row")\
                    .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")
                    
for B_Hundayi_car in B_Hundayi_cars:
    try:
        name =  B_Hundayi_car.find("h3",class_="title").find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string

        car_company = B_Hundayi_car.find("h3",class_="title").find("a").text.split(" ")[1]

        price = B_Hundayi_car.find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year =  int(B_Hundayi_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = B_Hundayi_car.find("div",class_="dotsDetails").text.split("•")[1]

        travelled = B_Hundayi_car.find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = B_Hundayi_car.find("div",class_="dotsDetails").text.split("•")[2]

        location = B_Hundayi_car.find("div",class_="NewUcExCard posR").find("div",class_="bottom_container").find("div",class_="distanceText")\
                                .text.split(",")[1]

        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue

B_Tata_cars = B_Tata.find("body").find("div",class_="app-content").find("div",class_="gsc_row")\
                    .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")

for B_Tata_car in B_Tata_cars:
    try:
        name =  B_Tata_car.find("h3",class_="title").find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string
        
        car_company = B_Tata_car.find("h3",class_="title").find("a").text.split(" ")[1]

        price = B_Tata_car.find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year =  int(B_Tata_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = B_Tata_car.find("div",class_="dotsDetails").text.split("•")[1]

        travelled = B_Tata_car.find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = B_Tata_car.find("div",class_="dotsDetails").text.split("•")[2]

        location = B_Tata_car.find("div",class_="NewUcExCard posR").find("div",class_="bottom_container").find("div",class_="distanceText")\
                                .text.split(",")[1]
        
        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue

B_Mahindra_cars = B_Mahindra.find("body").find("div",class_="app-content").find("div",class_="gsc_row")\
                    .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")

for B_Mahindra_car in B_Mahindra_cars:
    try:
        name =  B_Mahindra_car.find("h3",class_="title").find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string
     
        car_company = B_Mahindra_car.find("h3",class_="title").find("a").text.split(" ")[1]

        price = B_Mahindra_car.find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year =  int(B_Mahindra_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = B_Mahindra_car.find("div",class_="dotsDetails").text.split("•")[1]

        travelled = B_Mahindra_car.find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = B_Mahindra_car.find("div",class_="dotsDetails").text.split("•")[2]

        location = B_Mahindra_car.find("div",class_="NewUcExCard posR").find("div",class_="bottom_container").find("div",class_="distanceText")\
                                .text.split(",")[1]

        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue

B_Honda_cars = B_Honda.find("body").find("div",class_="app-content").find("div",class_="gsc_row")\
                    .find_all("div",class_="gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-4 cardColumn")

for B_Honda_car in B_Honda_cars:
    try:
        name =  B_Honda_car.find("h3",class_="title").find("a").text.split(" ")
        name.pop(0)
        result=""
        for string in name:
            result+= " "+string
       
        car_company = B_Honda_car.find("h3",class_="title").find("a").text.split(" ")[1]
        
        price = B_Honda_car.find("div",class_="NewUcExCard posR").find("div",class_="Price hover").find("p").text.split(" ")[0].split("₹")[1]

        purchased_year =  int(B_Honda_car. find("div",class_="NewUcExCard posR").find("div",class_="title_heart_section").find("h3",class_="title")\
                    .find("a").text.split(" ")[0])

        fuel = B_Honda_car.find("div",class_="dotsDetails").text.split("•")[1]

        travelled = B_Honda_car.find("div",class_="dotsDetails").text.split("•")[0].split(" ")[0]

        transmission = B_Honda_car.find("div",class_="dotsDetails").text.split("•")[2] 

        location = B_Honda_car.find("div",class_="NewUcExCard posR").find("div",class_="bottom_container").find("div",class_="distanceText")\
                                .text.split(",")[1]

        print(result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location)
        sheet.append([result,car_company,float(price)*100000,purchased_year,fuel,travelled,transmission,location])

    except:
        continue
    
excel.save(r"D:\My Projectss\Used_Cars_Sales_Data.xlsx")