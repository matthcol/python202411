from city import City


city01 = City(name='Bourg-en-Bresse', zipcode='01000', population=41525)
city31 = City(name='Toulouse', zipcode='31000', population=477000)

city01 += city31
print(city01)