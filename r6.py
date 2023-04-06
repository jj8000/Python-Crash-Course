
alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

alien_0['color'] = 'żółty'
alien_0['speed'] = 'średnio'
print(alien_0)

if alien_0['speed'] == 'wolno':
    x_increment = 1
elif alien_0['speed'] == 'średnio':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

language = favorite_languages['sara'].title()
print(language)
points_value = alien_0.get('points', "Brak wyników")
print(points_value)

fav_numbers = {
    'janek': 3,
    'sara': 7,
    'edward': 1,
    'paweł': 8,
    }

for x, y in fav_numbers.items():
    print(f"{x} - {y}")

for x in fav_numbers:
    print(f"{x.title()}\n\t{fav_numbers[x]}")

user_0 = {
    'username': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski'
}

for k, v in user_0.items():
    print(f"\n{k}")
    print(f"{v}")

l = [2, 88, [], [4, 5, 0, [5, 7]], 4, 4, 9022, [6, 7, 0], [1], [8, [7], [[[77]]], 90, [0, [23, 67, [76, 6, [5], 8],]], 0], 11]
splaszczona_lista = []

def splaszcz(arg):

    for i in arg:
        if type(i) != list:
            splaszczona_lista.append(i)
        else:
            splaszcz(i)
    return(splaszczona_lista)

print(splaszcz(l))