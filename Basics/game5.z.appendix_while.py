#接game5.py
###练习（难）
guest_list=['a','s','d','f','g','h','j','k','j']
for guest in guest_list:
 print(f"Dear {guest}, i would like to invite you to dinner.") #一个一个邀请客人
can_not=guest_list.pop(2)
print(f"Sorry,{can_not} can't come to dinner.")
guest_list[2]='t'
for guest in guest_list:
 print(f"Dear {guest}, i would like to invite you to dinner.")
print("I't great, I found a bigger table,I can invite more people.")
guest_list.insert(0,'q')
guest_list.insert(4,'w')
guest_list.append('e')
for guest in guest_list:
 print(f"Dear {guest},I would like to invite you to dinner.")
print("Sorry,new table can't come intime, I can only invite two people.")
#!#删除多余的客人(循环)#!#
while len(guest_list)>2:
    removed_guest=guest_list.pop()
    print(f"Sorry,{removed_guest},I can't invite you to dinner.")
print(f"Dear {guest_list},I would like to invite you to dinner.")
del guest_list[0]
del guest_list[0]
print("the final guest list is:", guest_list)
