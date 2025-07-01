#字符串练习#

#改变字符串大小写
name="ai love me."
print(name.upper())  #全大写 .upper()

nawe="i love world."
print(nawe.title())  #开头大写 .title()

mama="qu ni ma de."
print(mama.lower())  #全小写 .lower()
#合并变量
a_name="aha"
b_name="moment"
f_name=f"{a_name} {b_name}"  #空格可有可无
print(f_name)
message=f"HELLO , {f_name.title()} !"  #字符串创建消息 f
print(message)

#使用制表符和换行符来添加空白
print("AI.1")  #普通
print("\tAI.1") #制表符 \t
print("I\nLOVE\nYOU\nAI")  #换行符 \n
print("I\n\tYOU\n\tSHE\n\tHE")  #换行+空格 \n\t

#删除空白
f_language="   python  "
print(f_language)
print(f_language.rstrip())  #右端去空格 .rstrip()
print(f_language.lstrip())  #左端去空格 .lstrip()

#删除前缀
nostrip_url="https://python.com"
print(nostrip_url)  #正常
print(nostrip_url.removeprefix('https://'))  #删除 .removeprefix('要删的东西')




###练习1###
name="Eric"
message=f"Hello {name},would you like to learn python?"  #不要忘了 f
print(message)
###练习2###
name2="ahasbby toppy"
print(name2.upper())  #全大写
print(name2.lower())  #全小写
print(name2.title())  #开头大写
###练习3###
SAY='Albert Einstein once said,"A persion who never made a mistake never tired anything new."'
print(SAY)  #字符串应用
###练习4###
namee="\tSantty\nHubby\twhatty "
print(namee)
print(namee.rstrip())  #后面去空格!(不熟)！
print(namee.lstrip())  #前面去空格
print(namee.strip())  #前后都去空白 .strip()                                                    *



