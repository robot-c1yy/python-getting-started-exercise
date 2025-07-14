###第八天###
##嵌套##
#字典列表
alien_0 = {'color': 'green','points': 5}
alien_1 = {'color': 'yellow','points': 10}
alien_2 = {'color': 'red','points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
#创建一个用于储存外星人的空列表
aliens = []
#创建 30 个绿色的外星人(一样的)
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#显示前 5 个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")

#创建一个用于存储外星人的空列表
aliens = []
#创建 30 个绿色外星人
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10   
#显示 5 个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#扩展
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print('\n')
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
#在字典中储存列表
#储存顾客所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#概括顾客点的比萨
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\n{topping}")
#在字典中储存字典
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in user.items():
    print(f"\nUsername: {username}")
    full_name =f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

###练习###
#练习1
namme_0 = {
    'first': 'emma',
    'last': 'wilson',
    'age': 28,
    'city': 'london'
}
namme_1 = {
    'first': 'liam',
    'last': 'davis',
    'age': 32,
    'city': 'new york'
} 
namme_2 = {
    'first': 'sophia',
    'last': 'taylor',
    'age': 25,
    'city': 'sydney' 
}
people = [namme_0,namme_1,namme_2]
for person in people:
    print(f"First name:{person['first'].title()}")
    print(f"Last name: {person['last']}.title()")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city']}.title()\n")
#练习2
pet_0 = {
    'ani_type': 'dog',
    'owner': 'alice'
}
pet_1= {
    'ani_type': 'cat',
    'owner': 'bob'
}
pet_2 = {
    'ani_type': 'rabbit',
    'owner': 'charlie'
}
pet_3= {
    'ani_type': 'parrot',
    'owner': 'diana'
}
pets= [pet_0,pet_1,pet_2,pet_3]
for pet in pets:
    print(f"\nOwner: {pet['owner'].title()}")
    print(f"\tAnimal Type: {pet['ani_type']}")
#练习3
favorite_places= {
    'alice': ['lira','voss','zara'],
    'emma': ['milo','nara','sora'],
    'ethan': ['kona','jura','lune']
}
for name, places in favorite_places.items():
    print(f"\nName: {name.title()}")
    print("Favorite Place:")
    for place in places:
        print(place.title())
friends= ['bob','juddy','landan']
for friend in friends:
    print(f"\tPlease tell your favorite place, {friend.title()}.")
print('Thank everyone!')