print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[-2])
print(len(counties))
print(counties[0:2])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])
counties_dict = {}
counties_dict ["Arapahoe"] = 422829
print(counties_dict)
counties_dict ["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county) 

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:  
    print(county_dict.values())

for county_dict in voting_data:    
   for value in county_dict:      
       print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
     for key, value in county_dict.items():
         print(value)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters. ")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
print(f'{voting_data["county"]} county has {voting_data["registered_voters"]} registered voters.')

