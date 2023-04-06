# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(f'{magician.title()}, to była doskonała sztuczka!')
#     print(f'Nie mogę sie doczekać Twojej kolejnej sztuczki, {magician.title()}.\n')
#
# print("Dziękujemy wszystkim za występ")

for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

squares = (i**2 for i in range(1,6))
print(squares)
print(list(squares)[2])

even_numbers = list(range(2, 11, 2))
print(even_numbers)

print(sum(list(range(1, (10**6)+1))))

squares = [i**2 for i in range(1, 11)]
print(squares)

for i in range(1, 21):
    print(i)

mil_list = []
for i in range(1, 10**6+1):
    mil_list.append(i)

print(min(mil_list))
print(max(mil_list))
print(sum(mil_list))

for i in range(1, 21, 2):
    print(i)

list3 = [i**3 for i in range(3, 31)]
print()
for i in list3:
    print(i)

players = ['karol', 'martyna', 'michał', 'florian', 'ela']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[::2])

for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
friend_foods = my_foods[:]
my_foods.append('lody')
friend_foods.append('cannolo')

print(f"Moje ulubione potrawy:\t{my_foods}")
print(f"Twoje ulubione potrawy:\t{friend_foods}")

print(list(id(i) for i in my_foods))
print(list(id(i) for i in friend_foods))
print()
my_foods[0] = 'kluchy'

import copy

my_foods_deepc = copy.deepcopy(my_foods)

print(list(id(i) for i in my_foods))
print(list(id(i) for i in friend_foods))
print(list(id(i) for i in my_foods_deepc))

print(f"Moje ulubione potrawy:\t{my_foods}")
print(f"Twoje ulubione potrawy:\t{friend_foods}")

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

bufet = ('flaki', 'barszcz', 'pieczeń', 'szczupak', 'kompot')

for i in bufet: print(i)
print()
bufet = ('flaki', 'kalafiorowa', 'klops', 'leszcz', 'kompot')

for i in bufet: print(i)