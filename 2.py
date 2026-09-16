布尔型 = ("真假")
print(布尔型)
b = True
print(b)
print(type(b))
#list-列表
c = [10,20,30]
print(type(c))
#tuple-元组
d = (10,20,30)
print(type(d))
#set-集合
e = {10,20,30}
print(type(e))
#dict--字典--键值对
f = {"name":"tom","age":18}
print(f["name"])
print(f["age"])
print(type(f))
if False:
    print("条件成立执行代码1")
    print("条件成立执行代码2")

print("条件成立执行代码3")
age = input("请输入你的年龄")
if age <= "18":
    print("童工")
elif (age >= "18") and (age <= "60"):
    print("合法")
else:
    print("退休")
print("系统关闭")
import random
print("0--石头，1.txt--剪刀，2--布")
player = int(input("玩家出拳"))
computer = random.randint(0,2)
print("电脑出拳",computer)
if ((player == 0)and(computer == 1))or((player == 1)and(computer == 2))or((player == 2)and(computer == 0)):
    print("玩家获胜")
elif (player == computer):
    print("平局")
else:
    print("电脑获胜")

