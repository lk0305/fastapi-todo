from email import message

name = "'111'"
print(name)
print(type(name))

name = """111"""
print(name)
name = "\"111\""

print(name)
# 表达式
name = "水果橙子"
year = "19"
print(f"我是{name}，今年{year}岁")
#如何格式化表达式
print("1.txt*1的结果是：%d"%(1*1))
print(f"1.txt*1的结果是：{1*1}")
print("字符串在python中的类型是：%s"% type('字符串'))
name = "橙子"
pre_price = 19.99
good_num = "1008"
pre_price_daily_growth_factor= 1.2
growth_days = 7
pre_price2 = pre_price*pre_price_daily_growth_factor**growth_days
print(f"{name},商品编号：{pre_price}，当前均价：{good_num}")
message = "每日增长系数:%.1f,经过%d天的增长后，均价达到了：%.2f" %(pre_price_daily_growth_factor,growth_days,pre_price2)
print(message)
#print 输入
#input 输出
"""print("请告诉我你是谁")
name = input()
print("你好，我是：%s" % name)"""
name = input("请告诉我你是谁")
print("你好，我是：%s" % name)