bicycles = ['trekingowy', 'górski', 'miejski', 'szosowy']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[-1].title())

message = f'To jest rower {bicycles[2].lower()}'
print(message)
print()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'kawasaki')
print(motorcycles)
del motorcycles[0]
print(motorcycles)

popped_moto = motorcycles.pop()
print(motorcycles)
print(popped_moto)

lista_gosci = ['AK', 'JJ', 'KY']

print(f'Zaproszenie dla {lista_gosci[0]}')

for x in lista_gosci:
    print(f'Zaproszenie dla {x}')


lista_gosci.remove('KY')
lista_gosci.insert(0, 'UL')
lista_gosci.insert(2, 'FC')
lista_gosci.append('TR')
print(lista_gosci)

while len(lista_gosci) > 2:
    popped_guest = lista_gosci.pop()
    print(f'Przeprosiny dla {popped_guest}')

print(lista_gosci)

del lista_gosci[0]
print(lista_gosci)
del lista_gosci[0]
print(lista_gosci)

cars = ['bmw', 'lada', 'isuzu', 'dodge']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

motorcycles.append('ducati')
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.reverse()
print(motorcycles)
print(len(cars))

miejsca = ['Iran', 'Chile', 'Japonia', 'Meksyk', 'Irlandia']
print(miejsca)

print(sorted(miejsca, reverse=True))
print(miejsca)
miejsca.reverse()
print(miejsca)
miejsca.reverse()
print(miejsca)
miejsca.sort()
print(miejsca)
miejsca.sort(reverse=True)
print(miejsca)

