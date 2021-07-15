import os
import csv

csvpath = os.path.join("Pixies_tour.csv")


with open('Pixies_tours.csv', 'r') as file:
    Pixies_tours = csv.reader(file, delimiter=',')

print(Pixies_tours)
    
    

# # key = 2e6353fbfb1c46b9b584abfe80e40aed
# from opencage.geocoder import OpenCageGeocode
# geocoder = OpenCageGeocode("2e6353fbfb1c46b9b584abfe80e40aed")


# # create empty lists
# list_lat = []   

# list_long = []


# # iterate over rows in dataframe
	
# for index, row in Pixies_tours.iterrows(): 


#     City = row['City']
#     State = row['State']       
#     query = str(City)+','+str(State)

#     results = geocoder.geocode(query)   
#     lat = results[0]['geometry']['lat']
#     long = results[0]['geometry']['lng']

#     list_lat.append(lat)
#     list_long.append(long)

	
# # create new columns from lists    

# Pixies_tours['lat'] = list_lat   

# Pixies_tours['lon'] = list_long



