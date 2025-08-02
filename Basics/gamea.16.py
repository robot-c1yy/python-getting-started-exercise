###第十一天###
##函数##

#定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

#向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}! ")
greet_user("jesse")

###练习###
#练习1
def display_message(chaptername):
    """指出本章的主题"""
    print(f"The topics of this chapter are {chaptername.title()}")
display_message('flowers')

#练习2
def favorite_book(bookname):
    """指出书籍名字"""
    print(f"My favorite book is {bookname.title()}.")
favorite_book("wonderland")

#传递实参

#位置实参
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet(animal_type='hamster',pet_name='harry')   #关键字实参

#默认值
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet("any")

###练习###
#练习1
def make_shirt(T_size,T_pattern):
    """T恤制作详情"""
    print(f"\nThe site of this T-shirt is {T_size}.")
    print(f"Please add a {T_pattern} pattern.")

make_shirt('big','robot')
#练习2
def describe_city(city, country='China'):
    """打印一个描述城市所属国家的句子"""
    print(f"{city} is in {country}.")

describe_city('Beijing')
describe_city('Shanghai')
describe_city('Tokyo', 'Japan')

#返回值
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician) 

doog = get_formatted_name('sdgd','sffg','wtuy')
print(doog)
#返回字典
def build_person(first_nam,last_nam,age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_nam, 'last': last_nam}
    if age:
        person['age'] = age 
    return person

mmuctan = build_person('jimi','hendirx',age=27)
print(mmuctan)
#结合使用函数和While循环
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#这是一个循环！
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")

###练习###
#练习1
def city_country(city,country):
    cit_coun = f'"{city.title()}, {country.title()}"'
    return cit_coun
city_country('beijing', 'china')
yyy = city_country('beijing', 'china')
print(yyy)
