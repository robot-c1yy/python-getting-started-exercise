###第七天###
##字典##
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points=alien_0['points']
print(f"You just earned {new_points} points!")
#添加键值对
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#从创建一个空字典开始
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
#修改字典中的值
print(f"The alien is {alien_1['color']}.")
alien_1['color'] = 'yellow'
print(f"The alien is now {alien_1['color']}.")
##例子##
alien_2 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Origital position: {alien_2['x_position']}")
#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的移动速度一定很快
    x_increment = 3
#新位置为旧位置加移动距离
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New position : {alien_2['x_position']}")
#删除键值对
alien = {'color': 'green', 'position': 5}
print(alien)
del alien['position']
print(alien)              #删除（永远消失）  del ~
#访问值
point_value = alien.get('points','No point value assigned.')
print(point_value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}                         #末尾加逗号为以后加键值对做准备
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {favorite_languages['sarah']}.")

###练习###
#练习1
persion ={
    'first_name': 'Durry',
    'last_name': 'Green',
    'age': 17,
    'city': 'beijing'
}
print(persion)
favorite_numbers = {
    'sarsh': 10,
    'qurrt': 8,
    'juin': 9,
    'green': 6,
    'wahtf': 48
}
persion_0 = ['sarsh','qurrt','juin','green','wahtf']
for persion_1 in persion_0:
    print(f"\n{persion_1.title()}'s favorite number is {favorite_numbers[persion_1]}.")
    print(f"Is your favorate number {favorite_numbers[persion_1]}? {persion_1.title()}.")  

#遍历所有键值对           .items()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}                    
for name, language in favorite_languages.items():
    print(f"\nName: {name.title()}")
    print(f"Language: {language}")
    friends =['phil','sarah']
    if name in friends:
        print(f"\t{name.title()}, I see you love {language}!")
    else:
        print(f"\tHi, {name}. Is your favorite language {language}?")
    print(f"{name.title()}, thank you for taking the poll. @^_^@")
#遍历所有键              .keys()
for name in favorite_languages.keys():
    print(f"Hi,{name.title()}.")
#遍历所有值              .values()
for language in favorite_languages.values():
    print(language.title())
#剔除重复项              in set()
for language in set(favorite_languages.values()):
    print(language.title())

###练习###
#练习1
rivers = {'nile':'egypt', 'amazon': 'peru', 'yantze': 'china'}
for name, state in rivers.items():
    print(f"\nThe {name.title()} runs through {state.title()}.")
    print(f"River: {name.title()}" )
    print(f"Country: {state.title()}")    