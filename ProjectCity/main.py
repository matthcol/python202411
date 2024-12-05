from city import City


c1 = City('Toulouse', '31000', 477_000)
c2 = City(name='Pau', population=77_000, zipcode='64000')
c3 = City(name='Meillon', zipcode='64510')

for c in c1, c2, c3:
    print(c)
    print(c.name, c.population, c.zipcode, c.department())

c3.population = 943
print(c3)

print(c1 == c2)

c2bis = City(name='Pau', population=77_000, zipcode='64000')
print(c2 == c2bis)
print(c2 is c2bis)

c2.incr_population(23)
print(c2)

c5 = City.parse('Tournefeuille,31170,42')
print(c5)
