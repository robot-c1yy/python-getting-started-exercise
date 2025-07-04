###第二天###
poetry="""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""" #python之禅
print(poetry)

##列表##
bicycle=['trek','cannondale','redline','specialized']
print(bicycle)   #列表表示   []
#访问列表元素
print(bicycle[0])   #访问第一个元素       [0]
print(bicycle[0].title())   #访问第一个元素并将首字母大写       [0].title()
#其他也是要访问元素位数减一
print(bicycle[-1])   #访问最后一个元素   [-1]
print(bicycle[3])
#使用列表中各个值
message=f"My favorite bicycle is {bicycle[1].title()}."
print(message)

####练习####
#练习1
names=['Awey','Ehuty','fuhty','Ruioy','Aopky']
print(names[-2])
print(names[4])
#练习2
message1=f"Hello,{names[2]} is great to see you."
print(message1)
message2=f"Hello,{names[0]} is a superstar."
print(message2)
#练习3
F_work=['ahid','sdfg','sfgdu','uiim','iuhf','ujyf']
message3=f"Hello {F_work[0].title()},you are a good persion."
print(message3)

#修改、添加和删除元素
tiuhwq=['arsd','rfjsh','ertj','hfy','gtd','dftgyk']
tiuhwq[2]='rytibd'
print(tiuhwq)   #修改元素   [~]='...'
print(tiuhwq[2])
tiuhwq.append('fkdio')   #在末尾添加元素   .append()
print(tiuhwq)

asdf=[]
asdf.append('rgjiic')
asdf.append('ehbu')
asdf.append('aruob')
asdf.append('eyvsu')
asdf.append('rwsvbij')
print(asdf)   #添加多个元素
asdf.insert(0,'d7yc')
print(asdf)   #在指定位置插入元素   .insert(数，'~')
del asdf[1]   #删除元素   del ...[数]
print(asdf)   
qwer1=asdf.pop()
print(qwer1)   #删除末端元素并返回该元素   
print(asdf)   #删除末端元素  .pop()
message4=f"You are very {qwer1.title()}."
print(message4)   #使用已删除的元素
#!#!#!#!#!# del语句：不用已删除的元素 VS pop()方法：可以使用已删除的元素 #!#!#!#!#
asdf.remove('ehbu')      #根据值删除元素 .remove('~') 
print(asdf)
rwtyhf='aruob'
asdf.remove(rwtyhf)
print(asdf)
print(f"A {rwtyhf.title()} is good.")   
#!#!#remove()方法只删除第一个指定值#!#!#
#!#!#!#如果要删除的值在列表中出现多次,需要用循环，确保除干净#!#!#!#
#练习见game5.appendix_while.py


      

