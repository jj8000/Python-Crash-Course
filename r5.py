cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'pieczarki'

if requested_topping != 'anchois':
    print("Dawaj anchois!")

print()
alien_color = 'czerwony'

if alien_color == 'zielony':
    print("Zarobiłeś pięć punktów!")
elif alien_color == 'żółty':
    print("Zarobiłeś dziesięć punktów!")
else:
    print("Zarobiłeś piętnaście punktów!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Dodaję {requested_topping}.")
    print("Gotowe!")
else:
    print("Czy na pewno pizza bez dodatków?")

current_users = ['Janek', 'Orzeł', 'Jajo12', 'Kapsel']
current_users_lc = [user.lower() for user in current_users]
new_users = ['Karol', 'Janek', 'jaJO12']

for user in new_users:
    if user.lower() in current_users_lc:
        print(f'nazwa użytkownika "{user}" już w użyciu')
    else:
        print(f'nazwa "{user}" przyjęta')

numbers = [i for i in range(1, 10)]
print(numbers)

for i in numbers:
    if i == 1:
        print('1st')
    elif i == 2:
        print('2nd')
    elif i == 3:
        print('3rd')
    else:
        print(f"{i}th")

