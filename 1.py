message = 'Witaj!'
print(message)

message = 'Żegnaj!'
print(message)

m_message = '1\\n2'
print(m_message)

name = "jan kowalski"
print(name.title())

name = name.title()

print(name)

print(name.upper())
print(name.lower())

first_name = "jan"
last_name = 'kowalski'
full_name = f'{first_name} {last_name}'
print(full_name.title())

print("\tXOX\n\tXOXOXOXOXO")

lang = ' python '

print(lang.rstrip())
print(lang.lstrip())
print(lang.strip())
print(lang.strip().upper())
print(lang.strip().title())
print()
pies = 'melon'

lista = (x for x in pies)

print(tuple(lista))
print(lista)

zdanie = "Melon zjada własny ogon"

zdanie2 = [x for x in zdanie if x != ' ']
print(zdanie2)

sklejone_zdanie = ''.join(zdanie2)
print(sklejone_zdanie)

imie = 'Kleofas'

message = f"Witaj, {imie}!"
print(message)

print(imie.lower())
print(imie.upper())
print(imie.title())

print('Andrzej powiedział: "Nie wrócę"')

osoba = "Andrzej"
message = f'{osoba} powiedział: "Nie wrócę"'
print(message)

# #############

