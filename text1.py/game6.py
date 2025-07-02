###管理列表###
#永久排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)   #按字母顺序排列   .sort()
cars.sort(reverse=True)   #按字母顺序的相反顺序排列
print(cars)
#临时排序
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))   #按字母顺序排列列表，但不改变原列表      sortsd(~)
print("\nHere is the original list again:")
print(cars)
print(sorted(cars,reverse=True))  #按字母顺序的相反顺序排列列表，但不改变原列表   sortsd(~,reverse=True)
#反向打印列表
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)   #反向打印列表   .reverse()
cars.reverse()   #恢复到原来的顺序
print(cars)   
#确定列表的长度
cars=['bmw','audi','toyota','subaru']
print(len(cars))   #确定列表的长度   len()
###练习###
#练习1
Worlds=['China','America','Japan','Korea']
print(Worlds)
sorted_Worlds=sorted(Worlds)  
print(sorted_Worlds)
print(Worlds)
print(sorted(Worlds,reverse=True))
print(Worlds)
Worlds.reverse()
print(Worlds)   
Worlds.reverse()
print(Worlds)
Worlds.sort()
print(Worlds) 
Worlds.sort(reverse=True)
print(Worlds)
#练习2
print(len(Worlds)) 
